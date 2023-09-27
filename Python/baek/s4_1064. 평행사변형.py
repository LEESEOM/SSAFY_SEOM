# s4 1064 평행사변형

ax, ay, bx, by, cx, cy = map(int, input().split())

# 1자로 있으면 컷 (기울기)
if ax == bx == cx or ay == by == cy:
    print(-1)