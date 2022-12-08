#!/usr/bin/python3

def get_input(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        return contents.split('\n')

def part_one(contents):
    total = 0

    for line in contents:
        if line == 'A X':
            total += 3 + 1
        elif line == 'A Y':
            total += 6 + 2
        elif line == 'A Z':
            total += 0 + 3
        elif line == 'B X':
            total += 0 + 1
        elif line == 'B Y':
            total += 3 + 2
        elif line == 'B Z':
            total += 6 + 3
        elif line == 'C X':
            total += 6 + 1
        elif line == 'C Y':
            total += 0 + 2
        elif line == 'C Z':
            total += 3 + 3

    print(f"Part 1: {total}")

def part_two(contents):
    total = 0

    for line in contents:
        if line == 'A X':
            total += 0 + 3
        elif line == 'A Y':
            total += 3 + 1
        elif line == 'A Z':
            total += 6 + 2
        elif line == 'B X':
            total += 0 + 1
        elif line == 'B Y':
            total += 3 + 2
        elif line == 'B Z':
            total += 6 + 3
        elif line == 'C X':
            total += 0 + 2
        elif line == 'C Y':
            total += 3 + 3
        elif line == 'C Z':
            total += 6 + 1
    
    print(f"Part 2: {total}")


def main(contents, part_one, part_two):
    part_one(contents)
    part_two(contents)

if __name__ == '__main__':
    filename = get_input('input_day02.txt')
    main(filename, part_one, part_two)
