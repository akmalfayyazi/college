n = int(input())
stack = []
sort_stack = []
temp = []

for _ in range(n):
    command = input().split()

    if command[0] == 'PUSH':
        val = int(command[1])
        stack.append(val)
        if not sort_stack or val <= sort_stack[-1]:
            sort_stack.append(val)
        else:
            while sort_stack and sort_stack[-1] < val:
                temp.append(sort_stack.pop())
            sort_stack.append(val)
            while temp:
                sort_stack.append(temp.pop())
    
    elif command[0] == 'MIN':
        if sort_stack[-1] in stack:
            print(sort_stack[-1])
        else:
            while sort_stack[-1] not in stack:
                sort_stack.pop()
            print(sort_stack[-1])
    
    elif command[0] == 'POP':
        stack.pop()




