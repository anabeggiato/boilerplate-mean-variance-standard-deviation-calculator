import numpy as np

def calculate(lista):

    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = np.zeros((3, 3))
        matrix[0] = lista[0:3]
        matrix[1] = lista[3:6]
        matrix[2] = lista[6:9]


        calculations = {
            'mean': [],
            'variance': [],
            'standard deviation': [],
            'max': [],
            'min': [],
            'sum': []
        }

        calculations['mean'] = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix)]
        calculations['variance'] = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)]
        calculations['standard deviation'] = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)]
        calculations['max'] = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)]
        calculations['min'] = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)]
        calculations['sum'] = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)]

        return calculations