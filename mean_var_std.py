import numpy as np

def calculate(list_of_numbers):
    # Raise ValueError if list has less than 9 elements
    if (len(list_of_numbers) != 9):
        raise ValueError('List must contain nine numbers.')

    np_array = np.array(list_of_numbers).reshape(3, 3)
    
    calculations = {
        "mean": [list(np.mean(np_array, axis=0)), list(np.mean(np_array, axis=1)), np.mean(np_array)],
        "variance": [list(np.var(np_array, axis=0)), list(np.var(np_array, axis=1)), np.var(np_array)],
        "standard deviation": [list(np.std(np_array, axis=0)), list(np.std(np_array, axis=1)), np.std(np_array)],
        "max": [list(np.max(np_array, axis=0)), list(np.max(np_array, axis=1)), np.max(np_array)],
        "min": [list(np.min(np_array, axis=0)), list(np.min(np_array, axis=1)), np.min(np_array)],
        "sum": [list(np.sum(np_array, axis=0)), list(np.sum(np_array, axis=1)), np.sum(np_array)]
    }

    return calculations