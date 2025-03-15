n = int(input())
queue = []

for _ in range(n):
    command = input()

    if command[0] == '+':
        queue.append(command[1])

    elif command == '-':
        if queue:
            queue.pop(0)
        else:
            break
    
    print(queue)
