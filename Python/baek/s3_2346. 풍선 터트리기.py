
N = int(input())
lst = list(map(int, input().split()))


# ans = [1]
# i = 0
# a = lst[0]
# del lst[0]
# while lst:
#     if a > 0:
#         b = len(lst)
#         c = (a+i)%b
#         a = lst[c]
#         ans.append(c) # 여기서 문제 생길듯
#         del lst[c]
# print(ans)



   # 5 1 2 3 4 인데 12341이잖아 그럼 5%4하면 되는거지
   #
   # 22314야 그럼 2314 다음 214에서 3번인데 142잖아 214가 아니라 그럼 그 인덱스 값까지
   #  더해주면 +1해서 2142는 가능
   #  32134야 2134 다음 214에서 3번인데 421임 214가 아니라 근데 2더하면 21421
   #  오키 양수쪽은 가능
   # -3 1234면 432잖아
