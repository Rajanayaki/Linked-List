class Stack:
  def __init__(self):
    i=0
    self.threeStack=[]
    while(i!=30):
      i+=1
      self.threeStack.append("0")
      self.stack1=0
      self.stack2=10
      self.stack3=20
 
  def push(self,stackNum,elementToPush):
    if stackNum==1:
      self.threeStack[self.stack1]=elementToPush
      self.stack1+=1
    elif stackNum==2:
      self.threeStack[self.stack2]=elementToPush
      self.stack2+=1
    else:
      self.threeStack[self.stack3]=elementToPush
      self.stack3+=1
  

  def pop(self,stackNum):
   
    if stackNum==1:
      print(self.threeStack[self.stack1-1])
      self.stack1-=1
    elif stackNum==2:
      print(self.threeStack[self.stack2-1])
      self.stack2-=1
    else:
      print(self.threeStack[self.stack3-1])
      self.stack3-=1
  
  def print(self):
    if len(self.threeStack[0:self.stack1])!=0:
      print("stack1")
      for i in range(self.stack1):
        print(self.threeStack[i])
    else:
      print("NULL")
    if len(self.threeStack[10:self.stack2])!=0:  
      print("stack2")
      for i in range(10,self.stack2):
        print(self.threeStack[i])
    else:
      print("NULL")
    if len(self.threeStack[20:self.stack3])!=0:  
      print("stack3")
      for i in range(20,self.stack3):
        print(self.threeStack[i])
    else:
      print("NULL")

size = int(input("Number of elements "))
s=Stack()
for i in range(size):
   l=list(map(int,input().split()))
   s.push(l[0],l[1])
print("Stack elements:")
s.print()
sizetopop=int(input("Stack to pop:"))
for i in range(sizetopop):
   s.pop(int(input()))
