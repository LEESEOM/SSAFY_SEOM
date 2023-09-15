# swea 문제풀이 1234. 비밀번호

Alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in Alphabet:
    word.replace(i, '*')
print(len(word))