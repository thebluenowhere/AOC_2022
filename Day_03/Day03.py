#!/usr/bin/python3

def get_input(filename):
    with open(filename, 'r') as file:
        contents = file.readlines()
        return contents

def part_one(contents):
    total = 0
    data = []
    data2 = []
    for line in contents:
        comp1, comp2 = line[:int(len(line)/2)], line[int(len(line)/2):]
        for i in comp1:
            if i in comp2:
                data.append(i)
                
            for l in data:
                if ord(l) >= 97 and ord(l) <= 122:
                    data2.append(ord(l) - 96)
                else:
                    data2.append(ord(l) - 38)
            break

    for n in data2:
        total += n
    print(f"Part 1: {total}")    

def part_two(contents):
    # 
    pass

def main(contents, part_one, part_two):
    part_one(contents)
    part_two(contents)

if __name__ == '__main__':
    filename = get_input('input_day03.txt')
    main(filename, part_one, part_two)
