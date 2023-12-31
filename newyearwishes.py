#simple python program to print new year wishes
alphabets="abcdefghijklmnopqrstuvwxyz"
b="ibqqz"
c="ofx"
d="zfbs"
k=1
q=[]
r=[]
s=[]
for i in range(len(b)):
  a = alphabets[alphabets.index(b[i])+(k*(-1))]
  q.append(a)
x=''.join(q)
x=x.capitalize()
for j in range(len(c)):
  a1= alphabets[alphabets.index(c[j])+(k*(-1))]
  r.append(a1)
y=''.join(r) 
y=y.capitalize() 
for m in range(len(d)):
    a2 =alphabets[alphabets.index(d[m])+(k*(-1))]
    s.append(a2)
z=''.join(s)
z=z.capitalize()
p = x + " " + y + " " + z
import math
u=math.pow(10,3)
v=math.log(100,10)
w=math.sqrt(625)
n=math.sin(90)
o=str(int((u*v)+w-n))
print(p +" "+ o )
