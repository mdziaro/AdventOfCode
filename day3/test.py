def process_engine_schematic(engine_schematic):
    rows, cols = len(engine_schematic), len(engine_schematic[0])
    output = set()

    def is_valid_coordinate(i, j):
        return 0 <= i < rows and 0 <= j < cols

    def has_digit_neighbor(i, j):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni, nj = i + di, j + dj
                if is_valid_coordinate(ni, nj) and engine_schematic[ni][nj].isdigit():
                    return True
        return False

    for i in range(rows):
        for j in range(cols):
            if engine_schematic[i][j] != '.' and has_digit_neighbor(i, j):
                start, end = j, j
                while end + 1 < cols and engine_schematic[i][end + 1].isdigit():
                    end += 1
                while start - 1 >= 0 and engine_schematic[i][start - 1].isdigit():
                    start -= 1
                number = engine_schematic[i][start:end + 1]
                if number.isdigit():
                    output.add(int(number))

    return sum(output)

# Example usage:
engine_schematic_example = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

result = process_engine_schematic(engine_schematic_example)
print(result)
