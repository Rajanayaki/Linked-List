cclass node:
  def __init__(self,data):
    self.data=data
    self.next=None

class linkedlist:
  def __init__(self):
    self.head=None

  def add(self,data):
    newnode=node(data)
    newnode.next = self.head 
    self.head = newnode


  def sumlists(self,head1,head2):
    curr1=head1
    curr2=head2
    
    carry=0
    while curr1!=None and curr2!=None:
      sum=curr1.data+curr2.data+carry
      if sum>=10:
        carry=1
        sum=sum%10
      else:
        carry=0
      temp=node(sum)
      if self.head is None:
        self.head=temp
      else:
        prev.next=temp
      prev=temp
      curr1=curr1.next
      curr2=curr2.next
    if carry>0:
      temp.next=node(carry)
    return self.head
  
  def reverse(self):
    curr=self.head
    prev=None
    while curr is not None:
      next=curr.next
      curr.next=prev
      prev=curr
      curr=next
    self.head=prev

  def printlist(self):
    while (self.head.next!=None):
      print(self.head.data,end=" ")
      self.head=self.head.next
    print(self.head.data)

        
ll1=linkedlist()
size1=int(input())
datalist1=list(map(int,input().split()))
for i in range(size1):
  ll1.add(datalist1[i])
ll2=linkedlist()
size2=int(input())
datalist2=list(map(int,input().split()))
for i in range(size2):
  ll2.add(datalist2[i])
ll=linkedlist()
ll.head=ll.sumlists(ll1.head,ll2.head)
ll.reverse()
ll.printlist()




