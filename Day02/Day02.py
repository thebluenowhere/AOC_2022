#!usr/bin/python3

def main():
    score = 0
    f = open('input.txt', 'r')
    for line in f:
        rounds = line.strip()

        if rounds == "A X":
            score += 3 + 1
        elif rounds == "A Y":
            score += 6 + 2
        elif rounds == "A Z":
            score += 0 + 3
        elif rounds == "B X":
            score += 0 + 1
        elif rounds == "B Y":
            score += 3 + 2
        elif rounds == "B Z":
            score += 6 + 3
        elif rounds == "C X":
            score += 6 + 1
        elif rounds == "C Y":
            score += 0 + 2
        elif rounds == "C Z":
            score += 3 + 3

    print(f"Part 1: {score}")

if __name__ == "__main__":
    main()
