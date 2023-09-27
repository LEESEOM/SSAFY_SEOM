switch_num = int(input())
switch = list(map(int, input().split()))
student_num = int(input())
info = []
for i in range(student_num):
    sex, num = map(int, input().split())
    info.append((sex,num))

# 스위치 변경
for j in range(len(info)):
    if info[j][0] == 1: # 남학생이라면
        for k in range(0, len(switch)):
            if (k+1)%info[j][1] == 0:
                if switch[k] == 1:
                    switch[k] = 0
                elif switch[k] == 0:
                    switch[k] = 1
    if len(switch) == 1:
        if switch[0] == 1:
            switch[0] = 0
        else:
            switch[0] = 1


    elif info[j][0] == 2: # 여학생이라면
        now = info[j][1] -1
        lst = [now]
        m = 1
        while True:
            if 0<=now-m and now+m<switch_num:
                if switch[now-m] == switch[now+m]:
                   lst.append(now-m)
                   lst.append(now+m)
                   m += 1
                else:
                    break
            else:
                break
        for n in range(len(lst)):
            if switch[lst[n]] == 1:
                switch[lst[n]] = 0
            elif switch[lst[n]] == 0:
                switch[lst[n]] = 1

for o in range(0, len(switch), 20):
    print(*switch[o:o+20])
