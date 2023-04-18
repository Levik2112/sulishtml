class muvelet:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def osszeadas(self):
        return self.x+self.y
    def kivonas(self):
        return self.x-self.y

    def osztas(self):
        return self.x/self.y

    def szorzas(self):
        return self.x*self.y
    
    




#if __name__=='__main__':
if True:
    #tesztelés
    q=muvelet(1,2)
    print(q.osszeadas())
    print(q.kivonas())
    print(q.osztas())
    print(q.szorzas())
