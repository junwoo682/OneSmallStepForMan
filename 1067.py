from math import exp, pi, e
N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

def fft(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        odd_arr = fft(arr[1::2])
        even_arr = fft(arr[::2])
        w = e ** (2j * pi / n)
        return [even_arr[i] + w**i * odd_arr[i] for i in range(n//2)] + [even_arr[i] - w**i * odd_arr[i] for i in range(n//2)]
    
def minimum_powerof_two(n):
    i = 1
    while i < n:
        i *= 2
    return i

def padding(arr):
    n = len(arr)
    m = minimum_powerof_two(n)
    return arr + [0] * (m - n)

def mul(arr1, arr2):
    return [arr1[i] * arr2[i] for i in range(len(arr1))]

def ifft(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        odd_arr = ifft(arr[1::2])
        even_arr = ifft(arr[::2])
        w = e ** (-2j * pi / n)
        return [even_arr[i] + w**i * odd_arr[i] for i in range(n//2)] + [even_arr[i] - w**i * odd_arr[i] for i in range(n//2)]
    


Y.reverse()
X = padding(X * 2)
Y = padding(Y + [0] * N)
# print(fft(X))
# print(fft(Y))
ans = 0
for i in ifft(mul(fft(X), fft(Y))):
    ans = max(ans, i.real)
print(f"{ans / minimum_powerof_two(N * 2):.0f}")