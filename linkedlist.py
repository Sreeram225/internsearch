class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_begin(head,new_node):
    new_node.next=head
    head=new_node
    return head
def insert_end(head,new_node):
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=new_node
    new_node.next=None
    return head
def insert_middle(head,new_node):
    temp=head
    while temp.data!="3":
        temp=temp.next
    new_node.next=temp.next
    temp.next=new_node
    return head
def print_List(head):
    temp=head
    while temp:
        print(temp.data)
        temp=temp.next
head=Node("1")
node2=Node("2")
node3=Node("3")
node4=Node("4")
head.next=node2
node2.next=node3
node3.next=node4
#head=insert_begin(head,Node("5"))
#head=insert_end(head,Node("4"))
head=insert_middle(head,Node("5"))
print_List(head)
