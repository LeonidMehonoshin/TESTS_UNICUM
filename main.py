import random
class Islands_tools:
    @staticmethod
    def get_input_nums(text, min_num, max_num):
        while True:
            try:
                num = int(input(text))
                if min_num <= num <= max_num:
                    return num
            except ValueError:
                pass

    @staticmethod
    def island_gen(max_perimeter_land, num, max_island_size):
        size_land = {
            'w': random.randint(10, max_perimeter_land//2),
            'h': random.randint(10, max_perimeter_land//2)
        }
        ascii = [['~' for _ in range(max_island_size['w'])] for _ in range(max_island_size['h'])]
        for size_land_h_enum in range(size_land['h']):
            size_line = random.randint(size_land['w'] // 2, size_land['w'] - 2)
            pos_line = random.randint(1, size_land['w'] - size_line - 1)
            for size_line_enum in range(size_line):
                if 0 < size_land_h_enum < size_land['h'] - 1:
                    ascii[size_land_h_enum][pos_line + size_line_enum] = 'H'
        return {
            'size_land': size_land,
            'ascii': ascii,
            'num': num
        }

    @staticmethod
    def islands_sort(islands, max_island_size):
        islands_groups = [[], [], []]
        for island in islands:
            if island['num'] < 3:
                islands_groups[0].append(island['ascii'])
            elif 3 <= island['num'] < 6:
                islands_groups[1].append(island['ascii'])
            else:
                islands_groups[2].append(island['ascii'])

        for islands_group in islands_groups:
            for land_height_enum in range(max_island_size['h']):
                line = []
                for island_ascii in islands_group:
                    line += island_ascii[land_height_enum]
                print(*line)

islands_tools = Islands_tools()
max_perimeter_land = islands_tools.get_input_nums('max perimeter (20-min, 45-max): ', 20, 45)
max_islands_qty = islands_tools.get_input_nums('max number of islands (1-min, 9-max): ', 1, 9)
islands_qty = random.randint(1, max_islands_qty)
islands = []

islands = [islands_tools.island_gen(max_perimeter_land, num, {'w':25, 'h':25}) for num in range(islands_qty)]

islands_tools.islands_sort(islands, {'w':25, 'h':25})
