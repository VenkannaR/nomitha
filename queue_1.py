class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self,value):
        node=Node(value)
        if self.tail==None:
            self.tail=node
            self.head=node
        self.tail.next=node
        self.tail=node
    def dequeue(self):
        if self.head==None:
            return
        nodetoreturn=self.head
        self.head=nodetoreturn.next
        return nodetoreturn

q=Queue()
q.enqueue(10)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue().data)
print(q.dequeue().data)
print(q.dequeue().data)
