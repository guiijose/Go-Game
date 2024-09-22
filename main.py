LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# TAD INTERSEÇÃO 
def cria_intersecao(col, lin):
    """
    Cria uma interseção com as coordenadas (col, lin).

    Args:
        col (int): A coordenada da coluna da interseção.
        lin (int): A coordenada da linha da interseção.

    Returns:
        tuple: Uma tuplo com as coordenadas (col, lin) da interseção.

    Raises:
        ValueError: Se as coordenadas não formarem uma interseção válida.
    """
    if not eh_intersecao((col, lin)):
        raise ValueError("cria_intersecao: argumentos invalidos")
    return (col, lin)

def eh_intersecao(i):
    """
    Verifica se o argumento é uma interseção válida.

    Args:
        i (tuple): Uma tuplo de dois elementos que representam as 
        coordenadas (linha, coluna) da interseção.

    Returns:
        bool: True se a interseção é válida, False caso contrário.
    """
    if (type(i) != tuple or len(i) != 2 or type(i[0]) != str 
        or type(i[1]) != int or len(i[0]) != 1):
        return False
    return 65 <= ord(i[0]) <= 83 and 1 <= i[1] <= 19

def eh_intersecao_valida(goban, intersecao):
    """
    Determina se uma dada interseção é válida no tabuleiro passado como 
    argumento.

    Args:
        goban (list): O estado atual do tabuleiro.
        intersecao (tuple): As coordenadas da interseção a ser verificada.

    Returns:
        bool: True se a interseção pode corresponder ao tabuleiro, 
        False caso contrário.
    """
    if not eh_intersecao(intersecao):
        return False
    maior_col = obtem_col(obtem_ultima_intersecao(goban))
    maior_lin = obtem_lin(obtem_ultima_intersecao(goban))
    # verifica se as coordenadas não excedem o tamanho do tabuleiro
    return ("A" <= obtem_col(intersecao) <= maior_col and 
            1 <= obtem_lin(intersecao) <= maior_lin)

def obtem_col(i):
    """
    Devolve a coluna da interseção.

    Args: 
        i (tuple): A interseção.

    Returns:
        str: A coluna da interseção.
    """
    return i[0]

def obtem_lin(i):
    """
    Devolve a linha da interseção.

    Args: 
        i (tuple): A interseção.

    Returns:
        int: A linha da interseção.
    """
    return i[1]

def intersecoes_iguais(i1, i2):
    """
    Verifica se duas interseções são iguais.
    
    Args:
        i1 (tuple): Uma interseção.
        i2 (tuple): Outra interseção.
    
    Returns:
        bool: True se as interseções são iguais, False caso contrário.
    
    Raises:
        ValueError: Se algum dos argumentos não for uma interseção.
    """
    # valida os argumentos
    if not eh_intersecao(i1) or not eh_intersecao(i2):
        raise ValueError("intersecoes_iguais: argumentos invalidos")
    # verifica a igualdade das coordenadas
    return obtem_col(i1) == obtem_col(i2) and obtem_lin(i1) == obtem_lin(i2)

def intersecao_para_str(i):
    """
    Devolve uma string que representa a interseção i.
    
    Args:
        i (tuple): Uma tuplo que representa uma interseção.
    
    Returns:
        str: Uma string que representa a interseção i.
    """
    return f"{i[0]}{str(i[1])}"

def str_para_intersecao(i):
    """
    Devolve uma interseção a partir de uma string.
    
    Args:
        i (str): Uma string que representa uma interseção.
        
    Returns:
        tuple: Uma interseção.
    
    Raises:
        ValueError: Se a string não representar uma interseção."""
    
    # valida os argumentos
    if (type(i) != str or len(i) not in (2, 3) 
        or not eh_intersecao(cria_intersecao(i[0], int(i[1])))):
        raise ValueError("str_para_intersecao: argumento invalido")
    
    return cria_intersecao(i[0], int(i[1:]))

# FUNÇÕES DE ALTO NÍVEL (INTERSEÇÃO)

def ordena_intersecoes(intersecoes):
    """
    Ordena as interseções dando prioridade à linha.

    Args:
        intersecoes (tuple): Um tuplo feito pelas interseções a 
        serem ordenadas.

    Returns:
        tuple: Um tuplo que contem as interseções ordenadas.
    """
    return tuple(sorted(intersecoes, key=lambda i: (obtem_lin(i), obtem_col(i))))

def obtem_intersecoes_adjacentes(i, l):
    """
    Devolve as interseções adjacentes à interseção i.

    Args:
        i (tuple): Uma interseção.
        l (tuple): A última interseção do tabuleiro.
    
    Returns:
        tuple: Um tuplo com as interseções adjacentes a i.
    
    Raises:
        ValueError: Se algum dos argumentos não for uma interseção.
    """
    # valida os argumentos
    if (l not in (cria_intersecao("S", 19), cria_intersecao("M", 13), 
                  cria_intersecao("I", 9))):
        raise ValueError("obtem_intersecoes_adjacentes: argumentos invalidos")
    elif not eh_intersecao(i):
        raise ValueError("obtem_intersecoes_adjacentes: argumentos invalidos")
    
    adjacentes = tuple()
    # verifica os 4 possíveis adjacentes
    if obtem_col(i) != "A":
        adjacentes += (cria_intersecao(chr(ord(obtem_col(i)) - 1), 
                        obtem_lin(i)),)
        
    if obtem_lin(i) != obtem_lin(l):
        adjacentes += (cria_intersecao(obtem_col(i), 
                        obtem_lin(i) + 1),)
        
    if obtem_col(i) != obtem_col(l):
        adjacentes += (cria_intersecao(chr(ord(obtem_col(i)) + 1), 
                        obtem_lin(i)),)
        
    if obtem_lin(i) != 1:
        adjacentes += (cria_intersecao(obtem_col(i), 
                        obtem_lin(i) - 1),)
    return ordena_intersecoes(adjacentes)

# TAD PEDRA

def cria_pedra_branca():
    """
    Devolve uma pedra branca.

    Returns:
        str: Uma string que representa uma pedra branca.
    """
    return 'O'

def cria_pedra_preta():
    """
    Devolve uma pedra preta.

    Returns:
        str: Uma string que representa uma pedra preta.
    """
    return 'X'

def cria_pedra_neutra():
    """
    Devolve uma pedra neutra.

    Returns:
        str: Uma string que representa uma pedra neutra.
    """
    return '.'

def pedras_iguais(p1, p2):
    """
    Verifica se duas pedras são iguais.

    Args:
        p1 (str): Uma pedra.
        p2 (str): Outra pedra.

    Returns:
        bool: True se as pedras forem iguais, False caso contrário.
    """
    return pedra_para_str(p1) == pedra_para_str(p2)

def eh_pedra(p):
    """
    Verifica se um caracter é uma pedra ou não.

    Args:
        p (str): Caracter a ser verificado.

    Returns:
        bool: True se o caracter é uma pedra ('O', 'X', '.'), False caso contrário.
    """
    return p in ('O', 'X', '.')

def eh_pedra_branca(p):
    """
    Verifica se a pedra passada como argumento é branca.
    
    Args:
        p (str): posição do tabuleiro a ser verificada
    
    Returns:
        bool: True se a posição for uma pedra branca, False caso contrário
    """
    return p == 'O'

def eh_pedra_preta(p):
    """
    Verifica se a pedra é preta.

    Args:
        p (str): a pedra a ser verificada.

    Returns:
        bool: True se a pedra for preta, False caso contrário.
    """
    return p == 'X'

def pedra_para_str(p):
    """
    Converte uma pedra para uma string que a representa.

    Args:
        p (str): Uma pedra.
    
    Returns:
        str: Uma string que representa a pedra.
    
    Raises:
        ValueError: Se o argumento não for uma pedra.
    """
    if not eh_pedra(p):
        raise ValueError("pedra_para_str: argumento invalido")
    if eh_pedra_branca(p):
        return "O"
    elif eh_pedra_preta(p):
        return "X"
    else:
        return "."

# FUNÇÕES DE ALTO NÍVEL (PEDRA)

def eh_pedra_jogador(p): 
    """
    Verifica se a peça é uma pedra branca ou preta.
    
    Args:
    p (str): A peça a ser verificada.
    
    Returns:
    bool: True se a peça é uma pedra branca ou preta, False caso contrário.
    """
    return eh_pedra_branca(p) or eh_pedra_preta(p)

# TAD GOBAN

def cria_goban_vazio(length):
    """
    Cria um tabuleiro de jogo vazio com o tamanho passado como argumento.

    Args:
        length (int): O tamanho do tabuleiro. Deve ser 9, 13 ou 19.

    Returns:
        list: Uma lista de listas que representa o tabuleiro vazio.

    Raises:
        ValueError: Se o argumento passado não for um inteiro ou não for um dos
        valores permitidos.
    """

    # valida o argumento
    if length not in (9, 13, 19) or type(length) != int:
        raise ValueError("cria_goban_vazio: argumento invalido")
    
    return [[cria_pedra_neutra() for i in range(length)] for j in range(length)]

def cria_goban(length, brancas, pretas):
    """
    Cria um goban com o comprimento especificado e as interseções brancas e 
    pretas especificadas.

    Args:
        length (int): comprimento do goban (9, 13 ou 19)
        brancas (tuple): tuplo com as interseções brancas no 
        formato (letra, número) 
        pretas (tuple): tuplo com as 
        interseções pretas no formato (letra, número)

    Returns:
        list: uma lista de listas representando o goban criado

    Raises:
        ValueError: se algum dos argumentos for inválido ou se as interseções 
        brancas e pretas se sobrepõem
    """

    # valida o comprimento e o tipo dos outros argumentos
    if type(length) != int or (length not in (9, 13, 19) or 
        type(brancas) != tuple or type(pretas) != tuple):
        raise ValueError("cria_goban: argumentos invalidos")
    
    # valida as interseções
    if not (all(eh_intersecao(i) for i in brancas) 
            and all(eh_intersecao(i) for i in pretas)):
        raise ValueError("cria_goban: argumentos invalidos")
    
    # verifica se não há interseções repetidas
    if not (len(brancas) == len(set(brancas)) 
            and len(pretas) == len(set(pretas))):
        raise ValueError("cria_goban: argumentos invalidos")
    
    # verifica se as brancas e pretas não têm interseções em comum
    if any(intersecao in brancas for intersecao in pretas):
        raise ValueError("cria_goban: argumentos invalidos")
    # verifica se nenhuma intersecaoe excede o tamanho do goban
    if any(obtem_col(i) not in LETRAS[:length] or not (1 <= obtem_lin(i) <= length) 
           for i in brancas + pretas):
        raise ValueError("cria_goban: argumentos invalidos")
    
    # cria goban verificando se as interseções estão nas tuplos passados como argumentos
    goban = [[cria_pedra_branca() if (chr(j + 65), i) in brancas 
              else cria_pedra_preta() if (chr(j + 65), i) in pretas 
              else cria_pedra_neutra() 
              for i in range(1, length + 1)] for j in range(length)]

    return goban

def cria_copia_goban(goban):
    """
    Cria uma cópia do goban.

    Args:
        goban (list): O goban a ser copiado.

    Returns:
        list: Uma cópia do goban.
    """
    tamanho = obtem_lin(obtem_ultima_intersecao(goban))
    brancas, pretas = tuple(), tuple()
    for x in LETRAS[:tamanho]:
        for y in range(1, tamanho + 1):
            intersecao = cria_intersecao(x, y)
            if eh_pedra_branca(obtem_pedra(goban, intersecao)):
                brancas += (intersecao,)
            elif eh_pedra_preta(obtem_pedra(goban, intersecao)):
                pretas += (intersecao,)

    return cria_goban(tamanho, brancas, pretas)


def obtem_ultima_intersecao(goban):
    """
    Devolve a última interseção do goban.

    Args:
        goban (list): lista de listas que representa o tabuleiro do jogo.

    Returns:
        tuple: um tuplo com a letra e o número da última interseção do goban.
    """
    return cria_intersecao(chr(64 + len(goban)), len(goban))

def obtem_pedra(goban, i):
    """
    Devolve a pedra na interseção especificada.

    Args:
        goban (list): Uma lista que representa o tabuleiro.
        i (tuple): Um tuplo que representa a interseção.

    Returns:
        str: Uma string que representa a pedra na interseção especificada.
    """
    return goban[ord(obtem_col(i)) - 65][obtem_lin(i) - 1]

def obtem_cadeia(goban, i):
    """
    Função que devolve a cadeia de interseções do mesmo tipo que contém a interseção i.

    Args:
        goban (list): Uma lista que representa o tabuleiro.
        i (tuple): Um tuplo que representa a interseção.

    Returns:
        tuple: Um tuplo com as interseções da cadeia ordenadas.
    
    Raises:
        ValueError: Se o goban ou a interseção não forem válidos.
    """

    # valida os argumentos
    if not (eh_goban(goban) and eh_intersecao(i) and 
            eh_intersecao_valida(goban, i)):
        raise ValueError('obtem_cadeia: argumentos invalidos')
    ocupacao = obtem_pedra(goban, i)
    cadeia, to_check = [], [i]

    # enquanto ha interseções a verificar continua a obter interseções
    while to_check:
        # retirar a interseção prestes a ser executada e coloca na cadeia
        pos = to_check.pop()
        cadeia.append(pos)
        
        # obtem as interseções adjacentes e adiciona às interseções a verificar
        adjacentes = obtem_intersecoes_adjacentes(pos, 
                    obtem_ultima_intersecao(goban))
        
        for new_pos in adjacentes:
            if (pedras_iguais(obtem_pedra(goban, new_pos), ocupacao) and 
                new_pos not in cadeia + to_check):
                to_check.append(new_pos)            

    return ordena_intersecoes(cadeia)

def eh_goban(goban):
    """
    Verifica se o argumento é um goban válido.

    Args:
        goban (list): Uma lista de listas representando o goban.

    Returns:
        bool: True se o argumento é um goban válido, False caso contrário.
    """
    # valida o tipo e comprimento do argumento
    if type(goban) != list or len(goban) not in (9, 13, 19):
        return False
    # valida o tipo e comprimento das linhas
    if all(type(linha) != list or len(linha) != len(goban) for linha in goban):
        return False
    # valida o tipo das pedras
    if any(not eh_pedra(pedra) for linha in goban for pedra in linha):
        return False
    return True



def gobans_iguais(g1, g2):
    """
    Verifica se dois gobans são iguais.

    Recebe dois gobans e retorna True se eles são iguais e False caso contrário.
    Dois gobans são iguais se possuem o mesmo tamanho, a mesma última interseção
    e as mesmas pedras nas mesmas interseções.

    Args:
        g1 (goban): O primeiro goban a ser comparado.
        g2 (goban): O segundo goban a ser comparado.

    Raises:
        ValueError: Se algum dos argumentos não for um goban válido.

    Returns:
        bool: True se os gobans são iguais, False caso contrário.
    """

    if not eh_goban(g1) or not eh_goban(g2):
        raise ValueError("gobans_iguais: argumentos invalidos")
    if obtem_ultima_intersecao(g1) != obtem_ultima_intersecao(g2):
        return False
    tamanho = obtem_lin(obtem_ultima_intersecao(g1))
    if tamanho != obtem_lin(obtem_ultima_intersecao(g2)):
        return False
    # itera pelas interseções e verifica a igualdade das pedras
    for i in LETRAS[:tamanho]:
        for j in range(1, tamanho + 1):
            intersecao = cria_intersecao(i, j)
            if not pedras_iguais(obtem_pedra(g1, intersecao), obtem_pedra(g2, intersecao)):
                return False
    return True

def coloca_pedra(goban, i, p):
    """
    Coloca uma pedra na interseção especificada do goban.

    Args:
        goban (list): O goban onde a pedra será colocada.
        i (str): A interseção onde a pedra será colocada.
        p (str): A pedra que será colocada na interseção.

    Raises:
        ValueError: Se os argumentos não forem válidos.

    Returns:
        list: O goban atualizado com a pedra colocada na interseção.
    """
    # valida os argumentos
    if not eh_goban(goban) or not eh_pedra(p) or not eh_intersecao_valida(goban, i):
        raise ValueError("coloca_pedra: argumentos invalidos")
    # coloca a pedra na interseção
    goban[ord(obtem_col(i)) - 65][obtem_lin(i) - 1] = p
    return goban

def remove_pedra(goban, i):
    """
    Remove uma pedra da interseção especificada no goban.

    Args:
        goban (list): O goban a ser modificado.
        i (str): A interseção da qual a pedra será removida.

    Raises:
        ValueError: Se o goban ou a interseção forem inválidos.

    Returns:
        list: O goban modificado.
    """
    # valida os argumentos
    if not eh_goban(goban) or not eh_intersecao_valida(goban, i):
        raise ValueError("remove_pedra: argumentos invalidos")
    # remove a pedra da interseção
    goban[ord(obtem_col(i)) - 65][obtem_lin(i) - 1] = pedra_para_str(cria_pedra_neutra())
    return goban

def remove_cadeia(goban, cadeia):
    """
    Remove a cadeia do goban.
    
    Args:
        goban (list): lista de listas que representa o tabuleiro.
        cadeia (list): lista de tuplos que representa as coordenadas das interseções da cadeia.
    
    Raises:
        ValueError: se o goban ou a cadeia forem inválidos.
    
    Returns:
        goban (list): lista de listas que representa o tabuleiro sem a cadeia.
    """
    # valida os argumentos
    if (not eh_goban(goban) or 
        any(not eh_intersecao_valida(goban, i) for i in cadeia)):
        raise ValueError("remove_cadeia: argumentos invalidos")
    # remove as pedras das interseções da cadeia
    for i in cadeia:
        remove_pedra(goban, i)
    return goban


def goban_para_str(goban):
    """
    Devolve uma string que representa o estado atual do tabuleiro de jogo.

    Args:
        goban (Goban): O tabuleiro de jogo.

    Returns:
        str: A representação do tabuleiro de jogo em formato de string.
    """

    # função auxiliar para contar o número de digitos
    def digits(num): 
        digitos = 0
        while num != 0:
            digitos += 1
            num //= 10
        return digitos
    
    comp = obtem_lin(obtem_ultima_intersecao(goban))
    goban_str = "  "
    for i in LETRAS[:comp]: # adiciona primeira linha com as letras
        goban_str += f" {i}"
    goban_str += '\n'
    for j in range(comp): # itera pelas linhas do tabuleiro
        espacamento = 2 - digits(comp - j)
        goban_str = goban_str + " " * espacamento + f"{comp - j} " 
        for x in LETRAS[:comp]: # itera pelas interseções dessa linha e adiciona a str da pedra
            goban_str += f"{pedra_para_str(obtem_pedra(goban, cria_intersecao(x, comp - j)))} "
        goban_str = goban_str + " " * espacamento + f"{comp - j}\n" 
    goban_str += "  "
    
    for i in LETRAS[:comp]: # adiciona a última linha com as letras
        goban_str += f" {i}"
    return goban_str


def obtem_captura(goban, pedras_to_remove): # função auxiliar
    """
    Devolve uma lista de cadeias de pedras que podem ser capturadas pelo jogador adversário.

    Args:
        goban (list): uma lista de listas que representa o tabuleiro do jogo.
        pedras_to_remove (tuple): uma tuplo que representa a cor das pedras a serem removidas.

    Returns:
        cadeias (list): uma lista de cadeias de pedras que podem ser capturadas pelo jogador adversário.
    """
    
    cadeias, visitadas = [], []
    tamanho = obtem_lin(obtem_ultima_intersecao(goban))

    # itera pelas interseções
    for x in LETRAS[:tamanho]:
        for y in range(tamanho):
            intersecao = cria_intersecao(x, y + 1)

            # verifica se a interseção tem pedra que pode ser removida
            if (pedras_iguais(obtem_pedra(goban, intersecao), pedras_to_remove) 
                and intersecao not in visitadas):

                cadeia = obtem_cadeia(goban, intersecao)
                visitadas.extend(cadeia)

                # verifica se toda a fronteira é da mesma cor e adiciona
                border = obtem_adjacentes_diferentes(goban, cadeia)
                if all(pedras_iguais(obtem_pedra(goban, i), pedras_to_remove) for i in border):
                    cadeias.append(cadeia)

    return cadeias



# FUNÇÕES DE ALTO NÍVEL (GOBAN)

def obtem_pedras_jogadores(goban):
    """
    Devolve o número de pedras brancas e pretas no tabuleiro.

    Args:
        goban (Goban): O tabuleiro a ser analisado.

    Raises:
        ValueError: Se o argumento não for um tabuleiro válido.

    Returns:
        tuple: Uma tuplo que contém o número de pedras brancas e pretas, respectivamente.
    """
    # valida o argumento
    if not eh_goban(goban):
        raise ValueError("obtem_pedras_jogadores: argumento invalido")
    pretas = 0
    brancas = 0
    tamanho = obtem_lin(obtem_ultima_intersecao(goban))

    # itera pelas interseções e adiciona pontos à respetiva cor
    for x in LETRAS[:tamanho]:
        for i in range(tamanho):

            intersecao = cria_intersecao(x, i + 1)
            if eh_pedra_branca(obtem_pedra(goban, intersecao)):
                brancas += 1
            elif eh_pedra_preta(obtem_pedra(goban, intersecao)):
                pretas += 1

    return (brancas, pretas)

def obtem_territorios(goban):
    """
    Devolve um tuplo que contém as cadeias de interseções com pedras neutras.
    As cadeias são ordenadas tendo em conta a primeira interseção de cada 
    cadeia.

    Args:
        goban (tuple): Uma tuplo que representa o estado atual do jogo.

    Raises:
        ValueError: Se o argumento não for uma tuplo válida que representa 
        o estado atual do jogo.

    Returns:
        tuple: Um tuplo que contém as cadeias de pedras neutras.
    """
    # valida o argumento
    if not eh_goban(goban):
        raise ValueError("obtem_territorios: argumento invalido")
    
    # calcula os território das interseções vazias rodeadas completamente por uma só cor
    territorios, territorios_vistos = (), set()
    tamanho = obtem_lin(obtem_ultima_intersecao(goban))
    for i in LETRAS[:tamanho]:
        for j in range(1, tamanho + 1):
            intersecao = cria_intersecao(i, j)

            if (not eh_pedra_jogador(obtem_pedra(goban, intersecao)) 
                and intersecao not in territorios_vistos):
                
                cadeia = obtem_cadeia(goban, intersecao)
                territorios += (cadeia,)
                territorios_vistos.update(cadeia)
    
    # ordena os territorios dando prioridade à primeira interseção
    return tuple(sorted(territorios, key=lambda x: obtem_lin(x[0])))

def obtem_adjacentes_diferentes(goban, intersecoes):
    """
    Devolve um tuplo ordenado com as interseções adjacentes às interseções 
    dadas que possuem uma ocupação diferente.

    Args:
        goban (tuple): Uma tuplo que representa o estado atual do tabuleiro.
        intersecoes (tuple): Um tuplo com as interseções para as quais se 
        deseja obter os adjacentes diferentes.

    Raises:
        ValueError: Se algum dos argumentos não for válido.

    Returns:
        tuple: Um tuplo ordenado com as interseções adjacentes às 
        interseções dadas que possuem uma ocupação diferente.
    """
    # valida os argumentos
    if not (eh_goban(goban) or not all(eh_intersecao_valida(goban, intersecao) 
                                       for intersecao in intersecoes)):
        raise ValueError("obtem_adjacentes_diferentes: argumentos invalidos")
    # obtem os adjacentes com ocupação diferente, considerando apenas ocupada e livre
    adjacentes = ()
    for intersecao in intersecoes:
        novos_adj = tuple(filter(lambda x: eh_pedra_jogador(obtem_pedra(goban, x)) != 
                eh_pedra_jogador(obtem_pedra(goban, intersecao)), 
                obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(goban))))
        adjacentes += tuple(adj for adj in novos_adj if adj not in adjacentes)
    return ordena_intersecoes(adjacentes)

def jogada(goban, i, p):
    """
    Esta função faz uma jogada alterando o argumento.

    Args:
        goban (list): Uma lista que representa o tabuleiro.
        i (tuple): Um tuplo que representa a interseção.
        p (str): Uma string que representa a pedra.
    
    Returns:
        list: O goban com a jogada efetuada.
    """
    # modifica o tabuleiro g colocando a pedra na interseção dada
    coloca_pedra(goban, i, p)
    # obtem as cadeias de peças dos jogadores
    pedras_to_remove = (cria_pedra_branca() if eh_pedra_preta(p) 
                        else cria_pedra_preta())
    to_remove = obtem_captura(goban, pedras_to_remove)
    # remove as cadeias de peças dos jogadores
    for cadeia in to_remove:
        remove_cadeia(goban, cadeia)
    return goban

    
# FUNÇÕES ADICIONAIS

def calcula_pontos(goban):
    """
    Calcula os pontos de cada jogador no final do jogo.

    Args:
        goban (list): Lista de listas que representa o tabuleiro do jogo.

    Returns:
        tuple: Tuplo com a pontuação do jogador branco e do jogador preto, respectivamente.
    """
    territorios = obtem_territorios(goban)
    # conta as pedras dos jogadores
    pb, pp = obtem_pedras_jogadores(goban)

    for terr in territorios:
        border = obtem_adjacentes_diferentes(goban, terr)
        if not border:
            continue
        # verifica se o território é do jogador branco ou preto
        elif all(eh_pedra_branca(obtem_pedra(goban, i)) for i in border):
            pb += len(terr)
        elif all(eh_pedra_preta(obtem_pedra(goban, i)) for i in border):
            pp += len(terr)
    return (pb, pp)

    

def eh_jogada_legal(goban, i, p, l):
    """
    Verifica se uma jogada é legal, ou seja, se é possível jogar uma pedra na 
    interseção i com a cor p no tabuleiro goban sem violar as regras do jogo.
    
    Args:
        goban (list): uma lista de listas que representa o tabuleiro do jogo.
        i (str): uma string que representa a interseção onde a jogada será feita.
        p (str): uma string que representa a cor da pedra que será jogada.
        l (list): uma lista de listas que representa o estado do tabuleiro antes da jogada.
    
    Returns:
        bool: True se a jogada é legal, False caso contrário.
    """
    if not eh_intersecao_valida(goban, i):
        return False
    if i == "":
        return False
    copia_goban = cria_copia_goban(goban)

    # verifica se a interseção é vazia
    if (eh_pedra_jogador(obtem_pedra(copia_goban, i)) or 
        not eh_intersecao_valida(goban, i)):
        return False
    jogada(copia_goban, i, p)
    # deteta se a jogada não é suicídio
    # verificando se a cadeia da interseção é capturada
    if obtem_captura(copia_goban, p):
        return False
    # verifica se a regra do ko não é quebrada
    return not gobans_iguais(copia_goban, l)

def turno_jogador(goban, p, l):
    """
    Realiza o turno do jogador atual, permitindo que ele faça uma jogada válida no tabuleiro.

    Args:
        goban (list): O tabuleiro atual do jogo.
        p (Pedra): A pedra do jogador atual.
        l (int): O tamanho do lado do tabuleiro.

    Returns:
        bool: True se a jogada foi realizada com sucesso, False se o jogador passou a vez.
    """
    simbolo = (pedra_para_str(cria_pedra_preta()) if eh_pedra_preta(p)
               else pedra_para_str(cria_pedra_branca()))
    str_intersecao = ""
    intersecao = ""

    while True:
        # pede a interseção e se não for válida pede outra vez
        str_intersecao = str(input(f"Escreva uma intersecao ou 'P' para passar [{simbolo}]:"))
        # verifica se o jogador quer passar a vez
        if str_intersecao == "P":
            return False
        try:
            intersecao = str_para_intersecao(str_intersecao)
        except ValueError:
            continue

        # verifica a legalidade da jogada e se não for legal pede outra vez
        if not eh_jogada_legal(goban, intersecao, p, l):
            continue
        # altera o tabuleiro com a jogada e acaba o turno
        jogada(goban, intersecao, p)  # Moved inside the try block
        break  # Break the loop after a successful move

    return True

def go(tamanho, ib, ip):
    """
    Joga uma partida de Go com um tabuleiro de tamanho `tamanho` e as posições iniciais das pedras brancas e pretas
    especificadas pelas listas `ib` e `ip`, respetivamente. Devolve True se o jogador branco ganhar e False caso contrário.

    Args:
        tamanho (int): tamanho do tabuleiro
        ib (list): lista de strings com as posições iniciais das pedras brancas no formato "A1", "B2", etc.
        ip (list): lista de strings com as posições iniciais das pedras pretas no formato "A1", "B2", etc.

    Raises:
        ValueError: se algum dos argumentos for inválido

    Returns:
        bool: True se o jogador branco ganhar, False caso contrário
    """
    # valida os argumentos
    if type(ib) != tuple or type(ip) != tuple:
        raise ValueError("go: argumentos invalidos")
    
    # verifica se as interseções são válidas e se não, levanta uma exceção 
    # com a mensagem de erro

    try:
        if (not eh_goban(cria_goban_vazio(tamanho)) 
            or not all(eh_intersecao(str_para_intersecao(i)) for i in ib) 
            or not all(eh_intersecao(str_para_intersecao(i)) for i in ip)):
            raise ValueError("go: argumentos invalidos")
        ko_impar = cria_goban_vazio(tamanho)
        ko_pares = cria_goban_vazio(tamanho)
        brancas, pretas = tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip)
        goban = cria_goban(tamanho, brancas, pretas)
    except ValueError:
        raise ValueError("go: argumentos invalidos")
    
    vez = 1
    passed = False
    while True:
        pontos = calcula_pontos(goban)
        # imprime a mensagem e decide a pedra a jogar
        print(f"Branco (O) tem {pontos[0]} pontos\nPreto (X) tem {pontos[1]} pontos\n{goban_para_str(goban)}")
        pedra = cria_pedra_branca() if vez % 2 == 0 else cria_pedra_preta()

        # executa o turno do jogador consoante a vez
        # guarda o goban anterior para verificar a regra do ko
        ko = ko_pares if vez % 2 == 0 else ko_impar if vez % 2 == 1 else None
        turno = turno_jogador(goban, pedra, ko)
        if vez % 2 == 0:
            ko_pares = cria_copia_goban(goban)
        elif vez % 2 == 1:
            ko_impar = cria_copia_goban(goban)

        if passed and not turno:
            print(f"Branco (O) tem {pontos[0]} pontos\nPreto (X) tem {pontos[1]} pontos\n{goban_para_str(goban)}")
            break
        elif not passed and not turno:
            passed = True
        else:
            passed = False
        vez += 1
    # devolve True se o jogador branco ganhar
    return pontos[0] > pontos[1]

