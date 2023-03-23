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
    
    # Build matriz
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
    
    # Returns how many vertxes on the graph
    def QtdVertices(self):
        linha = self.linhas

        val = linha[0]

        self.vertices = int(val[9:])

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
        return True if self.matrix[v1][v2] != self.inf else False
    
    def GetWeight(self,v1,v2):
        # Visa o obter o peso da aresta entre v1 e v2
        return self.matrix[v1][v2]

    # Retorna o grau do vértice
    def grau(self,vertice):
        return self.vertices - self.matrix[vertice].count(self.inf)

    # cria lista de rótulos
    def Rotulo(self):
        linhas = self.linhas
        rotulos = []
        self.rotulo = {}

        for i in linhas:
            if i == '*edges':
                break
            else:
                rotulos.append(i)
        
        for j in rotulos:
            rot = j.split(" ")
            self.rotulo.update({rot[0]:rot[1:]})
        
        return self.rotulo

    # obtém valores de rótulos
    def getRotulo(self,rotulo):
        dick = self.rotulo
        rotulo = str(rotulo)

        if rotulo in dick.keys():
            print(dick[rotulo])
        else:
            print("Rótulo não existente")
        
        
    # Retorna os vizinhos do vertice
    def vizinhos(self,vertice):
        vizinhos = []
        
        for i in range (0,self.vertices):
            if self.matrix[vertice][i] != self.inf:
                vizinhos.append(i)
            else:
                pass

        return vizinhos

if __name__ == '__main__':
    
    filex = 'Instancias/facebook_santiago.net'
    
    g = Grafo(filex)
    
    g.OpenFile()

    g.QtdVertices()

    g.ConstroiMatriz()

    g.Rotulo()

    print(g.getRotulo(22))

    print(g.GetWeight(86,114))

    print(g.vizinhos(86))