num =[]
zeros = []
def num_extract():
    for i in range(1,len(x)+1):
        try:
            if isinstance(int(x[-i]), int) is True:
                num.append(x[-i])		
        except:
            break
def zero_extract():
    for i in num[::-1]:
        if i == '0':
            zeros.append(i)
        else:
            break
    return str(int(''.join(num[::-1]))+1)

x = input("enter a word: ")
num_extract()

if len(num)==0:
	print(x+'1')
else:
    sum = zero_extract()
    if len(num) != len(''.join(zeros)+sum):
        print(x[:len(x)-len(num)]+''.join(zeros[:len(zeros)-1])+sum)
    else:
        print(x[:len(x)-len(num)]+''.join(zeros)+sum)
