a = input()
stack = []
pasangan = {')':'(','}':'{',']':'['}

for i in a:
    if i in '([{':
        stack.append(i)
    elif i in ']})':
        if not stack or stack.pop() != pasangan[i]:
            print('tidak seimbang')
            break
else:
    print('seimbang')    
