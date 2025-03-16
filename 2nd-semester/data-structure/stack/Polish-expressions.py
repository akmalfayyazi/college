n = int(input())

for _ in range(n):
    command = input()
    stack = []
    result = []

    for i in command:
        if i == '(':
            stack.append(i)
        elif i.isalpha():
            result.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            stack.append(i)

    print(''.join(result))
