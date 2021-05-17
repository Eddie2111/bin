import time
def store(x):
    with open ("c:/Users/Acer/Desktop/New folder/firstSite.html", "a") as textico:
        print(x, file=textico)
    time.sleep((2))
    print("\nfile created\n")
        
print("Hi, this is website builder.")
data = ''
while True:
    print("Let's work\n[1].paragraph\n[2]line break\n[3]heading \n[4]horizontal line\n[5]marquee\n[6]Finish\n\npress 7 to exit")
    a = [1,2,3,4,5,6]
    x = int(input('=>'))
    if x==7:
        exit()
    if x in a:
        if x==1:
            data +=('<p>')
            data += input("Enter paragraph: ")
            data += ('</p>')
        if x==2:
            data +=('</br>')
            print('single line break added..!')
        if x==3:
            size = str(input('heading size: [1-6]'))
            data +=('<h{}>'.format(size))
            data += input("Enter paragraph: ")
            data +=('</h{}>'.format(size))
        if x==4:
            data +=('</hr>')
            print('#####line added####')
        if x==5:
            data +=('<p>')
            data += input("Enter paragraph: ")
            data += ('</p>')
        if x==6:
            store(data)
            data = ''
    else:
        g=x%10
        if g in a:
            print('did you mean number {} ?'.format(g))
        else:
            print('please input correct numbers of function..!')
        
        
