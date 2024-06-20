N = int(input())
fruits = list(map(int, input().split()))


fruitCount = {}
for i in range(1, 10):
    fruitCount[i] = 0

def fruitType():
    cnt = 0
    for fruit in fruitCount.keys():
        if fruitCount[fruit] > 0:
            cnt += 1
    return cnt

maxLength = 0

i, j = 0, 0
while i <= N:
    if fruitType() > 2:
        fruitCount[fruits[j]] -= 1
        j += 1
    else:
        maxLength = max(maxLength, i - j)
        if i == N: break
        fruitCount[fruits[i]] += 1
        i += 1

print(maxLength)
