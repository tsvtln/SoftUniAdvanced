from collections import deque as dq

materials_for_crafting = dq([int(x) for x in input().split()])
magic_level = dq([int(x) for x in input().split()])

present_values = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}

presents_crafted = {}

while materials_for_crafting and magic_level:
    # if "doll" in presents_crafted and "wooden_train" in presents_crafted or \
    #         "teddy_bear" in presents_crafted and "bicycle" in presents_crafted:
    #     break
    if magic_level[0] == 0 and materials_for_crafting[-1] == 0:
        magic_level.popleft()
        materials_for_crafting.pop()
        continue
    if magic_level[0] == 0:
        magic_level.popleft()
        continue
    if materials_for_crafting[-1] == 0:
        materials_for_crafting.pop()
        continue

    materials = materials_for_crafting[-1]
    magic = magic_level[0]
    result = materials * magic
    if result in present_values.values():
        for key, val in present_values.items():
            if val == result:
                if key not in presents_crafted:
                    presents_crafted[key] = 0
                presents_crafted[key] += 1
        magic_level.popleft()
        materials_for_crafting.pop()
    elif result < 0:
        materials_magic_combo = materials_for_crafting[-1] + magic_level[0]
        magic_level.popleft()
        materials_for_crafting.pop()
        materials_for_crafting.append(materials_magic_combo)
    elif result > 0:
        magic_level.popleft()
        materials_for_crafting[-1] += 15

if 'Doll' in presents_crafted.keys() and "Wooden train" in presents_crafted.keys() or \
            "Teddy bear" in presents_crafted.keys() and "Bicycle" in presents_crafted.keys():
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

materials_for_crafting = list(reversed(materials_for_crafting))
# magic_level = list(reversed(magic_level))

if len(materials_for_crafting) > 0:
    print(f"Materials left: {', '.join(map(str, materials_for_crafting))}")
if len(magic_level) > 0:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

sort_dict = dict(sorted(presents_crafted.items(), key=lambda item: item[0]))

for key, val in sort_dict.items():
    print(f"{key}: {val}")
