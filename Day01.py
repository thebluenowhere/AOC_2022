#!/usr/bin/python3

def get_data(filename):
    with open(filename, 'r') as file:
        contents = file.read()
    return contents

def main(contents):

        groups = contents.split("\n\n")

        totals = []

        for group in groups:
            group = group.strip()
            numbers = group.split("\n")

            # Convert the numbers from strings to integers
            numbers = [int(n) for n in numbers]

            totals.append(sum(numbers))

        print(f"Part 1: {max(totals)}")

        totals.sort(reverse=True)
        print(f"Part 2: {sum(totals[:3])}")

if __name__ == "__main__":
    contents = get_data('input.txt')
    main(contents)
