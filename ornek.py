##1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # iç içe liste varsa yine flatten ile aç
        else:
            result.append(item)
    return result

# Örnek:
inp1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(inp1))  # [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
