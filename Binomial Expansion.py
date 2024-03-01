def fact(x):
    Fact=1
    for i in range(x):
        Fact=Fact*(i+1)
    return Fact

def comb(n,r):
    a=fact(n)
    b=fact(n-r)
    Comb=a/(b*fact(r))
    return int(Comb)

def binomial_expansion(expression,power,step):
    arr=expression.split("+")
    if arr != expression:
        x_value=arr[0]
        constant=arr[1]
        if constant[-1:]=='x' or constant=='x':
            c=x_value
            x_value=constant
            constant=c
        expansion=""
        const=int(constant)
        x_coefficient=(x_value.split("x"))[0]
        if x_coefficient=="":
            x_coefficient=1
        x_coefficient=int(x_coefficient)
        n=power
        for r in range(n+1):
            coefficient=(comb(n,r))
            coefficient=coefficient*(pow(x_coefficient,(n-r)))
            coefficient=coefficient*(pow(const,r))
            x_power="x^"+str(n-r)
            if coefficient==1 and n!=r:
                coefficient=""
            term=str(coefficient)+x_power
            if r!=0:
                term="+"+term
            if (n-r)==0:
                term="+"+str(coefficient)
            if step==1:
                expansion=expansion+term
            else:
                if (n-r)==0:
                    x_power=""
                term=str(coefficient)+x_power
                if r!=n:
                    term="+"+term
                expansion=term+expansion
   
                   
        print(expansion)
        
express=str(input("Enter expression : "))
power=int(input("Enter power : "))
x=int(input("step? Enter 0 for ascending powers and 1 for descending powers : "))
binomial_expansion(express,power,x)
