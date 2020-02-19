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
      newnode.next=None
    else:
      newnode.next=self.head
      self.head=newnode

  def sumoflists(self,head1,head2,head3):
    curr1,curr2=head1,head2
    carry=0
    print(head1.data,)
    while curr1!=None and curr2!=None:
      sum=curr1.data+curr2.data+carry
      if sum>=10:
        carry=1
        sum=sum%10
      else:
        carry=0
        sum=sum
      temp=node(sum)
      if head3 is None:
        head3=temp
       else:
        prev.next=temp
      prev=temp
      curr1=curr1.next
      curr2=curr2.next
    if carry!=0:
      temp.next=node(carry)
    return head3
  
  def printlist(self):
    temp=self.head
    while(temp.next.next!=None):
      print(temp.data,end=" ")
      temp=temp.next
    print(temp.data,temp.next.data)
    
ll1=linkedlist()
ll2=linkedlist()
elements1=list(map(int,input().split()))
for i in range(len(elements1)):
  ll1.push(elements1[i])
elements2=list(map(int,input().split()))
for i in range(len(elements2)):
  ll2.push(elements2[i])
ll1.printlist()
ll2.printlist()
ll3=linkedlist()
ll3.head=ll3.sumoflists(ll1.head,ll2.head,ll3.head)
ll3.printlist()
