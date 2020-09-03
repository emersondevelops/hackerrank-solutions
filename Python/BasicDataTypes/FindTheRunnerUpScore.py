if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    items = list(arr)
    items.sort()
    items.reverse()

    for i in range(n):
        if items[i] != items[i+1]:
            print(items[i+1])
            break
