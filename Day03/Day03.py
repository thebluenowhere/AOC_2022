#!/usr/bin/python3

def get_input(filename):
    with open(filename, 'r') as file:
        contents = file.readlines()
        return contents

def part_one(contents):
    priority = 0
    for line in contents:
        comp1, comp2 = line[:int(len(line)/2)], line[int(len(line)/2):]
        for i in comp1:
            if i in comp2:
                n =  ord(i) - 96 if i.islower() else ord(i) - 38
                priority += n
                break

    print(f"Part 1: {priority}")    

def part_two(contents):
    badge = 0
    group = [contents[i:i + 3] for i in range(0, len(contents), 3)]
    for trio in group:
        for i in trio[0]:
            if i in trio[1]:
                if i in trio[2]:
                    n = ord(i) - 96 if i.islower() else ord(i) - 38
                    badge += n
                    break
    
    print(f"Part 2: {badge}")

def main(contents, part_one, part_two):
    part_one(contents)
    part_two(contents)

if __name__ == '__main__':
    filename = get_input('input.txt')
    main(filename, part_one, part_two)