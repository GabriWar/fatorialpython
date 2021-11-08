N = float(input("insira um numero para que o fatorial possa ser calculado: "))
if N == 0:
    print("0!=1")
if N==1:
    print("1!=1")
N2=N
N-=1
while N > 0:
    print(N2,"*",N, "=", (N2*N))
    N2=(N2*N)
    N -= 1
