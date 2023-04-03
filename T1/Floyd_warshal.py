from Grafo import Grafo

def floydWarshall(grafo):

    grafo = Grafo(grafo)

    grafo.OpenFile()

    grafo.QtdVertices()

    grafo.ConstroiMatriz()

    # obtém a quantidade de vértices do Grafo
    qtdvertices = grafo.QtdVertices()

    # 5.4 pag. 57
    for k in range(qtdvertices):
        for u in range(qtdvertices):
            for v in range(qtdvertices):
                grafo.matrix[u][v] = min(grafo.matrix[u][v],grafo.matrix[u][k] + grafo.matrix[k][v])
    
    # output
    for i in range(qtdvertices):
        print(f"{i+1}: ", end="")
        print(*grafo.matrix[i], sep=", ")

if __name__ == "__main__":
    grafo = "Instancias/fln_pequena.net" # Aqui vai o arquivo que sera utilizado como base
    floydWarshall(grafo)