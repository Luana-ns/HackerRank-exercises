if __name__ == '__main__':
    number = int(input())
    list = []
    for x in map(int, input().split()):
        list.append(x)
    y = max(list)
    while max(list) == y:
        list.remove(max(list))
    print(max(list))
