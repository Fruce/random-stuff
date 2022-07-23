x = input("enter a word: ")
num =[]
for i in range(1,len(x)+1):
	try:
		if type(int(x[-i])) == type(1):
			num.append(x[-i])		
	except:		
		break
if len(num)==0:
	print(x+'1')
else:
    print(x[:len(x)-len(num)]+str(int(''.join(num[::-1]))+1))
