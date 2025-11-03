from app.model import multiply_matrices

def test_multiply_matrices():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = multiply_matrices(A, B)
    assert result == [[19, 22], [43, 50]]
