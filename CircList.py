class Node(object):
    """node for lists"""
    
    def __init__(self,val):
        """constructeur"""
        
        self.val = val
        self.suivant = None
        
        
    def getVal(self):
        """get the value of the node"""
        return self.val
    
    def getNext(self):
        """ get next node of the list """
        return self.suivant
        
    def setNext(self,suivant):
        """ set the next node of the list"""
        self.suivant = suivant
        
    def setVal(self,value):
        """ set a new value for the node """
        self.val = value
        
        


class CircList(object):
    """circulaire list """ 
    
    def __init__(self):
        """constructeur"""
        self.head = Node(-1)
        self.head.setNext(self.head)
        
        
    def isEmpty(self):
        return self.head.getNext() == self.head
        
    def add(self,item):
        """ add for circular list"""
        
        temp=Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)
        
     
    def addAfter(self,base,item):
        
        temp=Node(item)
        temp.setNext(base.getNext())
        base.setNext(temp)
        
        
    def length(self):
        """length for circ"""
        count =0
        
        current = self.head.getNext()
        while(current!=self.head):
            
            count+=1
            current = current.getNext()
        
        return count
        
        
        
    def search(self,item):
        """search a circ list"""
        
        #temp=Node(item)
        found=False
        current = self.head.getNext()
        
        while(current != self.head and not found):
            if item == current.getVal():
                
                found=True
   
            else:
                current=current.getNext()
        
        return found
        
        
        
        
    def remove(self,base):
        """remove method for circ lists"""
        
        previous = self.head
        current = self.head.getNext()
        found = False
        
        while(current != self.head and not found):
            
            if current is base:
                found=True
                previous.setNext(current.getNext())

                
                
            else:
                previous = current
                current = current.getNext()
                


        
        
        
