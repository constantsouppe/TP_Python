#-*-coding:Utf-8 -*
import.split
# f= open('mon fichier.txt','r')
# l=f.readlines()
# c=0
# for i in range(len(l))
#     if((any(chr.isdigit() for chr in l[i]))==true):
#         c+=1

#print ("il y  a",c,"lignes contenant des caractères numériques")

#autre solution + conventionnelle

# def compteur_num(nom_fichier):
#     num=0
#     fichier= open(nom_fichier, 'r')
#     while 1:
#         line= fichier.readline()
#         if line=="":
#             break
#         for char in line:
#             if char.isnumeric():
#                 num+=1
#     print(num)
#     fichier.close()

f= open('Mon_Fichier.txt','r')
lignes = f.readlines()
cpt_digit = 0
for ligne_courante in lignes:
    for mot in ligne_courante:
        if mot.isdigit():
            cpt_digit +=1
            break
print ("le nombr de lignes contenant des nomlbres est:", cpt_digit)

#comtpage de mots

f=open('Mon_Fichier.txt','r')
lignes = f.readlines()
n = 0
while 1:
    if lignes=="":
        break
    li= list.split(lignes)
    n=n+len(li)
fs.close()
print("ce fichier contient",n,"mots")

#recopiage avec maj en début de phrase

fs=open('Mon_Fichier.txt','r')

fd= open('nouveau_fichier','w')
while 1:
    ch= fs.readlines()
    if ch=="":
        break
    if ch[0]>= "A" and ch[0]<="Z":
        pass
    else:
        ch = ch.capitalize()
    fd.write(ch)
fd.close()
fs.close()

# Exo 4

fs=open('Mon_Fichier.txt','r')
fd= open('nouveau_fichier','w')
ch1= fs.readlines()
while 1:
    ch2= fs.readlines()
    if ch=="":
        break
    if ch[0]>= "A" and ch[0]<="Z":
        fd.write(ch1)
        ch1=ch2
    else:
        ch1 = ch1[:-1] + " " +ch2
    fd.write(ch1)
fd.close()
fs.close()

#Exo 5
fs=open('Mon_Fichier.txt','r')
fd= open('nouveau_fichier','w')

while 1:
    ch1 = fs.readlines()
    if ch1=="":
        break
    for i in range (len(ch1))
    fd.write("Diam =",int(ch1(i)),"section=",int(ch1(i))²*3.14,"surf=",4*3.14*int(ch1(i))**2,"Vol=",(4/3)*3.14*int(ch1(i))**3,"\n)
