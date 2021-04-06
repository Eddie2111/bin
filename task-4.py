stack = []
stack_test = []


a = '1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14}}'
#for test
for i in range (len(a)):
    if a[i] =='(':
        stack_test.append(a[i])
    if a[i] ==')':
        try:
            stack_test.remove('(')
        except:
            stack_test.append(a[i])
    if a[i] =='{':
        stack_test.append(a[i])
    if a[i] =='}':
        try:
            stack_test.remove('{')
        except:
            stack_test.append(a[i])
    if a[i] =='[':
        stack_test.append(a[i])
    if a[i] ==']':
        try:
            stack_test.remove('[')
        except:
            stack_test.append(a[i])
print(stack_test)

##attempted to implement class method##

class stack:
    stack_test = []
    def __init__(self):
        pass
    def push(self,append):
        self.append = append
        self.stack_test.append(self.append)
    def pop(self,remuv):
        self.remuv = remuv
        self.stack_test.remove(self.remuv)

a = '1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14}}'
#for test
for i in range (len(a)):
    if a[i] =='(':
        stack_test.append(a[i])
    if a[i] ==')':
        try:
            stack_test.remove('(')
        except:
            stack_test.append(a[i])
    if a[i] =='{':
        stack_test.append(a[i])
    if a[i] =='}':
        try:
            stack_test.remove('{')
        except:
            stack_test.append(a[i])
    if a[i] =='[':
        stack_test.append(a[i])
    if a[i] ==']':
        try:
            stack_test.remove('[')
        except:
            stack_test.append(a[i])
print(stack_test)
    
    

    
