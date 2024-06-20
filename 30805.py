N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

def findLargestCommonElement(A, B):
    possNum = set(A) & set(B)
    if not possNum: return 0, 0, 0
    m = max(possNum)
    return m, A.index(m), B.index(m)

ans = []

while A or B:
    m, a, b = findLargestCommonElement(A, B)
    if not m: break
    ans.append(m)
    A = A[a + 1:]
    B = B[b+1:]

print(len(ans))
print(*ans, sep=" ")