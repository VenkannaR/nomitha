class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

    def is_circular(head):
        if head==None:
            return False
        
        slow=head
        fast=head.next
        while fast and fast.next:
            if slow==fast:
                return True
            










      





