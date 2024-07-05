# Open and read the file
with open("algorithmic_heights/binary_search.txt", "r") as file:
    lines = file.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())
a = list(map(int, lines[2].strip().split()))
keys = list(map(int, lines[3].strip().split()))

results = []

def binary_search(k, low, high):
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == k:
            return mid + 1
        elif a[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1

for k in keys:
    result = binary_search(k, 0, n - 1)
    results.append(result)

print(" ".join(map(str, results)))
