class Main{
  static Node head;
  static class Node{
     int data;
     Node next;
     Node(int d)
     {
       data=d;
       next=null;
     }
  }
  void detectandremoveloop(Node node)
  {
     if (node==null || node.next==null)
     {
       return;
     }
     Node slow=node,fast=node;
     slow=slow.next;
     fast=fast.next.next;
     while(fast!=null && fast.next!=null)
     {
       if(slow==fast)
         break;
      slow=slow.next;
      fast=fast.next.next;
     }
     if(slow!=fast)
     {
       System.out.println("No loop");
       return;
     }
     if(slow==fast)
     {
       slow=node;
       while(slow.next!=fast.next)
       {
         slow=slow.next;
         fast=fast.next;
       }
       fast.next=null;
     }
  }


  void printlist(Node node)
  { int count=0;
    while(node!=null)
    {
      System.out.print(node.data+" ");
      node=node.next;
      count+=1;
    }
  }
  public static void main(String[] args)
  {
    Main m=new Main();
    m.head=new Node(50);
    m.head.next=new Node(100);
    m.head.next.next=new Node(150);
    m.head.next.next.next=new Node(10);
    m.head.next.next.next.next=new Node(14);
    m.head.next.next.next.next.next=new Node(16);

        head.next.next.next.next.next.next = head.next.next; 
    m.detectandremoveloop(head);
    System.out.println("Removing ");
    m.printlist(head);

  }











}
