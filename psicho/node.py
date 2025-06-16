class Node:
    next = None
    prev = None
    text = None
    def __init__(self, next=None, prev=None, text=None):
        self.next = next
        self.prev = prev
        self .text = text
    def getnext(self):
        return self.next
    def setnext(self, next):
        self.next = next
    def getprev(self):
        return self.prev
    def setprev(self, prev):
        self.prev = prev
    def gettext(self):
        return self.text
    def settext(self, text):
        self.text = text
    def prinnode(self, node):
        print(node.text)
        if(node.next != None):
            self.prinnode(node.next)