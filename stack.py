class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.root=None

    def push(self,value):
        node= Node(value)
        if self.root==None:
            self.root=node
            return
        node.next=self.root
        self.root=node

    def pop(self):
        if self.root==None:
            return
        popedNode=self.root
        self.root=popedNode.next
        return popedNode
    def peek(self):
        if self.root==None:
            return
        return self.root.value

st=Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print(st.pop().data)
print(st.pop().data)
print(st.pop().data)
print(st.pop().data)
