def rabbits_after_months(n, k):
    if n == 1 or n == 2:
        return

    f1, f2, fn = 1, 1, 0;
    for _ in range(3, n + 1):
        fn = f2 + k * f1
        f1 = f2
        f2 = fn

    return fn;

n, k = 29, 3;
result = rabbits_after_months(n, k)

print(result)