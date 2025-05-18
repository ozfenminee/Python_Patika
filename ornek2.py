#2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

def deep_reverse(lst):
    reversed_list = []
    for item in reversed(lst):  # dış listeyi ters çevir
        if isinstance(item, list):
            reversed_list.append(deep_reverse(item))  # iç liste varsa onu da ters çevir
        else:
            reversed_list.append(item)
    return reversed_list

# Örnek:
inp2 = [[1, 2], [3, 4], [5, 6, 7]]
print(deep_reverse(inp2))  # [[7, 6, 5], [4, 3], [2, 1]]
