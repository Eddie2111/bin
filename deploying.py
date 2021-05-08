class db:
    def __init__(self,name='default'):
        self.name=name
        #100% complete..!
    def store(self,name):  #test it #stores password  #ok..!
        #storing format must be like this:
            #x={'cname':('Eddie2111','[a,1],[b,2],[c,3],[d,4]')}
        self.name=name
        with open ("db.txt", "a") as textico:
            print(self.name, file=textico)
        return 'stored..!'
    
    def encrypt(self,pas):  #done#encrypts password  #ok..!
        self.pas=pas
        arr1,arr2,arr3,arr4=[],[],[],[]
        keys=[]
        x=0
        if len(self.pas)%2==0:
            try:
                while len(self.pas)-1>x:
                    arr1.append(self.pas[x])
                    x+=1
                    arr2.append(self.pas[x])
                    x+=1
                    arr3.append(self.pas[x])
                    x+=1
                    arr4.append(self.pas[x])
                    x+=1
            except:
                g=0
        else:
            try:
                while len(self.pas)-1>x:
                    arr1.append(self.pas[x])
                    x+=1
                    arr2.append(self.pas[x])
                    x+=1
                    arr3.append(self.pas[x])
                    x+=1
                    arr4.append(self.pas[x])
                    x+=1
                arr1.append(self.pas[len(self.pas)-1])
            except:
                g=0
        realgtx=str((arr1,arr2,arr3,arr4))
        unreal_g=''
        for i in range(len(realgtx)):
            if realgtx[i]=="'":
                no_data=1
            else:
                unreal_g+=realgtx[i]
        
        return unreal_g
    
    def decrypt(self,g):  #takes a string as the four arrays and returns the password.
        self.g=g
        temp1,temp2=[],[]
        for i in range(len(g)):
            if g[i]=='[':
                temp1.append(i) 
            elif g[i]==']':
                temp2.append(i)
        text1=g[temp1[0]+1:temp2[0]]
        text2=g[temp1[1]+1:temp2[1]]
        text3=g[temp1[2]+1:temp2[2]]
        text4=g[temp1[3]+1:temp2[3]]
        real=''
        for i in range(8):
            try:
                real+=text1[i]
                real+=text2[i]
                real+=text3[i]
                real+=text4[i]
            except:
                pass
                error=0
        real_g=''
        for i in range(len(real)):
            if real[i]==',':
                rem=1
            else:
                real_g+=real[i]
        unreal_g=''
        for i in range(len(real_g)):
            if real_g[i]==' ':
                error=0
            else:
                unreal_g+=real_g[i]
        return unreal_g

    def s_retrieve(self,cname_main):
        self.cname_main=cname_main
        #instance incomplete[95% done] #shows email,id,pass
        #main retrieve section file..!#
        
        with open ('db.txt','r') as textfile:  #replace the location by the main db.txt file to complete 100%
            gstring=textfile.read() #read complete
        hexa=gstring.splitlines()
     

        a=cname_main  ###main input here...!!
        for i in range(0,len(hexa)):
            if a in hexa[i]:
                gotit=hexa[i]
            else:
                None 
        b_x=[]
        for i in range(len(gotit)):
            if gotit[i]=="'":
                b_x.append(i)
        a,b,c='','',''
        for i in range(b_x[0]+1,b_x[1]):
            a+=gotit[i]
        for i in range(b_x[2]+1,b_x[3]):
            b+=gotit[i]
        for i in range(b_x[4]+1,b_x[5]):
            c+=gotit[i]
        print(24*'=',"\n")
        print( 'Company: {}\nID: {}'.format(a,b))
        temp1,temp2=[],[]
        for i in range(len(c)):#
            if c[i]=='[':#
                temp1.append(i) 
            elif c[i]==']':#
                temp2.append(i)
        text1=c[temp1[0]+1:temp2[0]]####
        text2=c[temp1[1]+1:temp2[1]]
        text3=c[temp1[2]+1:temp2[2]]
        text4=c[temp1[3]+1:temp2[3]]
        real=''
        for i in range(8):
            try:
                real+=text1[i]
                real+=text2[i]
                real+=text3[i]
                real+=text4[i]
            except:
                error=0
        real_g=''
        for i in range(len(real)):
            if real[i]==',':
                rem=1
            else:
                real_g+=real[i]
        unreal_g=''
        for i in range(len(real_g)):
            if real_g[i]==' ':
                error=0
            else:
                unreal_g+=real_g[i]
        return 'Password: {}'.format(unreal_g)

    def selfsec(self,pass_x): #protects the whole program
        import hashlib
        self.pass_x=pass_x
        self.pass_x=hashlib.md5(self.pass_x.encode())
        g_hash=self.pass_x.hexdigest()
        if g_hash=='55295a43516e2fb71673ef48d38b690c':
            return 'welcome'
        else:
            return 'wrong password'
a=db()
def storing_style(x,y,z):  ##not implemented ##hardcode section is not changed
    return '\n {} \n'.format(a.store({x:(str(y),str(a.encrypt(z)))}))


print('Welcome to HexWall Password Storing System.')
while True:

    print('Chose an option:')
    input_x=input('[1]Store\n[2]Retrieve\n[3]Stored Key List\n[4]Exit Program\n=>')
    try:
        if int(input_x)==1:
            print('Storing System Initialized')
            x=str(input('company name:'))
            y=str(input('Id name: '))
            z=str(input('Password: '))
            print('\n',a.store({x:(str(y),str(a.encrypt(z)))}),'\n')
        if int(input_x)==2:
            for i in range(0,3):
                print('Please enter master password to continue: ')
                x=a.selfsec(str(input()))
                if 'elco' in x:
                    print(24*'=',"\n",'Retrieval System Initialized',24*'=',"\n")
                    x=str(input('company name:'))
                    print(a.s_retrieve(x),"\n",24*'=',"\n")
                    break
                if 'ron' in x:
                    print('Wrong password..!\n{} attepmts left'.format(2-i))
        if int(input_x)==3:
            #FIRST read the total db
            #Scan like the password headers
            #print only the company names
            print('Under construction.')
        if int(input_x)==4:
            print('Thanks for using HexWall')
            break
            exit()
    except:
        print('Please enter numbers from 1 to 4 to operate the software...!')
   
