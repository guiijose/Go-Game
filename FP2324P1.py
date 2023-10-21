# This is the Python script for your project
# projeto 1

def eh_territorio(arg):
    """
    Esta função recebe um argumento e verifica se é um território válido.
    """
    if type(arg) is not tuple or not 0 < len(arg) < 27:
        return False
    try:
        altura = len(arg[0])
    except TypeError:
        return False
        
    for coluna in arg:
        if (type(coluna) is not tuple or not 0 < len(coluna) < 100
            or len(coluna) != altura):
            return False
        for coordenada in coluna:
            if type(coordenada) is not int or coordenada not in (0, 1):
                return False
    return True

def obtem_ultima_intersecao(t):
    """
    Esta função recebe um território e devolve a última interseção.
    """
    if not eh_territorio(t): # verificar se o território é válido
        return False
    # devolver a última coordenada
    return (chr(len(t) + 64), len(t[0]))

def eh_intersecao(arg):
    """
    Esta função recebe um argumento e verifica se é uma interseção válida,
    ou seja, se é um tuplo com dois elementos, sendo o primeiro uma letra 
    maiúscula e o segundo um número entre 1 e 99.
    """
    if not isinstance(arg, tuple): # verificar se o argumento é um tuplo
        return False
    if (len(arg) != 2 or not isinstance(arg[0], str) # verifica se as outras condições são válidas
        or not isinstance(arg[1], int) or not arg[0].isupper() 
        or not 1 <= arg[1] <= 99 or len(arg[0]) != 1):
        return False
    
    return True

def eh_intersecao_valida(t, i):
    """
    Esta função recebe um território e uma interseção e verifica se a 
    interseção pode pertencer ao território.
    """
    # verificar se o território e a interseção são válidos
    if not eh_territorio(t) or not eh_intersecao(i): 
        return False
    
    # Verificar se interseção não ultrapassa limites do território
    if ord(i[0]) - 64 > len(t) or i[1] > len(t[0]):
        return False
    
    return True

def eh_intersecao_livre(t, i):
    """
    Esta função recebe um território e uma interseção e verifica se a 
    interseção tem valor de 0 (se é livre), devolvendo um booleano.
    """
    # verificar se o território e a interseção são compatíveis
    if not eh_intersecao_valida(t, i):
        return False
    # verificar se a coordenada corresponde a um 0 ou 1
    return t[ord(i[0]) - 65][i[1] - 1] == 0

def obtem_intersecoes_adjacentes(t, i):
    """
    Esta funcão recebe um território e uma interseção e devolve um tuplo com as
    interseções adjacentes à interseção dada.
    """
    if not eh_intersecao_valida(t, i): # verificar se a interseção é válida
        return False
    adjacentes = ()
    # verificar as 4 possíveis interseções adjacentes
    if eh_intersecao_valida(t, (i[0], i[1] - 1)):
        adjacentes = adjacentes + (((i[0], i[1] - 1)),)

    if eh_intersecao_valida(t, (chr(ord(i[0]) - 1), i[1])):
        adjacentes += (((chr(ord(i[0]) - 1), i[1]),))
        
    if eh_intersecao_valida(t, (chr(ord(i[0]) + 1), i[1])):
        adjacentes += (((chr(ord(i[0]) + 1), i[1]),))

    if eh_intersecao_valida(t, (i[0], i[1] + 1)):
        adjacentes += (((i[0], i[1] + 1)),)

    return adjacentes

def ordena_intersecoes(arg):
    """
    Esta função rebe um tuplo com interseções e devolve um tuplo com as 
    intersesções ordenadas.
    """
    if type(arg) is not tuple: # verifica se o argumento é um tuplo
        return False
    for item in arg: # itera sobre as interseções para verificar se são válidas
        if type(item) is not tuple and not eh_intersecao(item):
            raise ValueError('argumentos inválidos')
    # ordena as interseções, usando um lambda para dar prioridade à letra,
    # ou seja, ao segundo elemento do tuplo da interseção
    return tuple(sorted(arg, key=lambda x: (x[1], x[0])))

def territorio_para_str(t):
    """
    Esta função recebe um território e devolve uma string com a representação 
    desse mesmo território.
    """
    if not eh_territorio(t): # verificar se o território é válido
        raise ValueError('territorio_para_str: argumento invalido')
    
    def digits(num): # função auxiliar que conta o número de dígitos de um número
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
    """
    Esta função recebe um território e uma interseção e devolve um tuplo com 
    as interseções que estão ligadas a essa interseção por interseções com 
    o mesmo estado de ocupação.
    """
    if not eh_intersecao_valida(t, i): # verificar se os argumentos são válidos
        raise ValueError('obtem_cadeia: argumentos invalidos')
    
    # Função para obter interseções adjacentes com mesmo estado de ocupação
    def adjacentes_tipo(t, i): 
        adjacentes = obtem_intersecoes_adjacentes(t, i)
        adjacentes_livres = tuple(adjacente for adjacente in adjacentes 
                                  if eh_intersecao_livre(t, adjacente) == 
                                  eh_intersecao_livre(t, i))
        
        return adjacentes_livres
    
    cadeia = adjacentes_tipo(t, i) + (i,) 

    adicionado = True
    while adicionado: # itera até não ser possível adicionar mais interseções
        adicionado = False
        novos_adjacentes = ()

        for adjacente in cadeia: # itera sobre as interseções da cadeia

            # cria um tuplo com as interseções adjacentes que ainda não estão 
            # na cadeia nem no tuplo novos_adjacentes para evitar repetições
            aux = tuple(adj for adj in adjacentes_tipo(t, adjacente) 
                        if adj not in cadeia and adj not in novos_adjacentes)
            novos_adjacentes += aux

            if aux: # define o valor de adicionado se o tuplo aux não for vazio
                adicionado = True

        cadeia += novos_adjacentes

    return ordena_intersecoes(cadeia)

def obtem_vale(t, i):
    """
    Esta função recebe um território e uma interseção ocupada por uma montanha 
    e devolve um tuplo com as interseções vazias adjacentes às montanhas que
    pertencem à cadeia da interseção dada.
    """
    # verificar se os argumentos são válidos
    if not eh_intersecao_valida(t, i) or eh_intersecao_livre(t, i):
        raise ValueError("obtem_vale: argumentos invalidos")
    
    # Função para obter interseções adjacentes com estado de ocupação diferente
    def adjacentes_tipo_diferente(t, i):
        adjacentes = obtem_intersecoes_adjacentes(t, i)
        adjacentes_diferente = tuple(adjacente for adjacente in adjacentes 
                                     if eh_intersecao_livre(t, adjacente) != 
                                     eh_intersecao_livre(t, i))
        return adjacentes_diferente


    cadeia = obtem_cadeia(t, i)
    vales = ()
    for montanha in cadeia: # itera sobre as interseções da cadeia
        # adiciona as interseções adjacentes com o estado de ocupação diferente
        vales += tuple(vale for vale in adjacentes_tipo_diferente(t, montanha) 
                       if vale not in vales)

    return ordena_intersecoes(vales)

def verifica_conexao(t, i1, i2):
    """
    Esta função recebe um território e duas interseçõese e verifica se as
    interseções pertencem à mesma cadei, devolvendo um booleano.
    """
    # verificar se os argumentos são válidos
    if not eh_intersecao_valida(t, i1) or not eh_intersecao_valida(t, i2):
        raise ValueError('verifica_conexao: argumentos invalidos')

    # verificar se as interseções pertencem à mesma cadeia
    return i1 in obtem_cadeia(t, i2)

def calcula_numero_montanhas(t):
    """
    Esta função recebe um território e devolve um inteiro com o número de
    montanhas existentes no território.
    """
    # verificar se o argumento é válido
    if not eh_territorio(t):
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    
    contador = 0
    for coluna in t: # itera pelas colunas do território e conta o número de 1s
        contador += coluna.count(1)

    return contador

def calcula_numero_cadeias_montanhas(t):
    """
    Esta função recebe um território e devolve um inteiro com o número de
    cadeias diferentes de montanhas existentes no território.
    """
    # verificar se o argumento é válido
    if not eh_territorio(t):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    cadeias = ()
    contador = 0
    # vai adicionando as cadeias de montanhas ao tuplo cadeias e conta o número
    # de vezes que isso acontece

    for y in range(len(t[0])):
        for x in range(len(t)):
            if t[x][y] == 1 and (chr(65 + x), y + 1) not in cadeias:
                cadeias += obtem_cadeia(t, (chr(65 + x), y + 1))
                contador += 1
    return contador

def calcula_tamanho_vales(t):
    """
    Esta função recebe um território e devolve um inteiro correspondente
    ao número de interseções vazias que pertencem a vales.
    """
    if not eh_territorio(t):
        raise ValueError( 'calcula_tamanho_vales: argumento invalido')
    vales = ()
    # itera sobre as interseções do território e adiciona as interseções vazias
    for y in range(len(t[0])):
        for x in range(len(t)):
            if not eh_intersecao_livre(t, (chr(65 + x), y + 1)):
                novo_vale = obtem_vale(t, (chr(65 + x), y + 1))
                vales += tuple(vale for vale in novo_vale if vale not in vales)
    # devolve o número de interseções vazias que pertencem a vales
    return len(vales)

