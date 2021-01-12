#Ion şi Vasile joacă următorul joc: Ion spune un număr iar Vasile trebuie să găsească cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion. 
#Exemplu : Ion spune 10, Vasile spune 8 9 10 11 12. Ajutaţi-l pe Vasile să găsească răspunsul mai repede. Din fişierul « input.txt » se citeşte un număr, în fişierul « output.txt » - se înscrie consecutivitatea numerelor.

with open ("input.txt","r") as f:
    a=f.readline()
    n=int(a)-2
    d=int(a)-1
    r=int(a)+1
    e=int(a)+2
with open ("output.txt","w") as f:
    f.write(str(n))
    f.write("  ")
    f.write(str(d))
    f.write("  ")
    f.write(str(a))
    f.write("  ")
    f.write(str(r))
    f.write("  ")
    f.write(str(e)) 