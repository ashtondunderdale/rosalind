file = open("intro/p5.txt", "r")
lines = file.readlines()

for idx, x in enumerate(lines):
    if idx % 2 != 0:
        print(x)