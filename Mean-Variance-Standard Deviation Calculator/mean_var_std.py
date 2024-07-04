import numpy as np

def calculate(list):
    calculations = dict()
    array_arg=np.array(list)
    matrix_arg= array_arg.reshape(3,3)
    mean_a1 = np.mean(matrix_arg, axis=0)
    mean_a2 = np.mean(matrix_arg, axis=1)
    mean_flattened = np.mean(list)
    variance_a1 = np.var(matrix_arg, axis=0)
    variance_a2 = np.var(matrix_arg, axis=1)
    variance_flattened = np.var(list)
    std_dev_a1= np.std(matrix_arg, axis=0)
    std_dev_a2= np.std(matrix_arg, axis=1)
    std_dev_flattened = np.std(list)
    max_a1 = np.max(matrix_arg, axis=0)
    max_a2 = np.max(matrix_arg, axis=1)
    max_flattened = np.max(list)
    min_a1 = np.min(matrix_arg, axis=0)
    min_a2 = np.min(matrix_arg, axis=1)
    min_flattened = np.min(list)
    sum_a1 = np.sum(matrix_arg, axis =0)
    sum_a2 = np.sum(matrix_arg, axis =1)
    sum_flattened = np.sum(list)
    calculations['mean'] = [mean_a1.tolist(), mean_a2.tolist(), mean_flattened.tolist()]
    calculations['variance'] = [variance_a1.tolist(), variance_a2.tolist(), variance_flattened.tolist()]
    calculations['standard deviation'] = [std_dev_a1.tolist(), std_dev_a2.tolist(), std_dev_flattened.tolist()]
    calculations['max'] = [max_a1.tolist(), max_a2.tolist(), max_flattened.tolist()]
    calculations['min'] = [min_a1.tolist(), min_a2.tolist(), min_flattened.tolist()]
    calculations['sum'] = [sum_a1.tolist(), sum_a2.tolist(), sum_flattened.tolist()]
    return calculations