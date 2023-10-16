# This is the Python script for your project
# projeto 1

def eh_territorio(arg): # assert not true (já coloquei que as coordenadas não podem ser floats)
    if type(arg) is not tuple or not 0 < len(arg) < 27:
        return False
    try:
        altura = len(arg[0])
    except TypeError:
        return False
        
    for coluna in arg:
        if type(coluna) is not tuple or not 0 < len(coluna) < 100  or len(coluna) != altura:
            return False
        for coordenada in coluna:
            if type(coordenada) is not int or coordenada not in (0, 1):
                return False
    return True

def obtem_ultima_intersecao(t):
    # verificar se o território é falso
    if not eh_territorio(t):
        return False
    # devolver a última coordenada
    return (chr(len(t) + 64), len(t[0]))

def eh_intersecao(arg):
    if not isinstance(arg, tuple):
        return False
    if len(arg) != 2 or not isinstance(arg[0], str) or not isinstance(arg[1], int) or not arg[0].isupper() or not 1 <= arg[1] <= 99 or len(arg[0]) != 1:
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
        return False
    # verificar se a coordenada corresponde a um 0 ou 1
    if t[ord(i[0]) - 65][i[1] - 1] == 1:
        return False
    else:
        return True

def obtem_intersecoes_adjacentes(t, i):
    # vericar se o território e a interseção são compatíveis
    if not eh_intersecao_valida(t, i):
        return False
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
        return False
    # verificar se cada tuplo é uma interseção
    for item in arg:
        if type(item) is not tuple and not eh_intersecao(item):
            raise ValueError('argumentos inválidos')
    # através de um lambda, trocamos os elementos de um tuplo para a função sorted considerar a altura a coordenada prioritária para ordenar
    # a função sorted devolve uma lista, por isso usamos a funçã tuple para a converter num tuplo
    return tuple(sorted(arg, key=lambda x: (x[1], x[0])))

def territorio_para_str(t):
    if not eh_territorio(t):
        raise ValueError('territorio_para_str: argumento invalido')
    
    def digits(num):
        if type(num) is not int:
            raise ValueError('argumento inválido')
        digitos = 0
        while num != 0:
            digitos += 1
            num //= 10
        return digitos
    
    altura = len(t[0])
    largura = len(t)
    territorio = "  "
    for i in range(largura): # adiciona primeira linha com as letras
        territorio += f" {chr(65 + i)}"
    territorio += '\n'

    for j in range(altura): # itera por n linhas sendo n o valor da altura
        territorio = territorio + (2 - digits(altura - j)) * " " + f"{altura - j} " 
        for x in range(largura): # iteram por n colunas sendo n o valor da largura
            intersecao = '. ' if t[x][altura - j - 1] == 0 else 'X '
            territorio += intersecao
        territorio = territorio + (2 - digits(altura - j)) * " " + f"{altura - j}\n" 
    territorio += "  "
    for i in range(largura): # adiciona a ulitma linha com as letras
        territorio += f" {chr(65 + i)}"
    return territorio

def obtem_cadeia(t, i): 
    if not eh_intersecao_valida(t, i):
        raise ValueError('obtem_cadeia: argumentos invalidos')
    
    def adjacentes_tipo(t, i): 
        adjacentes = obtem_intersecoes_adjacentes(t, i)
        adjacentes_livres = ()
        for adjacente in adjacentes:
            if eh_intersecao_livre(t, i):
                if eh_intersecao_livre(t, adjacente):
                    adjacentes_livres += (adjacente,)
            else:
                if not eh_intersecao_livre(t, adjacente):
                    adjacentes_livres += (adjacente,)

        return adjacentes_livres
    
    cadeia = adjacentes_tipo(t, i) + (i,)
    iterador = list(cadeia)
    adicionado = True

    while adicionado:
        adicionado = False
        novos_adjacentes = []
        
        for intersecao in iterador:
            novas_intersecoes = adjacentes_tipo(t, intersecao)
            for adjacente in novas_intersecoes:
                if adjacente not in cadeia and adjacente not in novos_adjacentes:
                    novos_adjacentes.append(adjacente)
                    adicionado = True
        
        for novo_adjacente in novos_adjacentes:
            cadeia += (novo_adjacente,)
            iterador.append(novo_adjacente)
    
    return ordena_intersecoes(cadeia)

def obtem_vale(t, i):
    if not eh_intersecao_valida(t, i) or eh_intersecao_livre(t, i):
        raise ValueError("obtem_vale: argumentos invalidos")
    
    def adjacentes_tipo_diferente(t, i):
        adjacentes = obtem_intersecoes_adjacentes(t, i)
        adjacentes_diferentes = ()
        for adjacente in adjacentes:
            if eh_intersecao_livre(t, i):
                if not eh_intersecao_livre(t, adjacente):
                    adjacentes_diferentes += (adjacente,)
            else:
                if eh_intersecao_livre(t, adjacente):
                    adjacentes_diferentes += (adjacente,)

        return adjacentes_diferentes


    cadeia = obtem_cadeia(t, i)
    vales = ()
    for montanha in cadeia:
        for vale in adjacentes_tipo_diferente(t, montanha):
            if vale not in vales:
                vales += (vale,)
    return ordena_intersecoes(vales)

def verifica_conexao(t, i1, i2):
    if not eh_intersecao_valida(t, i1) or not eh_intersecao_valida(t, i2):
        raise ValueError('verifica_conexao: argumentos invalidos')
    if i1 in obtem_cadeia(t, i2):
        return True
    return False

def calcula_numero_montanhas(t):
    if not eh_territorio(t):
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    contador = 0
    for y in range(len(t[0])):
        for x in range(len(t)):
            if t[x][y] == 1:
                contador += 1
    return contador

def calcula_numero_cadeias_montanhas(t):
    if not eh_territorio(t):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    cadeias = ()
    for y in range(len(t[0])):
        for x in range(len(t)):
            if t[x][y] == 1 and obtem_cadeia(t, (chr(65 + x), y + 1)) not in cadeias:
                cadeias += (obtem_cadeia(t, (chr(65 + x), y + 1)),)
    return len(cadeias)

def calcula_tamanho_vales(t):
    if not eh_territorio(t):
        raise ValueError( 'calcula_tamanho_vales: argumento invalido')
    vales = ()
    for y in range(len(t[0])):
        for x in range(len(t)):
            if not eh_intersecao_livre(t, (chr(65 + x), y + 1)):
                novo_vale = obtem_vale(t, (chr(65 + x), y + 1))
                for vale in novo_vale:
                    if vale not in vales:
                        vales += (vale, )

    return len(vales)
