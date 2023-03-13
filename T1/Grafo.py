import math

class Grafo:
    def __init__(self,arq) -> None:
        self.arq = arq
        self.vertices = None
        self.arestas = None
        self.inf = math.inf
        self.rotulo = None
        self.linhas = None
        self.matrix = None


    # Open file
    def OpenFile(self):
        arquivo = self.arq
        
        try:
            with open(arquivo, "r") as file:
                lines = [i for i in file.read().splitlines()]
        
        except FileNotFoundError:
            print("arquivo nao encontrado: %s" % arquivo)
            exit()
        
        self.linhas = lines

        return lines
    
    # Constroi matriz
    def ConstroiMatriz(self):
        # Using params as an emptry matrix, vertices and inf values to represent 
        matrix = self.matrix
        vertices = int(self.vertices) + 1
        inf = self.inf
        linhas = self.linhas

        # builing empty matrix 
        matrix = [[inf for x in range(vertices)] for y in range(vertices)]

        #submatrix contanting values for connections
        vals = vertices + 2
        submatrix = []
        for i in range(vals,len(linhas)):
            linha = linhas[i].split(" ")
            submatrix.append(linha)
        
        #Inserting values into empty matrix
        for i in submatrix:
            v1,v2,v3 = int(i[0]),int(i[1]), i[2]
            #print("v1 = %i, v2 = %i"%(v1,v2))
            matrix[v1][v2] = v3
        
        # saving matrix
        self.matrix = matrix

        #return matrix
        return matrix
    
    # Retorna a quantidade de vertices
    def QtdVertices(self):
        linha = self.linhas

        val = linha[0]

        self.vertices = val[9:]

        return self.vertices
    
    
    #Retorna a quantidade de arestas
    def qtdArestas(self):
        count = 0
        for i in range(self.vertices):
            for j in(0, i+1):
                if self.matrix[i][j] != self.inf:
                    count += 1
        return count

    #Verifica se há aresta
    def HaAresta(self,v1,v2):
        return True if self.matriz[v1][v2] != self.inf else False

    # Retorna o grau do vértice
    def grau(self,vertice):
        return self.vertices - self.matrix[vertice].count(self.inf)

    # cria lista de rótulos
    def Rotulo(self):
        linhas = self.linhas
        rotulos = []

        for i in linhas:
            if i == '*edges':
                break
            else:
                rotulos.append(i)

        for j in rotulos:
            rotulos = j.split(" ")

        self.rotulo = rotulos

        return rotulos
    
    # obtém valores de rótulos
    def getRotulo(self,vertice):
        return self.rotulo

    # Retorna o peso do vértice
    def peso(self,vertice1,vertice2):
        pass

    # Retorna os vizinhos do vertice
    def vizinhos(self,vertice):
        pass


if __name__ == '__main__':
    
    filex = 'T1/Instancias/facebook_santiago.net'
    
    g = Grafo(filex)
    
    g.OpenFile()

    g.QtdVertices()

    g.ConstroiMatriz()

    g.Rotulo()

    print(g.getRotulo(22))