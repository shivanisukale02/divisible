def div5(x):
    if x%5==0:
        return True
    else:
        return False

def div7(x):
    if x%7==0:
        return True
    else:
        return False

def div9(x):
    if x%9==0:
        return True
    else:
        return False

def div11(x):
    if x%11==0:
        return True
    else:
        return False

if __name__=="__main__":
    n1=int(input("Enter number"))
    print(div5(n1))
    print(div7(n1))
    print(div9(n1))
    print(div11(n1))