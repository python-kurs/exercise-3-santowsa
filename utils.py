# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script
def countSingles(x,returnval=False):
    import pandas as pd
    """
    Count the sum of each single item in a list.
    
    Parameter:
    x : list or any format readable in python
        
    Returns:
    Printed total sum for each unique element in the list.
    If returnval = T
        Return will be saved in a variable.
    
    """
    if returnval:
        items = list(set(x))
        counts = []
        for value in items: 
            counts.append(x.count(value))
            countedDB = pd.DataFrame({'car_name': items, 'number': counts})
            return(countedDB)
    else:
        items = list(set(x))
        for value in items: 
            print(value, x.count(value))

def dirCreate(x):
    """
    Creates a subdirectory.
    
    Parameters:
    Preferenced subfolder to be createed.
    
    Return:
    Subfolderdirectory creation or a message that it already exists.
    
    """
    subdir = x.exists()
    if subdir:
        print("All good! Filepath {} already exists.".format(x))
    
    else:
        x.mkdir(parents = True, exist_ok = True)
        

