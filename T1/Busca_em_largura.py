from Grafo import Grafo

def BuscaL(grafo,vertice):

    grafo = Grafo(grafo)

    grafo.OpenFile()

    grafo.QtdVertices()

    grafo.ConstroiMatriz()
    
    grafo = Grafo(grafo)
    # obtém a quantidade de vértices do Grafo
    vertices = grafo.QtdVertices()
    # vetor de vértices visitados
    visitados = [False] * vertices
    # vetor de vertices a serem visitados
    proximo = [vertice]
    # nivel de busca inicia em zero
    nivel = 0

    while True:
        atual = proximo.copy()
        proximo = []

        #
        for i in range(len(atual)):
            # inserção de elementos a serem visitados no atual
            v = atual[i]
            # Marcação de elemento visitado
            visitados[v] = True
            # lista de vetores não visitados
            nao_visitados = list(filter(lambda x:not visitados[x], grafo.vizinhos(v)))
            
            #
            for x in nao_visitados:
                visitados[x] = True
            
            proximo.extend(nao_visitados)
        
        print("%d: "%(nivel), end = ' ')
        print(",".join(map(lambda y:str(y+1),atual)))

        if len(proximo) == 0:
            break

        nivel += 1
<<<<<<< HEAD


if __name__ == '__main__':
    file = 'Instancias/facebook_santiago.net'
=======
>>>>>>> c43daa2622bf987d3c5ee5e7f5a44f66b16bc0e1
    
if __name__ == '__main__':
    grafo = 'Instancias/facebook_santiago.net'
    v = int(input("vertice inicial: \n "))

    BuscaL(grafo,v)