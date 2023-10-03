from collections import deque as dq
worker_bees = dq([int(x) for x in input().split()])
nectar = dq([int(x) for x in input().split()])
symbols = dq(input().split())

total_honey = 0


def rbns(bee_dq, nectar_dq, symbol_dq):
    return bee_dq.popleft(), nectar_dq.pop(), symbol_dq.popleft()


def check_nectar(bee_val: int, nectar_val: int):
    if nectar_val >= bee_val:
        return True
    return False


def calculate_collected(bee_val: int, symbol: str, nectar_val: int):
    if symbol == '/' and nectar_val == 0:
        return "skip"
    else:
        res = abs(eval(str(bee_val) + symbol + str(nectar_val)))
        return res


while worker_bees and nectar:
    if check_nectar(worker_bees[0], nectar[-1]):
        result = calculate_collected(worker_bees[0], symbols[0], nectar[-1])
        if result != 'skip':
            total_honey += result
            rbns(worker_bees, nectar, symbols)
        else:
            rbns(worker_bees, nectar, symbols)
    else:
        nectar.pop()
        continue

print(f"Total honey made: {total_honey}")
print(f"Bees left: {', '.join(map(str, worker_bees))}") if worker_bees else None
print(f"Nectar left: {', '.join(map(str, nectar))}") if nectar else None
