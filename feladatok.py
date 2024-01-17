
from Betegseg import Betegseg

def beolvas():
    fajl=open("alapbetegsegek.txt", "r", encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close()

    lista=[]
    for i in range(0, len(nyers_lista),1):
        sorok=nyers_lista[i]
        sor_tag=sorok.strip().split("@")
        sorszam=sor_tag[0]
        nem=sor_tag[1]
        kor=int(sor_tag[2])
        betegsegek=sor_tag[3]
        betegseg=Betegseg(sorszam, nem, kor, betegsegek)
        lista.append(betegseg)
    return lista
        
def idosebb(lista):
    szamlalo=0
    for i in range(0, len(lista),1):
        if lista[i].kor>50:
            szamlalo+=1
    return szamlalo

"""def demencia(lista):
    szamlalo2=0
    for i in range(0, len(lista),1):
        if lista[i].betegsegek=="demencia":
        szamlalo2+=1
    return szamlalo2"""

def legidosebb(lista):
    li_index=0
    for i in range(0, len(lista),1):
        if lista[li_index].kor>lista[i].kor:
            li_index=i
    return li_index

def atlag_n(lista):
    n_sz=0
    n_gy=0
    for i in range(0, len(lista),1):
        if lista[i].nem=="Nő":
            n_sz+=1
            n_gy+=lista[i].kor
            n_atlag=n_gy/n_sz
    return n_atlag

def atlag_f(lista):
    f_sz=0
    f_gy=0
    for i in range(0, len(lista),1):
        if lista[i].nem=="Férfi":
            f_sz+=1
            f_gy+=lista[i].kor
            f_atlag=f_gy/f_sz
    return f_atlag