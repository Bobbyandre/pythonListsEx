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
        
        


class LinearList(object):
    """ linear list """ 
    
    def __init__(self):
        """constructeur""" 
        
        self.head = None
        
        #self.longeur = 0 // peut etre implementer la longeur dans la liste ?
        
    def add(self,item):
        """ add a node to the list"""
        
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def isEmpty(self):
        return self.head == None
        
        
    def addAfter(self,base,item):
        """ add after ?? """ 
        temp=Node(item)
        temp.setNext(base.getNext())
        base.setNext(temp)
        
                

    def length(self):
        
        count=0 #this is the length
        current = self.head
        
        while(current != None):
            
            current = current.getNext()
            count+=1
        
        
        
        return count
        
    def search(self,item):
        """search into the list's nodes"""
        
        temp = self.head
        found = False
        
        while (temp != None and not found):
            
            
            if (temp.getVal() == item):
                found = True
                
                
                
            else:
                temp = temp.getNext()
                
                
                
        return found            
        
        
        
    def remove(self,item):
        """ remove an item from list """
        
        temp = None
        current = self.head
        found= False
        
        while(current != None and found):
            
            if(current.getVal() == item):
                found = True

            
            else:
                temp=current
                curent=current.getNext()
                
        if (found):
            if temp!= None:
                temp.setNext(current.getNext())
            else:
                self.head = current.getNext()
            
            
        
        
