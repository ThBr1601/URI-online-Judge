linha1= input().split(" ")
x1,y1=linha1
linha2= input().split(" ")
x2,y2=linha2
d = ((float(x1) - float(x2))**2 + (float(y2) - float(y1))**2)**(0.5)
print('{:.4f}'.format(d))
