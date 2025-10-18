import random

while True:
    try:
        perimeter = int(input("perimeter(20-min, 100-max): "))
        if perimeter > 19 and perimeter < 101: break
    except ValueError: pass
while True:
    try:
        max_islands = int(input("max number of islands(9-mux): "))
        if max_islands < 10 and max_islands > 0: break
    except ValueError: pass

islands = []
islands_qty = random.randint(1, max_islands)
for qty_enum in range(islands_qty):
    island = {
        'width': random.randint(5, perimeter//2),
        'height': random.randint(5, perimeter//2),
        'ascii': []
    }

    for land_height_enum in range(island['height']):
        island['ascii'].append([])
        for land_width_enum in range(island['width']):
            island['ascii'][land_height_enum].append('~')

    for land_height_enum in range(island['height']):
        size_rnd = random.randint(island['width']//2, island['width']-2)
        pos_rnd = random.randint(1, island['width'] - size_rnd-1)
        for island_width_enum in range(island['width']):
            for size_rnd_enum in range(size_rnd):
                if land_height_enum != 0 and land_height_enum < island['height']-1:
                    island['ascii'][land_height_enum].pop(pos_rnd+size_rnd_enum)
                    island['ascii'][land_height_enum].insert(pos_rnd+size_rnd_enum, 'H')
    islands.append(island)
for island in islands:
    for land_height_enum in range(island['height']):
        print(*island['ascii'][land_height_enum])
