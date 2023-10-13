# This is the Python script for your project
# projeto 1


# função que devolve o número de digitos de um número
def digits(num):
    if type(num) is not int:
        raise ValueError('argumento inválido')
    digitos = 0
    while num != 0:
        digitos += 1
        num //= 10
    return digitos


def eh_territorio(arg):
    # verificar se o argumento (território) é um tuplo e se o tuplo não é vazio
    if type(arg) is not tuple or len(arg) == 0:
        return False
    # verificar se dentro de um tuplo os argumentos são tuplos e se sim, se não são vazios e se têm o mesmo tamanho 
    # de seguida verificamos se dentro dos tuplos se os argumentos são 0 ou 1
    altura = len(arg[0])
    for coluna in arg:
        if type(coluna) is not tuple or len(coluna) == 0 or len(coluna) != altura:
            return False
        for coordenada in coluna:
            if coordenada != 0 and coordenada != 1:
                return False
    return True

def obtem_ultima_intersecao(t):
    # verificar se o território é falso
    if not eh_territorio(t):
        raise ValueError('argumento inválido')
    # devolver a última coordenada
    return (chr(len(t) + 64), len(t[0]))

def eh_intersecao(arg):
    # verificar se o argumento (interseção é um tuplo)
    if not isinstance(arg, tuple):
        raise ValueError('argumento inválido')
    # verificar se dentro do tuplo o primeiro argumento é uma letra maiúscula e se o segundo é um inteiro entre 1 e 99
    if len(arg) != 2 or not isinstance(arg[0], str) or not isinstance(arg[1], int) or not arg[0].isupper() or not 1 <= arg[1] <= 99:
        return False
    return True

def eh_intersecao_valida(t, i):
    # verificr se ambos os argumentos (território e interseção são válidos)
    if not eh_territorio(t) or not eh_intersecao(i):
        return False
    # verificar se as coordenadas da interseção não excedem os limites do território
    if ord(i[0]) - 64 > len(t) or i[1] > len(t[0]):
        return False
    return True

def eh_intersecao_livre(t, i):
    # verificar se o território e a interseção são compatíveis
    if not eh_intersecao_valida(t, i):
        raise ValueError('parâmetros inválidos')
    # verificar se a coordenada corresponde a um 0 ou 1
    if t[ord(i[0]) - 65][i[1] - 1] == 1:
        return False
    else:
        return True

def obtem_intersecoes_adjacentes(t, i):
    # vericar se o território e a interseção são compatíveis
    if not eh_intersecao_valida(t, i):
        raise ValueError
    # criar um tuplo das coordenadas adjacentes e verificar as 4 possíveis coordenadas adjacentes
    # se a coordenada adjacente for válida, adicionamos ao tuplo
    adjacentes = ()
    if eh_intersecao_valida(t, (i[0], i[1] - 1)):
        adjacentes += (((i[0], i[1] - 1)),)
    if eh_intersecao_valida(t, (chr(ord(i[0]) - 1), i[1])):
        adjacentes += (((chr(ord(i[0]) - 1), i[1]),))
    if eh_intersecao_valida(t, (chr(ord(i[0]) + 1), i[1])):
        adjacentes += (((chr(ord(i[0]) + 1), i[1]),))
    if eh_intersecao_valida(t, (i[0], i[1] + 1)):
        adjacentes += (((i[0], i[1] + 1)),)
    return adjacentes

def ordena_intersecoes(arg):
    # verificar se o argumento é um tuplo
    if type(arg) is not tuple:
        raise ValueError('argumentos inválidos')
    # verificar se cada tuplo é uma interseção
    for item in arg:
        if type(item) is not tuple and not eh_intersecao(item):
            raise ValueError('argumentos inválidos')
    # através de um lambda, trocamos os elementos de um tuplo para a função sorted considerar a altura a coordenada prioritária para ordenar
    # a função sorted devolve uma lista, por isso usamos a funçã tuple para a converter num tuplo
    return tuple(sorted(arg, key=lambda x: (x[1], x[0])))


def territorio_para_str(t):
    if not eh_territorio:
        raise ValueError('território não válido')
    altura = len(t[0])
    largura = len(t)
    territorio = "  "
    for i in range(largura):
        territorio += f" {chr(65 + i)}"
    territorio += '\n'

    for j in range(altura):
        territorio = territorio + (2 - digits(altura - j)) * " " + f"{altura - j} " 
        for x in range(largura):
            intersecao = '. ' if t[x][altura - j - 1] == 0 else 'X '
            territorio += intersecao
        territorio = territorio + (2 - digits(altura - j)) * " " + f"{altura - j}\n" 
    territorio += "  "
    for i in range(largura):
        territorio += f" {chr(65 + i)}"
    return territorio

t = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
t2 = '   A B C D E\n 4 . . . . .  4\n 3 . . X . .  3\n 2 X . . . .  2\n 1 . . . X .  1\n   A B C D E'
print(territorio_para_str(t))
print(t2)

def obtem_cadeia():
    pass

def obtem_vale():
    pass

def verifica_conexao():
    pass

def calcula_numero_montanhas():
    pass

def calcula_numero_cadeias_montanhas():
    pass

def calcula_tamanho_vales():
    pass


"""
def territorio_para_str(t):
    if not eh_territorio(t):
        raise ValueError('argumento não válido')
    max_digits = digits(len(t[0]))
    territorio = '   ' + (2 - max_digits) * ' '
    # primeira linha de letras
    for j in range(len(t)):
        if j == len(t) - 1:
            territorio += f'{chr(65 + j)}\n'
        else:
            territorio += f'{chr(65 + j)} '
    # loop por cada uma das linhas
    for i in range(len(t[0])):
        number = len(t[0]) - i

        territorio = territorio + (f' {number} ') + (max_digits - digits(number)) * ' '
        for x in range(len(t)):
            if t[x][len(t[0]) - i - 1] == 1 :
                territorio += 'X '
            elif t[x][len(t[0]) - i - 1] == 0:
                territorio += '. '
        territorio += f' {number}\n'
    territorio = territorio + '   ' + (2 - x) * ' '
    for j in range(len(t)):
        if j == len(t) - 1:
            territorio += f'{chr(65 + j)}'
        else:
            territorio += f'{chr(65 + j)} '


    return territorio


    t=((1,1,1,0,0,0,0,0,1,1),)
    t2 = '   A\n10 X 10\n 9 X  9\n 8 .  8\n 7 .  7\n 6 .  6\n 5 .  5\n 4 .  4\n 3 X  3\n 2 X  2\n 1 X  1\n   A'
    print(territorio_para_str(t))
    print(t2)

"""