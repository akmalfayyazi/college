n = int(input())

for _ in range(n):
    sentence = input()
    queue = []
    result = []
    temp = []

    for i in sentence:
        if i == '[':
            queue.append(i)
        elif i == ']':
            while queue and queue[0] != '[':
                temp.append(queue.pop(0))
            while queue and queue[0] == '[':
                queue.pop(0)
            while queue and queue[0] != ']':
                result.append(queue.pop(0))
        else:
            queue.append(i)
    while temp:
        result.append(temp.pop(0))
    while queue:
        result.append(queue.pop(0))

    print(''.join(result))