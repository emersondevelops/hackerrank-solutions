s = 'aba'
n = 10


def repeatedString(s, n):

    vezes_pedaco_inteiro = n//len(s)
    a_vezes_pedaco_inteiro = vezes_pedaco_inteiro * s.count('a')

    tamanho_resto = n % len(s)
    a_tamanho_resto = s[0:tamanho_resto].count('a')

    return a_vezes_pedaco_inteiro + a_tamanho_resto


print(repeatedString(s, n))
