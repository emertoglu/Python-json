book={}

book['ersin']={

    'name':'ersin',
    'adress':'erzurum',
    'phone':5320554411

}


book['tom']={

    'name':'tom',
    'adress':'istanbul',
    'phone':5320554410

}
book['duzgi']={'name':'duz','adress':'istanbul', 'phone':5320554436 }

book['ali']={'name':'ali', 'adress':'ist', 'phone':'123'}

import json

"""

j=json.dumps(book)         # burada içeriği bir değişkene atadık
print(j)                   # burada da yazdırdık


with open("/home/aspa/CALISMALAR/PycharmProjects/jSONN/adress.txt","w") as yazz :
    yazz.write(j)


"""

def oku():
    oku1=open("/home/aspa/CALISMALAR/PycharmProjects/jSONN/adress.txt","r")
    oku2=oku1.read()
    print(oku2)





print("-"*30)
oku()
print("-"*30)
print(book['ali'])
