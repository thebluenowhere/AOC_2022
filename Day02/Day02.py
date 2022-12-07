#!/usr/bin/env python3

def get_input(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        return contents

def main(contents):
    shape = {'R': 1, 'P': 2, 'S': 3 }
    opponent = {'R': 'A', 'P': 'B', 'S': 'C'}
    move = {'R': 'X', 'P': 'Y', 'S': 'Z'}
    lose = 0
    draw = 3
    win = 6

    for group in contents.split():
        print(group)

if __name__ == "__main__":
    filename = get_input('input.txt')
    main(contents)
