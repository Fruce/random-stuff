a = input("enter a num: ")
def armstrong(a,l,p):
	if l == 0:
		return 0
	else:
		sum = int(a[-l])**p
		return sum+armstrong(a,l-1,p)
if int(a) == armstrong(a,len(a),len(a)):
	print("armstrong")
else:
	print("not armstrong")
