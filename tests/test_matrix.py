import pytest
from src.matrix.matrix import Matrix

class TestMatrix:
    def setup_method(self):
        self.matrix = Matrix()

    # ── Suma ──────────────────────────────────────────────────────────────────

    def test_suma_matrices(self):
        # Test con matrices de enteros
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        assert self.matrix.suma_matrices(A, B) == [[6, 8], [10, 12]]

        # Test con valores negativos y ceros
        A2 = [[0, -1], [2, 3]]
        B2 = [[1, 1], [-2, 0]]
        assert self.matrix.suma_matrices(A2, B2) == [[1, 0], [0, 3]]

        # Test con matrices 1x1
        assert self.matrix.suma_matrices([[5]], [[3]]) == [[8]]

        # Test con matrices 3x3
        A3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        B3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert self.matrix.suma_matrices(A3, B3) == [[2, 2, 3], [4, 6, 6], [7, 8, 10]]

        # Test con dimensiones incompatibles (debe lanzar ValueError)
        with pytest.raises(ValueError):
            self.matrix.suma_matrices([[1, 2]], [[1, 2], [3, 4]])

    # ── Resta ─────────────────────────────────────────────────────────────────

    def test_resta_matrices(self):
        # Test con matrices de enteros
        A = [[5, 6], [7, 8]]
        B = [[1, 2], [3, 4]]
        assert self.matrix.resta_matrices(A, B) == [[4, 4], [4, 4]]

        # Test con resultado negativo
        A2 = [[1, 2], [3, 4]]
        B2 = [[5, 6], [7, 8]]
        assert self.matrix.resta_matrices(A2, B2) == [[-4, -4], [-4, -4]]

        # Test con matrices 1x1
        assert self.matrix.resta_matrices([[9]], [[4]]) == [[5]]

        # Test con dimensiones incompatibles (debe lanzar ValueError)
        with pytest.raises(ValueError):
            self.matrix.resta_matrices([[1, 2, 3]], [[1, 2], [3, 4]])

    # ── Multiplicación matricial ───────────────────────────────────────────────

    def test_multiplicar_matrices(self):
        # Test con matrices cuadradas 2x2
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        assert self.matrix.multiplicar_matrices(A, B) == [[19, 22], [43, 50]]

        # Test con matriz 2x3 por 3x2
        A2 = [[1, 2, 3], [4, 5, 6]]
        B2 = [[7, 8], [9, 10], [11, 12]]
        assert self.matrix.multiplicar_matrices(A2, B2) == [[58, 64], [139, 154]]

        # Test con matriz identidad (resultado igual a la original)
        identidad = [[1, 0], [0, 1]]
        M = [[3, 4], [5, 6]]
        assert self.matrix.multiplicar_matrices(identidad, M) == M

        # Test con dimensiones incompatibles (debe lanzar ValueError)
        with pytest.raises(ValueError):
            self.matrix.multiplicar_matrices([[1, 2]], [[1, 2]])

    # ── Multiplicación escalar ────────────────────────────────────────────────

    def test_multiplicar_escalar(self):
        # Test con enteros
        M = [[1, 2], [3, 4]]
        assert self.matrix.multiplicar_escalar(M, 3) == [[3, 6], [9, 12]]

        # Test con escalar cero
        assert self.matrix.multiplicar_escalar([[1, 2], [3, 4]], 0) == [[0, 0], [0, 0]]

        # Test con escalar negativo
        assert self.matrix.multiplicar_escalar([[1, -2], [3, -4]], -1) == [[-1, 2], [-3, 4]]

        # Test con matriz 1x1
        assert self.matrix.multiplicar_escalar([[5]], 4) == [[20]]

    # ── Transpuesta ───────────────────────────────────────────────────────────

    def test_transpuesta(self):
        # Test con matriz 2x3
        M = [[1, 2, 3], [4, 5, 6]]
        assert self.matrix.transpuesta(M) == [[1, 4], [2, 5], [3, 6]]

        # Test con matriz cuadrada 2x2
        assert self.matrix.transpuesta([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

        # Test con matriz 1x1
        assert self.matrix.transpuesta([[7]]) == [[7]]

        # Test con matriz vacía
        assert self.matrix.transpuesta([]) == []

    # ── Es cuadrada ───────────────────────────────────────────────────────────

    def test_es_cuadrada(self):
        # Test con matriz cuadrada 2x2
        assert self.matrix.es_cuadrada([[1, 2], [3, 4]]) == True

        # Test con matriz cuadrada 3x3
        assert self.matrix.es_cuadrada([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == True

        # Test con matriz no cuadrada 2x3
        assert self.matrix.es_cuadrada([[1, 2, 3], [4, 5, 6]]) == False

        # Test con matriz 1x1
        assert self.matrix.es_cuadrada([[5]]) == True

        # Test con matriz vacía
        assert self.matrix.es_cuadrada([]) == False

    # ── Es simétrica ─────────────────────────────────────────────────────────

    def test_es_simetrica(self):
        # Test con matriz simétrica 2x2
        assert self.matrix.es_simetrica([[1, 2], [2, 1]]) == True

        # Test con matriz simétrica 3x3
        M = [[1, 2, 3], [2, 5, 6], [3, 6, 9]]
        assert self.matrix.es_simetrica(M) == True

        # Test con matriz no simétrica
        assert self.matrix.es_simetrica([[1, 2], [3, 4]]) == False

        # Test con matriz identidad (es simétrica)
        assert self.matrix.es_simetrica([[1, 0], [0, 1]]) == True

    # ── Traza ────────────────────────────────────────────────────────────────

    def test_traza(self):
        # Test con matriz 2x2
        assert self.matrix.traza([[1, 2], [3, 4]]) == 5

        # Test con matriz 3x3
        assert self.matrix.traza([[1, 0, 0], [0, 5, 0], [0, 0, 9]]) == 15

        # Test con matriz 1x1
        assert self.matrix.traza([[7]]) == 7

        # Test con valores negativos
        assert self.matrix.traza([[-1, 0], [0, -4]]) == -5

        # Test con matriz no cuadrada (debe lanzar ValueError)
        with pytest.raises(ValueError):
            self.matrix.traza([[1, 2, 3], [4, 5, 6]])

    # ── Determinante 2x2 ─────────────────────────────────────────────────────

    def test_determinante_2x2(self):
        # Test con resultado negativo
        assert self.matrix.determinante_2x2([[3, 8], [4, 6]]) == -14

        # Test con resultado negativo simple
        assert self.matrix.determinante_2x2([[1, 2], [3, 4]]) == -2

        # Test con determinante cero (matriz singular)
        assert self.matrix.determinante_2x2([[2, 4], [1, 2]]) == 0

        # Test con matriz identidad (det = 1)
        assert self.matrix.determinante_2x2([[1, 0], [0, 1]]) == 1

        # Test con matriz no 2x2 (debe lanzar ValueError)
        with pytest.raises(ValueError):
            self.matrix.determinante_2x2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # ── Determinante 3x3 ─────────────────────────────────────────────────────

    def test_determinante_3x3(self):
        # Test con determinante cero (filas proporcionales)
        M1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert self.matrix.determinante_3x3(M1) == 0

        # Test con matriz diagonal (det = producto de diagonal)
        M2 = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
        assert self.matrix.determinante_3x3(M2) == 6

        # Test con valores generales
        M3 = [[2, -1, 0], [1, 3, -2], [0, 1, 4]]
        assert self.matrix.determinante_3x3(M3) == 32 # da 32 no 30 ;)

        # Test con matriz no 3x3 (debe lanzar ValueError)
        with pytest.raises(ValueError):
            self.matrix.determinante_3x3([[1, 2], [3, 4]])

    # ── Identidad ────────────────────────────────────────────────────────────

    def test_identidad(self):
        # Test n=1
        assert self.matrix.identidad(1) == [[1]]

        # Test n=2
        assert self.matrix.identidad(2) == [[1, 0], [0, 1]]

        # Test n=3
        assert self.matrix.identidad(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        # Test n=4 (verificar solo dimensiones y diagonal)
        M = self.matrix.identidad(4)
        assert len(M) == 4
        assert all(M[i][i] == 1 for i in range(4))
        assert all(M[i][j] == 0 for i in range(4) for j in range(4) if i != j)

    # ── Diagonal ─────────────────────────────────────────────────────────────

    def test_diagonal(self):
        # Test con matriz 3x3
        assert self.matrix.diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 5, 9]

        # Test con matriz 2x2
        assert self.matrix.diagonal([[3, 0], [0, 7]]) == [3, 7]

        # Test con matriz 1x1
        assert self.matrix.diagonal([[42]]) == [42]

        # Test con matriz no cuadrada (debe lanzar ValueError)
        with pytest.raises(ValueError):
            self.matrix.diagonal([[1, 2, 3], [4, 5, 6]])

    # ── Es diagonal ──────────────────────────────────────────────────────────

    def test_es_diagonal(self):
        # Test con matriz diagonal 2x2
        assert self.matrix.es_diagonal([[3, 0], [0, 7]]) == True

        # Test con matriz diagonal 3x3
        assert self.matrix.es_diagonal([[1, 0, 0], [0, 5, 0], [0, 0, 9]]) == True

        # Test con matriz no diagonal
        assert self.matrix.es_diagonal([[1, 2], [0, 4]]) == False

        # Test con matriz identidad (es diagonal)
        assert self.matrix.es_diagonal([[1, 0], [0, 1]]) == True

        # Test con matriz 1x1 (siempre diagonal)
        assert self.matrix.es_diagonal([[5]]) == True

    # ── Rotar 90 grados ──────────────────────────────────────────────────────

    def test_rotar_90(self):
        # Test con matriz 2x2
        assert self.matrix.rotar_90([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]

        # Test con matriz 3x3
        M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert self.matrix.rotar_90(M) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

        # Test con matriz 1x1 (sin cambio)
        assert self.matrix.rotar_90([[5]]) == [[5]]

        # Test con matriz rectangular 2x3
        M2 = [[1, 2, 3], [4, 5, 6]]
        assert self.matrix.rotar_90(M2) == [[4, 1], [5, 2], [6, 3]]

    # ── Buscar en matriz ─────────────────────────────────────────────────────

    def test_buscar_en_matriz(self):
        # Test con valor presente múltiples veces
        M = [[1, 2, 3], [4, 2, 6], [7, 8, 2]]
        assert self.matrix.buscar_en_matriz(M, 2) == [(0, 1), (1, 1), (2, 2)]

        # Test con valor presente una sola vez
        assert self.matrix.buscar_en_matriz([[1, 2], [3, 4]], 3) == [(1, 0)]

        # Test con valor no presente (lista vacía)
        assert self.matrix.buscar_en_matriz([[1, 2], [3, 4]], 9) == []

        # Test con valor en la primera celda
        assert self.matrix.buscar_en_matriz([[5, 1], [2, 3]], 5) == [(0, 0)]

        # Test con matriz vacía
        assert self.matrix.buscar_en_matriz([], 1) == []
