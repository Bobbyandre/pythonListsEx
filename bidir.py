class Node(object):
    """node for bidirect lists"""
    
    def __init__(self,val):
        """constructeur"""
        
        self.val = val
        self.suivant = None
        self.previous = None
        
        
    def getVal(self):
        """get the value of the node"""
        return self.val
    
    def getNext(self):
        """ get next node of the list """
        return self.suivant
    
    def getPrevious(self):
        """ get previous node of the list""" 
        return self.previous

            
    def setNext(self,suivant):
        """ set the next node of the list"""
        self.suivant = suivant
        
    def setVal(self,value):
        """ set a new value for the node """
        self.val = value
        
    def setPrevious(self,previous):
        """set a new previous for the node """
        self.previous = previous
        
        



class BidirList(object):
    """ bidirectional list """
    
    def __init__(self):
        """constructeur"""
        
        self.head = None
        
        
    def add(self,item):
        """ add item in bidir list"""
        
        temp = Node(item)
        if self.head != None:
            self.head.setPrevious(temp)
        temp.setNext(self.head)
        self.head = temp

        
    def addAfter(self,base,item):
        
        temp= Node(item)
        
        temp.setPrevious(base.getPrevious())
        base.getPrevious().setNext(temp)

        base.setPrevious(temp)
        temp.setNext(base)
        
        
        
        
