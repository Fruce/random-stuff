x = input("enter a word: ")
num =[]
zeros = []
for i in range(1,len(x)+1):
	try:
		if type(int(x[-i])) == type(1):
			num.append(x[-i])		
	except:		
		break
if len(num)==0:
	print(x+'1')
else:
    for i in num[::-1]:
        try:
            if i == '0':
                zeros.append(i)
        except:
            break
    sum = int(''.join(num[::-1]))+1
    if len(num) != len(''.join(zeros)+str(sum)):
        print(x[:len(x)-len(num)]+''.join(zeros[:len(zeros)-1])+str(sum))
    else:
        print(x[:len(x)-len(num)]+''.join(zeros)+str(sum))
