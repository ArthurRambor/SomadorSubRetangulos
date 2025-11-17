def iniciaMemo(i, j, mat, memo):
    """
    Constroi recursivamente memo[i][j] usando top-down + memoizacao.
    Usamos None para indicar que ainda não foi calculado.
    """
    if memo[i][j] is not None:
        return memo[i][j]
    
    # soma de mat[i][j] com os prefixos vizinhos (se existirem)
    total = mat[i][j]
    if i > 0:
        total += iniciaMemo(i - 1, j, mat, memo)
    if j > 0:
        total += iniciaMemo(i, j - 1, mat, memo)
    if i > 0 and j > 0:
        total -= iniciaMemo(i - 1, j - 1, mat, memo)

    memo[i][j] = total  # salva o valor calculado
    return total


def somaRect(r1, c1, r2, c2, memo):
    res = memo[r2][c2]
    if r1 > 0:
        res -= memo[r1 - 1][c2]
    if c1 > 0:
        res -= memo[r2][c1 - 1]
    if r1 > 0 and c1 > 0:
        res += memo[r1 - 1][c1 - 1]
    return res


def subretanguloMaxSoma(mat):
    n = len(mat)
    # Inicializa memo com None, para checagem de cálculo
    memo = [[None] * n for _ in range(n)]

    # Constrói todos os prefixos usando top-down
    for i in range(n):
        for j in range(n):
            iniciaMemo(i, j, mat, memo)

    # Agora percorre todos os sub-retângulos possíveis
    melhorSoma = -9999
    for r1 in range(n):
        for c1 in range(n):
            for r2 in range(r1, n):
                for c2 in range(c1, n):
                    s = somaRect(r1, c1, r2, c2, memo)
                    if s > melhorSoma:
                        melhorSoma = s
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

    ans = subretanguloMaxSoma(mat)
    print("Maior soma de sub-retângulo:", ans)


if __name__ == "__main__":
    main()
