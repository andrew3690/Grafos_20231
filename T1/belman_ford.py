from Grafo import Grafo

def resultado(res):
    distancias = res[0]
    caminhos = res[1]

    for destino, antecessor in caminhos.items():
        caminho = []
        while antecessor is not None:
            caminho.insert(0,antecessor)
            antecessor = caminhos[antecessor]
        caminho.append(destino)
        print(
            "%d: " %(destino) +
            ",".join(map(lambda x: str(x), caminho)) +
            "; d=%.2f" % (distancias[destino])
        )

def BelamnFord(grafo,vertice):
    grafo = Grafo(grafo)

    grafo.OpenFile()

    grafo.QtdVertices()

    grafo.ConstroiMatriz()

    verts = grafo.QtdVertices()
    
    # iniciando as distancias do vértice
    distancias = {vertice: grafo.inf for vertice in range(1,verts+1)}
    
    # caminhos dos vértices
    caminho = {vertice: None for vertice in range(1,verts+1)}
    
    # a distancia do vértice inicial para si mesmo é zero
    distancias[vertice] = 0

    #vertices
    vertices = [int(v) for v in range(1,verts+1)]
    
    while vertices:
        # vertice não visitado cuja distancia é minima aresta 
        atual = min(vertices, key=lambda vertice: distancias[vertice])

        # arestas de menor custo tem peso infinito
        if(distancias[atual] == grafo.inf):
            break
        print(list(filter(lambda x: x in vertices, grafo.vizinhos(atual))))
        for vertice in list(filter(lambda x: x in vertices, grafo.vizinhos(atual))):
            rota = distancias[atual] + int(grafo.GetWeight(atual,vertice))

            if(rota < distancias[vertice]):
                distancias[vertice] = rota
                caminho[vertice] = atual
        vertices.remove(atual)
    
    return(distancias, caminho)

if __name__ == '__main__':
    grafo = 'Instancias/fln_pequena.net'

    v = int(input("vertice inicial: \n "))

    resultado(BelamnFord(grafo,v))