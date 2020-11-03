import matplotlib.pyplot as plt
def J(x,y,c0,c1): #оценка функции
    j=0
    m=len(x)    
    for i in range(0,m):
        j+=((c0+c1*x[i])-y[i])**2
    j/=(2*m)
    return j

def Grad0(x,y,c0,c1):
    grad0=0
    m=len(x)
    for i in range (0,m):
       grad0+=(c0+c1*x[i])-y[i]
    grad0/=m
    return grad0
def Grad1(x,y,c0,c1):
    grad1=0
    m=len(x)
    for i in range (0,m):
       grad1+=((c0+c1*x[i])-y[i])*x[i]
    grad1/=m
    return grad1

c0=0
c1=0
x=[]
y=[]
temp=0
al=0.01
eps=0.000000001
time=[]
JNEW1=[]
f = open('data1.txt', 'r')
for line in f:
    temp = line.split(' ')
    x.append(float(temp[0]))
    y.append(float(temp[1]))
m=len(x)
Jnew=J(x,y,c0,c1)
JOld=Jnew+1
while(JOld-Jnew)>eps:
    time+=1
    JOld=Jnew
    temp=Grad1(x,y,c0,c1)
    c0-=al*Grad0(x,y,c0,c1)
    c1-=al*temp
    JNEW1.append(Jnew)
    Jnew=J(x,y,c0,c1)
    
minX=min(x)
maxX=max(x)

minY=c0+c1*minX
maxY=c0+c1*maxX
plt.plot(x,y,'ro')
plt.plot([minX,maxX],[minY,maxY])
plt.show()
plt.plot(JNEW1)
plt.show
