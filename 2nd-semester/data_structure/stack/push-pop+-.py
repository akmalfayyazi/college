n = int(input())
stack = []

for _ in range(n):
    command = input()

    if command[0] == "+":
        stack.append(command[1])

    elif command[0] == '-':
        if stack:
            stack.pop()
        else:
            break
    
    print(stack)
