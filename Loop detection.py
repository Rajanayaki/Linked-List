class node:
  def  __init__(self,data):
    self.data=data
    self.next=None

class linkedlist:
  def __init__(self):
    self.head=None
  
  def push(self,data):
    newnode=node(data)
    temp=self.head
    newnode.next=self.head
    if self.head is not None:
      temp=self.head
      while(temp.next!=self.head):
        temp=temp.next 
      temp.next=newnode   
    else:
      newnode.next=newnode
    self.head=newnode
  
  def loop(self):
    self.head.next.next.next.next=self.head.next.next
   
  def loopdetect(self):
    slow=self.head.next
    fast=self.head.next.next
    while(fast!=None and fast.next!=None):
      if fast==slow:
        break
      fast=fast.next.next
      slow=slow.next
    if fast!=slow:
      print("No loop")
    slow=self.head
    while(fast!=slow):
      fast=fast.next
      slow=slow.next
    print(slow.data)
      
  def printlist(self):
    temp=self.head
    while(temp.next!=self.head):
      print(temp.data,end=" ")
      temp=temp.next
    print(temp.data)
    
ll=linkedlist()
size=int(input())
elements=list(map(int,input().split()))
for i in range(size):
  ll.push(elements[i])
ll.printlist()
ll.loop()
ll.loopdetect()
