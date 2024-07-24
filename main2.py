def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    rtup = (items for items in aTup[::2])
    tup = tuple(rtup)
    return tup

x = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(x))