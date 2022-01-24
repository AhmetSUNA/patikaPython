'''
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
'''

def duzlestir(liste):
    for oge in liste:
        if isinstance(oge, list):
            yield from duzlestir(oge)
        else:
            yield oge


liste = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
duzListe = [a for a in duzlestir(liste)]

duzListe

'''
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
'''

def tersineCevir(x):

    for i in x:
        i.reverse()
    x.reverse()

    return x
	
liste2 = [[1, 2], [3, 4], [5, 6, 7]]

tersineCevir(liste2)