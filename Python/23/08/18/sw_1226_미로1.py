# sw_1226_미로1

for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, input().split())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
