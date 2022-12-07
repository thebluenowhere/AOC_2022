#!/usr/bin/env python3

def get_input(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        return contents

def main(contents):
    data = []
    score = 0
    loss = 0
    draw = 3
    win = 6
    R = 1
    P = 2
    S = 3
    A = R
    B = P
    C = S
    X = A
    Y = B
    Z = C
    print(Z)
    shape = [R, P, S]

    for line in contents.split('\n'):
        data.append(line)
        for group in data:
            if group[0] == R and group[1] == S:
                score += (win + R)

if __name__ == "__main__":
    contents = get_input('input.txt')
    main(contents)
