"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from math import inf
with open('data.csv','r') as tabla:
    file=csv.reader(tabla,delimiter='	')
    lista=list(file)
    
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma =0
    for i in lista: suma+=int(i[1])
    return suma

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    li=['A','B','C','D','E']
    mx=[]
    for i in li: 
        tmp=len(list(filter(lambda x: x[0]==i,lista)))
        mx.append((i,tmp))
    return mx


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    

    """
    li=['A','B','C','D','E']
    mx=[]
    for i in li: 
        tmp=list(filter(lambda x: x[0]==i,lista))
        suma=0
        for x in tmp: suma+=int(x[1])
        mx.append((i,suma))
    return mx



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    m=["01","02","03","04","05","06","07","08","09","10","11","12"]
    meses=[0 for i in range(12)]
    for i in lista:
        mes=int(i[2][5:7])
        meses[mes-1]+=1

    return [(m[i],meses[i])for i in range(12)]


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    maxis={"A":0,"B":0,"C":0,"D":0,"E":0}
    for i in lista: 
        if maxis.get(i[0])[0] < int(i[1]): maxis[i[0]][0]=int(i[1])
        if maxis.get(i[0])[1] > int(i[1]): maxis[i[0]][1]=int(i[1])
    return [(i,maxis[i][0],maxis[i][1]) for i in maxis.keys()]

def formating(str):
    output = ""
    quoting = False
    for char in str:
        if char.isalnum():
            if not quoting:
                output += '"'
                quoting = True
        elif quoting:
            output += '"'
            quoting = False
        output += char
    return output
from json import loads
def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computaedt , 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    maxis={"aaa":0,"bbb":0,"ccc":0,"ddd":0,"eee":0,"fff":0,"ggg":0,"hhh":0,"iii":0,"jjj":0}
    dts=[loads(formating('{'+i[4]+'}')) for i in lista]
    for i in dts:
        for k in i.keys():
            if maxis[k][0] < int(i[k]):maxis[k][0]=int(i[k])
            if maxis[k][1] > int(i[k]):maxis[k][1]=int(i[k])
        
    return [(i,maxis[i][1],maxis[i][0]) for i in maxis.keys()]


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    li=[[] for i in range(10)]
    for i in lista:
        li[int(i[1])].append(i[0])
    return [(i,li[i]) for i in range(10)]




def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    li=[[] for i in range(10)]
    for i in lista:
        li[int(i[1])].append(i[0])
    return [(i,sorted(list(set(li[i])))) for i in range(10)]


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    maxis={"aaa":0,"bbb":0,"ccc":0,"ddd":0,"eee":0,"fff":0,"ggg":0,"hhh":0,"iii":0,"jjj":0}
    dts=[loads(formating('{'+i[4]+'}')) for i in lista]
    for i in dts:
        for k in i.keys():
            maxis[k]+=1
    return maxis

from re import sub
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """ 

    return [(i[0],len(list(sub('\,','',i[3]))),len(loads(formating('{'+i[4]+'}')))) for i in lista]

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    dt={
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
    }
    for i in lista:
        for k in list(sub('\,','',i[3])): dt[k]+=int(i[1])
    return dt



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    rt= {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }
    for i in lista: rt[i[0]]+=sum(map(int,loads(formating('{'+i[4]+'}')).values()))
    return rt
print(pregunta_12())