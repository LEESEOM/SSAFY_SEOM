import matplotlib.pyplot as plt

# 예제 1 : x, y 가 같을 때
plt.plot([1, 2, 3, 4])
# plt.show()

# 이때까지 그렸던 plot 지우기
plt.clf()

# 예제 2 : x, y가 다를 때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x, y)
plt.show()
# x축은 고정해두는 것이 좋음

# 예제 3 : 제목 + 각 축의 설명
plt.plot(x, y)
# 제목 한글은 안됨
plt.title("Test Graph")

# x, y축
plt.ylabel('y label')
plt.xlabel('x label')

plt.show()


# 파일로 저장하기
# show()를 하지 말고 저장해야 함
plt.savefig('filename.png')