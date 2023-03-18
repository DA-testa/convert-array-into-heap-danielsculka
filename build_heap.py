# python3
# Dāniels Čulka 221RDB304

def swap(i, data, swaps):
    minIx = i
    leftIx = 2 * i + 1
    rightIx = 2 * i + 2

    if leftIx < len(data) and data[minIx] > data[leftIx]:
        minIx = leftIx

    if rightIx < len(data) and  data[minIx] > data[rightIx]:
        minIx = rightIx

    if i != minIx:
        swaps.append((i, minIx))

        el = data[i]
        data[i] = data[minIx]
        data[minIx] = el

        swap(minIx, data, swaps)

def build_heap(data):
    swaps = []

    for i in range(len(data), -1, -1):
        swap(i, data, swaps)

    return swaps


def main():
    inputType = input()

    if 'I' in inputType:
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F' in inputType:
        fileName = input()

        if 'a' in fileName:
            return
        
        with open("./tests/%s" % (fileName), "r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split(" ")))
    else:
        return

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
