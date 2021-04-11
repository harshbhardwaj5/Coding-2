class graph:
    def __init__(self,Nodes):
        self.nodes=Nodes          #Nodes bhejj d ilike a,b,c,d
        self.adjlist={}

        for i in self.nodes:
            self.adjlist[i]=[]              #empty adjlist A:[],B:[]

    def Edgeadd(self,source,des):
        self.adjlist[source].append(des)
    
    def printgraph(self):
        for i in self.nodes:
            print(i, '-> ',self.adjlist[i])


    
        


g=graph(["A","B","C","D"])
edges=[('A','B'),('C','D')]
for u,v in edges:
    g.Edgeadd(u,v)
g.printgraph()