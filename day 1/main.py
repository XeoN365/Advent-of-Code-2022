with open("input.txt") as f:
    n = 0
    calories = list()
    for line in f.readlines():
        if line == "":
            calories.append(n)
            n=0
        elif int(line) > 0:
            n+= int(line)
    
    print(max(calories))
