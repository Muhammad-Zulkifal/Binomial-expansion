def binomial_coefficient(n, k):
    """
    Compute the binomial coefficient C(n, k)
    """
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

def binomial_expansion(a, b, n):
    """
    Compute the binomial expansion of (a + b)^n
    """
    expansion = []
    for k in range(n + 1):
        coefficient = binomial_coefficient(n, k)
        term = coefficient * (a ** (n - k)) * (b ** k)
        expansion.append(term)
    return expansion

if __name__ == "__main__":
    a = int(input("Enter the value of x_coefficient: "))
    b = int(input("Enter the value of constant: "))
    n = int(input("Enter the value of power: "))

    expansion = binomial_expansion(a, b, n)
    if b>0:
        print(f"The binomial expansion of ({a}x+{b})^{n} is:")
    else:
        print(f"The binomial expansion of ({a}x{b})^{n} is: ")
print(expansion)
expression=""
for i in range(n+1):
    term=int(expansion[i])
    if term==1:
        if n==i:
            term=str(term)
        else:
            term="x^"+str(n-i)
    else:
        if n!=i:
            term=str(term)+"x^"+str(n-i)
    if i==0:
        expression=expression+term
    else:
        if int(expansion[i])<0:
            expression=expression+term
        else:
            expression=expression+"+"+term
print(expression)
