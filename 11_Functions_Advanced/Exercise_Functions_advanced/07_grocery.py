def grocery_store(**kwargs):
    recepy = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    result = []
    for k, v in recepy.items():
        result.append(f"{k}: {v}")
    return "\n".join(result)


'''
test print
'''
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))