
if __name__ == "__main__":
    with open("Alice_Maravilhas.txt") as file:
        texto = file.read().lower()
    
    limpa_texto = [l for l in texto if l.isalpha()]

    lista_letras = {}

    for l in limpa_texto:
        lista_letras_ordenadas = l.get(l, 0) + 1
    
    from collections import Counter
    lista_letras = Counter(lista_letras)
    import matplotlib.pyplot as plt

    rotulos, valores = zip(lista_letras_ordenadas.most_common(10))
    plt.title("Frequencia")
    plt.bar(rotulos,valores)
    plt.show()
    plt.savefig("Livro.png")
    plt.close() 


