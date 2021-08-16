class graph:
    graphDB={}
    def __init__(self,data=None):
        self.data=data

    def add_vertex(self,key):
        self.key=key
        if self.key not in self.graphDB:
            self.graphDB[self.key]=[]
        if self.key in self.graphDB:
            self.graphDB.pop(self.key)
            self.graphDB[self.key]=[]
                
    def addEdge(self,key,value):
        self.key=key
        self.value=value
        if self.key not in self.graphDB:
            self.graphDB[self.key]=list(self.value)
        if self.key in self.graphDB:
            self.graphDB[self.key].append(self.value)

    def constructGraph(self,a):
        self.a=a
        for i in range(len(self.a)):
            x1=self.a[i][0]
            self.add_vertex(x1)
            for j in range(1,len(self.a[i])):
                self.addEdge(x1,a[i][j])
                
    def printAdjacentList(self):
        print(self.graphDB)
        return self.graphDB
class stack:
    stackdb=[]
    def __init__(self,data=None):
        self.data=data
        
    def push(self,key):
        self.key=key
        self.stackdb.append(self.stackdb)
    def pop(self):
        self.stackdb.pop()
    def db(self):
        return stackdb

if __name__=='__main__':
    a=[ 
        [12], 
        [1, 2], 
        [2, 3, 4, 5], 
        [3, 4, 7, 11], 
        [4], 
        [5, 6, 7], 
        [6, 7, 8], 
        [7,11], 
        [8, 9, 10], 
        [9, 10], 
        [10, 11], 
        [11, 12], 
        [12]
    ]
    graph().constructGraph(a)
    x=graph().printAdjacentList()
    a={
        "kafrul":["cantonment","mirpur14"],
        "cantonment":["banani","kafrul","bijoysarani","matikata","ecb"],
        "ecb":["cantonment"],
        "policeStation":["mirpur14","mirpur13"],
        "matikata":["mirpur13","mirpur14"],
        "mirpur14":["matikata","mirpur11"],
        "mirpur11":["mirpur13","policeStation"],
        "mirpur13":["stadium","herbalUniversity"],
        "stadium":["rupnagar","shiyalbari"]
        }  

    def dfs(a,x1,x2): #x1=start x2=end  #has problem, only works for 1-12
        main,x1=[],1
        while x1!=x2 :
            if x1 not in main:
                main.append(x1)
            for i in a[x1]:
                if i not in main:
                    main.append(i)
            x1=main[len(main)-1]
        print(main)
    def dfs1(a,end):
        stack=[]
        isOff=False
        
        print(stack)

    def bfs(a,x,y):
        queue=[]
        main=[]
        #while x!=y:
            
        print(queue)

def test():
    start="kafrul"
    end="shiyalbari"
    def dfs(graph,start,end):
        stack=[]
        for i in range(5):
            if start!=end:
                stack.append(graph[start])
                for i in range(len(graph[start])):
                    if graph[start][i]==end:
                        print(graph[start][i])
                        exit()
                    else:
                        x=graph[start][i]
                        stack.append(graph[start][i])
                start=x
        
#dfs(a,start,end)
start="kafrul"
end="ecb"
dfs1(x,12)
#bfs(x,1,12)



