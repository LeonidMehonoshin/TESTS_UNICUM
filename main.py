import time

def towers_printer(towers):
    for i in range(len(towers)):
        print(f'{i+1} - ', end='')
        for disk in towers[i]:
            print(colors[disk-1], end=' ')
        print()
    print()

def checker_true(towers, true_tower):
    return len(towers[true_tower]) == 5 and towers[true_tower] == [1, 2, 3, 4, 5]

def checker_move(a, b):
    if len(a) == 0: return False
    if len(b) == 0: return True
    return a[0] < b[0]

def prediction(towers):
    predictions = []
    for a in range(3):
        for b in range(3):
            if a != b and checker_move(towers[a], towers[b]):
                new = [tower.copy() for tower in towers]
                disk = new[a].pop(0)
                new[b].insert(0, disk)
                predictions.append(new)
    return predictions

colors = [
    "\033[33m1\033[0m", "\033[31m2\033[0m", "\033[32m3\033[0m",
    "\033[36m4\033[0m", "\033[35m5\033[0m"
]

while True:
    towers = []
    print('\nВводите любые числа (от 1 до 5) через пробел(пример: 1 2 3 4 5) [верх|низ]\n')
    try:
        towers.append([int(disk) for disk in input(f'Диски на башне 1 - ').split()])
        towers.append([int(disk) for disk in input(f'Диски на башне 2 - ').split()])
        towers.append([int(disk) for disk in input(f'Диски на башне 3 - ').split()])
        true_tower = int(input("На какую башню собрать? (1 / 2 / 3): ")) - 1
        if (sum(map(sum, towers)) == 15 and
            len(towers[0]) + len(towers[1]) + len(towers[2]) == 5
            and true_tower in (0, 1, 2)): break
    except ValueError: pass

inbox = [(towers, [])]
checked = set([str(towers)])

while inbox:
    current_towers, result = inbox.pop(0)
    if checker_true(current_towers, true_tower):
        break
    for next_towers in prediction(current_towers):
        if str(next_towers) not in checked:
            checked.add(str(next_towers))
            inbox.append((next_towers, result + [next_towers]))

print(); towers_printer(towers)
for step in result: time.sleep(1); towers_printer(step)
