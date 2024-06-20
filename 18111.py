N, M, B = map(int, input().split())

blocks = [list(map(int, input().split())) for _ in range(N)]

maxHeight = max(max(block) for block in blocks)

def getTime(height):
    time = 0
    for block in blocks:
        for b in block:
            if b > height:
                time += (b - height) * 2
            else:
                time += (height - b)
    return time

def ifPossible(height):
    inventory = B
    for block in blocks:
        for b in block:
            inventory -= (height - b)
    return inventory >= 0

def getMinTime():
    minTime = float('inf')
    for height in range(maxHeight, -1, -1):
        if ifPossible(height):
            time = getTime(height)
            if time < minTime:
                minTime = time
                minHeight = height
    print(minTime, minHeight)

getMinTime()