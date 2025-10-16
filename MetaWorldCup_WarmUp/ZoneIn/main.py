import sys

# Fast input/output
sys.setrecursionlimit(10**6)

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    results = []
    
    for case in range(1, t + 1):
        r = int(data[index]); c = int(data[index + 1]); k = int(data[index + 2])
        index += 3
        grid = data[index:index + r]
        index += r

        # --- core logic ---
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '.':
                    # Check if visible or within range condition
                    visible = True
                    for dx in range(-k, k + 1):
                        for dy in range(-k, k + 1):
                            x, y = i + dx, j + dy
                            if 0 <= x < r and 0 <= y < c:
                                if grid[x][y] == '#':
                                    visible = False
                                    break
                        if not visible:
                            break
                    if visible:
                        count += 1

        results.append(f"Case #{case}: {count}")
    
    # Write to output.txt
    with open("output.txt", "w") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    solve()

