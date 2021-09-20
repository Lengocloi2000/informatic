with open("kaka.txt", "r") as file:
    for line in file:
        print(' '.join(line.split()))