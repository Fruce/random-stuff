def AND(a,b):
    return 1 if a == 1 and b == 1 else 0
def NOT(a):
    return 0 if a == 1 else 1
def NAND(a,b):
    return NOT(AND(a,b))
def OR(a,b):
    return NAND(NOT(a),NOT(b))
def XOR(a,b):
    return (AND(OR(a,b),NAND(a,b)))
def NOR(a,b):
    return(NOT(OR(a,b)))
def XNOR(a,b):
    return(NOT(XOR(a,b)))

def Call(f):
    print('\nTRUTH TABLE: \n')
    for i in range(4):
        print(' -- '.join(list(str(bin(i)[2:].zfill(2))))+'  = ',eval(f'{f}({bin(i)[2:].zfill(2)[0]},{bin(i)[2:].zfill(2)[1]})'))
Call(input('Show Truth Table for: '))
