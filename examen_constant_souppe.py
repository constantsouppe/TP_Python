#-*-coding:Utf-8 -*

#Ex1


class IPv4:


    def __init__(self,str_ipv4,str_mask,str_ipv4_min,str_ipv4_max):
        self.str_ipv4_max = str_ipv4_max
        self.str_ipv4_min= str_ipv4_min
        self.str_ipv4 = str_ipv4
        self.str_mask = str_mask


    def saisie_ipv4(self):
        IP=input("entrez une adresse ip sous la forme X3.x2.x1.x0:\n")
        x= IP.split(".")
        if int(x[0])<0 or int(x[0])>255 or int(x[1])<0 or int(x[1])>255 or int(x[2])<0 or int(x[2])>255 or int(x[3])<0 or int(x[3])>255:
            print("IP invalide")
        else:
            self.str_ipv4= IP
            print (self.str_ipv4)

    def __init__(self,str_mask):
        self.str_mask = str_mask

    def saisie_masque_ipv4(self):
        mask = input("entrez un masque ip sous la forme m3.m2.m1.m0:\n")
        m = mask.split(".")
        if int(m[0]) < 0 or int(m[0]) > 255 or int(m[1]) < 0 or int(m[1]) > 255 or int(m[2]) < 0 or int(
                m[2]) > 255 or int(m[3]) < 0 or int(m[3]) > 255:
            print("masque invalide")
        else:
            self.str_mask = mask
            print(self.str_mask)

    def calcule_ip_min(self):
        IP=self.str_ipv4
        mask=self.str_mask
        x=IP.split(".")
        m=mask.split(".")
        self.str_ipv4_min=str()
        for i in range (0,3):
            self.str_ipv4_min =self.str_ipv4_min +str(et_logique_bit_a_bit(int(x[i]),int(m[i])))+"."
        self.str_ipv4_min = self.str_ipv4_min + str(et_logique_bit_a_bit(int(x[3]), int(m[3]))+1)
    def get_ipv4_min(self):
        IPv4.calcule_ip_min()
        print(self.str_ipv4_min)

    def calcule_ip_max(self):
        IP = self.str_ipv4
        mask = self.str_mask
        x = IP.split(".")
        m = mask.split(".")
        self.str_ipv4_max = str()
        for i in range(0, 3):
            self.str_ipv4_max = self.str_ipv4_max +str(ou_logique_bit_a_bit(int(x[i]), complement_bit_a_bit(int(m[i]))))+"."
        self.str_ipv4_max = self.str_ipv4_max + str(ou_logique_bit_a_bit(int(x[3]), complement_bit_a_bit(int(m[3])))-1)

    def get_ipv4_max(self):
        IPv4.calcule_ip_max()
        print(self.str_ipv4_max)

    def saisie_cidr(self):
        cdir=input("entrez votre cidr:\n")

IPv4=IPv4("192.168.15.2")

#IPv4.saisie_ipv4()

#IPv4.saisie_masque_ipv4()

def complement_bit_a_bit(x):
    x=~x & 255
    return x
    #print(x)

def et_logique_bit_a_bit(x,y):
    x = x & y
    return x
    #print(resultat)

def ou_logique_bit_a_bit(x,y):
    x = x|y
    return x
    #print(resultat)

IPv4.saisie_ipv4()

IPv4.saisie_masque_ipv4()

IPv4.get_ipv4_min()

IPv4.get_ipv4_max()




