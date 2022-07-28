def sorter(str):
    for j in range(len(str)-1):
        for i in range(len(str)-1):
            if ord(str[i]) > ord(str[i+1]):
                str[i],str[i+1] = str[i+1],str[i]
    return ''.join(str).strip()
    
str = input('Enter a string: ')
print(sorter(list(str)))
