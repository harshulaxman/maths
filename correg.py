import matplotlib.pyplot as plt
x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]
N=len(x)
Sx=0
Sy=0
Sxy=0
Sx2=0
Sy2=0
for i in range (0,N):
    Sx=Sx+x[i]
    Sy=Sy+y[i]
    Sxy=Sxy+x[i]*y[i]
    Sx2=Sx2+x[i]**2
    Sy2=Sy2+y[i]**2
r=(N*Sxy-Sx*Sy)/(math.sqrt(N*Sx2-Sx**2) *math.sqrt(N*Sy2-Sy**2))
print("The Correlation coefficient is %0.3f"%r)
byx=(N*Sxy-Sx*Sy)/(N*Sx2-Sx**2)
xmean=Sx/N
ymean=Sy/N
print("THe Regression line Y on X is ::: y = %0.3f + %0.3f (x-%0.3f) "%(ymean, byx, xmean))
plt.scatter(x,y)
def Reg(x):
    return ymean + byx*(x-xmean)
x=np.linspace(0,80,51)
y1=Reg(x)
plt.plot(x,y1, 'r')
plt.xlabel('x-data')
plt.ylabel('y-data')
plt.legend (['Regression Line', 'Data points'])