class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        def somar_diagonal(matriz):
            soma = 0
            n = len(matriz)
            # diagonal primária
            for i in range(n):
                soma += matriz[i][i]
                

            # diagonal secundária
            for i in range(n):
                if n % 2 != 0 and i == n // 2:
                    soma += 0
                else:
                    soma += matriz[i][(n - 1) - i]

            return soma

        for linha in mat:
            print(linha)
        return somar_diagonal(mat)
