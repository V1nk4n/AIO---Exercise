import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = vector1.dot(vector2)
    return result


def matrix_multi_vector(matrix, vector):
    result = matrix.dot(vector)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    len_of_vector = np.dot(matrix1, matrix2)
    return len_of_vector


def inverse_matrix(matrix):
    det = np.linalg.det(matrix)
    if det == 0:
        return
    result = np.linalg.inv(matrix)
    return result


