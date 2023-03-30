from Grafo import Grafo

def Ciclo_Euleriano(grafo):
    grafo = Grafo(grafo)

    grafo.OpenFile()

    grafo.QtdVertices()

    grafo.ConstroiMatriz()

    # obtém a quantidade de vértices do Grafo
    qtdvertices = grafo.QtdVertices()

    # Dicionário de vértices do grafo 
    vertices = {i: grafo.vizinhos(i) for i in range(qtdvertices)}

    # Loop de verificação se o vértice possui a quantidade de arestas de tamanho par
    for i in vertices.values():
        if len(i) % 2 != 0:
            retval = (False,[])
            
    
    # Loop de verificação se existe elementos no grafo
    inicio = 0
    for chave, arestas in vertices.items():
        if len(arestas) > 0:
            inicio = chave
            break
    
    # Não há elementos no grafo
    if inicio == 0:
        retval = (False, [])
    
    # Ciclo a ser verificado
    ciclo = [inicio]
    
    # Enquanto o ciclo estiver 
    while True:
        # 
        for vertice in ciclo:
            #
            if len(vertices[vertice]) > 0:
                # 
                inicio = vertice
                atual = vertice
                break
        
        # Realização do subciclo 
        subciclo = [atual]
        
        while True:
            proximo = vertices[atual].pop()
            vertices[proximo].remove(atual)


if __name__ == '__main__':
    file = 'Instancias/facebook_santiago.net'

    print(Ciclo_Euleriano(file))