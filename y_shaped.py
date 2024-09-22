class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def get_count(head):
    count=0
    start=head
    while start!=None:
        count+=1
        start=start.next
    return count
def intersection_node(node,head1,head2):
    temp1=head1
    temp2=head2
    
