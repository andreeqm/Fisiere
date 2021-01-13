#Afişaţi tabla înmulţirii cu numărul n. Exemplu: pentru n=5, se va afişa pe verticală 1x5=5  2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45 10x5=50. 
#Din fişierul « numar.txt » se citeşte un număr, în fişierul « inmultire.txt » - se înscrie tabla înmulţirii cu acest număr.

with open("numar.txt","r") as f:
    a=f.read()
x=int(a)*1
y=int(a)*2
b=int(a)*3
c=int(a)*4
d=int(a)*5
e=int(a)*6
f=int(a)*7
g=int(a)*8
h=int(a)*9
i=int(a)*10
n1="1*"+str(a)+"="+str(x)
n2="2*"+str(a)+"="+str(y)
n3="3*"+str(a)+"="+str(b)
n4="4*"+str(a)+"="+str(c)
n5="5*"+str(a)+"="+str(d)
n6="6*"+str(a)+"="+str(e)
n7="7*"+str(a)+"="+str(f)
n8="8*"+str(a)+"="+str(g)
n9="9*"+str(a)+"="+str(h)
n10="10*"+str(a)+"="+str(i)
with open ("tm.txt","w") as f:
    f.write(str(n1))
    f.write("\n")
    f.write(str(n2))
    f.write("\n")
    f.write(str(n3))
    f.write("\n")
    f.write(str(n4))
    f.write("\n")
    f.write(str(n5))
    f.write("\n")
    f.write(str(n6))
    f.write("\n")
    f.write(str(n7))
    f.write("\n")
    f.write(str(n8))
    f.write("\n")
    f.write(str(n9))
    f.write("\n")
    f.write(str(n10))

