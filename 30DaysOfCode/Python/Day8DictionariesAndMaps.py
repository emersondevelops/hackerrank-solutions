n = int(input())

phone_book = dict()

for i in range(n):
    entry = list(input().split())
    phone_book[entry[0]] = int(entry[1])

try:
    while True:
        query = input()
        if query in phone_book:
            print("{}={}".format(query, phone_book[query]))
        else:
            print("Not found")
except EOFError:
    pass
