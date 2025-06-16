class Node:
    next=None
    prev=None
    image1=None
    def __init__(self,image=None,prev=None,next=None):
        self.next=next
        self.prev=prev
        self.image1=image
    def getnext(self):
        return self.next
    def getprev(self):
        return self.prev
    def getimage(self):
        return self.image1
    def setnext(self,next):
        self.next=next
    def setprev(self,prev):
        self.prev=prev
    def setimage(self,image):
        self.image1=image