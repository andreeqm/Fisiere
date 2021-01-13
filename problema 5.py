with open ("numere.txt","r") as f:
    a=f.read()
x=int(a)*1
y=int(a)*2
n1="1*"+str(a)+"="+str(x)
n2="2*"+str(a)+"="+str(y)
with open ("tm.txt","w") as f:
    f.write(str(n1))
    f.write("/n")
    f.write(str(n2))