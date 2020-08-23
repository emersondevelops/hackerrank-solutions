if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    counter = n

    while counter > 0:
        print(arr[counter - 1], end=' ')
        counter -= 1
