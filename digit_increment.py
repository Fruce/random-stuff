num =[]
zeros = []

def num_extract(x):
    for i in range(1,len(x)+1):
        try:
            if type(int(x[-i])) == type(1):
                num.append(x[-i])		
        except:
            break

def zero_extract(num):
    for i in num[::-1]:
        if i == '0':
            zeros.append(i)
        else:
            break
    print(zeros)
    return str(int(''.join(num[::-1]))+1)

#driver code
x = input("enter a word: ")
num_extract(x)


if len(num)==0:
	print(x+'1')
else:
    sum = zero_extract(num)
    if len(num) != len(''.join(zeros)+sum):
        print(x[:len(x)-len(num)]+''.join(zeros[:len(zeros)-1])+sum)
    else:
        print(x[:len(x)-len(num)]+''.join(zeros)+sum)
