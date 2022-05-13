import random

class mongodb:
    def __init__(self,text1,text2):
        self.text1=text1
        self.text2=text2
    def passgenerator(self):
        a = ''
        alpha, beta, number = [],[],[]
        for i in range(65,91): alpha.append(chr(i));
        for i in range(97,123): beta.append(chr(i));
        for i in range(0,10): number.append(str(i));
        alll = [alpha,beta,number]
        for i in range(0,16):
            a += random.choice(random.choice(alll))
        return a
    
    def createAccount(self,name,id_number):
        pass


print(mongodb('test','test').passgenerator())
