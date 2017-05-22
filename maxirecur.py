def maxi(v):
    """ max reccursive """ 
   
    if len(v) >= 2 : #
        res = v[1] if v[0] < v[1] else v[0] #plus grand elem entre les 2premier du vecteur
        
        v = [res]+ v[2:] #nouveau vecteur ou on enlever les deux premieer membre et seul le plus grand reste
        maxi(v)   # appel recursif sur un vecteur plus petit de un
       
