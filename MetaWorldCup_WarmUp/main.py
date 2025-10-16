def solve():
    import sys
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")

    t = int(sys.stdin.readline().strip())

    for case in range(1, t + 1):
        n = int(sys.stdin.readline().strip())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))

        possible = True
        for i in range(n):
            if B[i] < A[i]:
                possible = False
                break
        if not possible:
            print(f"Case #{case}: -1")
            continue

        from collections import defaultdict
        pos = defaultdict(list)
        for i in range(n):
            pos[A[i]].append(i + 1)

        sorted_temps = sorted(set(B), reverse=True)
        ops = []
        for temp in sorted_temps:
            targets = [i + 1 for i in range(n) if B[i] == temp and A[i] != B[i]]
            found = pos[temp][0] if pos[temp] else None
            if not found:
                possible = False
                break

            for idx in targets:
                ops.append((found, idx))
                A[idx - 1] = temp
                pos[temp].append(idx)

        if not possible:
            print(f"Case #{case}: -1")
        else:
            print(f"Case #{case}: {len(ops)}")
            for i, j in ops:
                print(i, j)

solve()
