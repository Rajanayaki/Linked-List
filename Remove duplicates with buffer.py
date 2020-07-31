class node:
  def  __init__(self,data):
    self.data=data
    self.next=None

class linkedlist:
  def __init__(self):
    self.head=None
  
  def push(self,data):
    newnode=node(data)
    if self.head is None:
      self.head=newnode
    else:
      temp=self.head
      while(temp.next!=None):
        temp=temp.next
      temp.next=newnode

  def dups(self):
    hashMap={}
    newhead=curr=self.head
    hashMap[newhead.data]=1
    prev=self.head
    while(curr is not None):
      if curr.data not in hashMap:
        hashMap[curr.data]=1
        prev=curr
      else:
        next=curr.next
        prev.next=next
      curr=curr.next
    self.head=newhead
    
  def printlist(self):
    temp=self.head
    while(temp.next!=None):
      print(temp.data,end=" ")
      temp=temp.next
    print(temp.data)
    
ll=linkedlist()
size=int(input())
elements=list(map(int,input().split()))
for i in range(size):
  ll.push(elements[i])
ll.dups()
ll.printlist()
