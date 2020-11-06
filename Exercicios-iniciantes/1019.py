N=int(input())
Nhoras=N//3600
Nh=N%3600
Nminuto=Nh//60
Nm=N%60
Nsegundos=Nm//1
print(str(Nhoras)+':'+str(Nminuto)+':'+str(Nsegundos))
