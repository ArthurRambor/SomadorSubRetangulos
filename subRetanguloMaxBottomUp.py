def somaSubretanguloMax(mat):
    n = len(mat)
    table = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            total = mat[i][j]
            if i > 0:
                total += table[i-1][j]
            if j > 0:
                total += table[i][j-1]
            if i > 0 and j > 0:
                total -= table[i-1][j-1]
            table[i][j] = total
    melhorSoma = -9999
    for r1 in range(n):
        for c1 in range(n):
            for r2 in range(r1, n):
                for c2 in range(c1, n):
                    res = table[r2][c2]
                    if r1 > 0:
                        res -= table[r1-1][c2]
                    if c1 > 0:
                        res -= table[r2][c1-1]
                    if r1 > 0 and c1 > 0:
                        res += table[r1-1][c1-1]
                    if res > melhorSoma:
                        melhorSoma = res
    return melhorSoma

def main():
    n = int(input("Digite o tamanho N da matriz (NxN): "))
    print(f"Digite {n} linhas com {n} números separados por espaço:")
    mat = []
    for _ in range(n):
        linha = list(map(int, input().split()))
        if len(linha) != n:
            print("Por favor, digite exatamente", n, "números!")
            return
        mat.append(linha)

    ans = somaSubretanguloMax(mat)
    print("Maior soma de sub-retângulo:", ans)

if __name__ == "__main__":
    main()
