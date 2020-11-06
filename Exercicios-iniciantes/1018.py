N=int(input())
if 0<N<1000000:
    print(N)
    N100=N//100
    Ni1=N%100
    print(N100,"nota(s) de R$ 100,00")
    N50=Ni1//50
    Ni2=Ni1%50
    print(N50,"nota(s) de R$ 50,00")
    N20=Ni2//20
    Ni3=Ni2%20
    print(N20,"nota(s) de R$ 20,00")
    N10=Ni3//10
    Ni4=Ni3%10
    print(N10,"nota(s) de R$ 10,00")
    N05=Ni4//5
    Ni5=Ni4%5
    print(N05,"nota(s) de R$ 5,00")
    N02=Ni5//2
    Ni6=Ni5%2
    print(N02,"nota(s) de R$ 2,00")
    N01=Ni6//1
    N07=Ni6%1
    print(N01,"nota(s) de R$ 1,00")
