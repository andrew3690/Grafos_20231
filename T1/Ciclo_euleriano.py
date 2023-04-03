from Grafo import Grafo

def ciclo_euler(grafo):
    grafo = Grafo(grafo)

    grafo.OpenFile()

    grafo.QtdVertices()

    grafo.ConstroiMatriz()
    
    # obtém a quantidade de vértices do Grafo
    vertices = grafo.QtdVertices()
    # vetor de vértices a serem visitados
    visitados = [False] * vertices
    #vetor de vértices disponíveis do grafo
    vertices_usados = {i: grafo.vizinhos(i) for i in range(vertices)}

    # Testando o Teorema 4.1.1
    for i in vertices_usados.values():
        if len(i) % 2 != 0:
            # valor de retorno
            retval = (False,[])
    
    # Testagem se há elementos disponíveis para busca
    inicio = 0
    for j, i in vertices_usados.items():
        if len(i) > 0:
            inicio = j
            break
    
    # Se não existir elmentos na fila, não é realizada a busca do ciclo
    if inicio == 0:
        retval = (False,[])

    # ponto inicial do ciclo
    ciclo = [inicio]

    # loop de verificação da existencia do ciclo, enquanto o vértice incial não for igual ao vértice final
    while True:
        # o vértice é verificado no ciclo
        for vertice in ciclo:
            # se o tamaho da quantidade de vizinhos do vértice for maior que 0
            if len(vertices_usados[inicio]) > 0:
                # seta o vértice inicial e o vértice atual e inicia a verificação do ciclo euleriano
                inicio = vertice
                atual = vertice
                break
        
        # vetor inical de verificação do subciclo, incializando com o vértice inical
        subciclo = [inicio]

        # loop de verificação do subciclo euleriano, verifica se consegue chegar ao vértice incial percorrendo a vizinhança
        while True:
            proximo = vertices_usados[atual]
            print(proximo)

            if atual == inicio:
                break

            # 12, 40, 53, 98, 131, 143, 147, 150, 168, 169, 206, 207, 211, 
            # 221, 227, 237, 239, 241, 244, 250, 256, 257, 260, 269, 283, 
            # 294, 299, 302, 315, 317, 322, 328, 336, 342, 349, 367, 387, 
            # 412, 433, 451, 506, 512, 521, 534, 542, 
            # 554, 562, 565, 573, 577, 586, 589, 591, 649, 653, 657, 662

    return retval
    
if __name__ == '__main__':
    grafo = 'Instancias/facebook_santiago.net'

    ciclo_euler(grafo)