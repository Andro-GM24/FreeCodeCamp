import numpy as np


def calculate(list):
    #get the list and put in a Numpy array
    array_np = np.array(list)

    if (len(array_np) != 9):  #if the len is not 9 throw the value error

        raise ValueError("List must contain nine numbers.")

    else:
        list = array_np.reshape(3, 3)  #reshape the list
        calculations = {}  #create the dictonario of the output

        elements = [
            'mean', 'variance', 'standard deviation', 'max', 'min', 'sum'
        ]  #add names of keys

        # to a procces repetitive use a way to iterate in the names of the operations and use it
        name_to_function = {
            'mean': 'mean',
            'variance': 'var',
            'standard deviation': 'std',
            'max': 'max',
            'min': 'min',
            'sum': 'sum'
        }

        # Apply each function on axis 0, 1, and on the flattened required
        for element in elements:
            func_name = name_to_function[element]#get the name of the function with the key 
            #getattr recover a the value of atribute of an object, 

            func = getattr(np, func_name)#save the functions of the array of the object numpy 
            calculations[element] = [# save the different calculations in a array call calculations
                func(list, axis=0).tolist(),
                func(list, axis=1).tolist(),
                func(list).tolist()
            ]

    return calculations
