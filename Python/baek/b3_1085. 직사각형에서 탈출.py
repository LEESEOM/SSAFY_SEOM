# Bronze III 1085
# 직사각형에서 탈출

x, y, w, h = map(int, input().split())
if x > w - x:
    min_x = w - x
else:
    min_x = x
if y > h - y:
    min_y = h - y
else:
    min_y = y
if min_x > min_y:
    print(min_y)
else:
    print(min_x)