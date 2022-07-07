resultados = ['e5_t10_p8_s8', 'e10_t7_p7_s8', 'e8_t5_p4_s9', 'e2_t2_p2_s1', 'e10_t10_p8_s9', 'e8_t5_p6_s9']

def receberNotasMinimas():
    notas_min = []
    while True:
        try:
            nota_e_min = int(input("Nota mínima na entrevista: "))
            notas_min.append(nota_e_min)
            nota_t_min = int(input("Nota mínima no teste teórico: "))
            notas_min.append(nota_t_min)
            nota_p_min = int(input("Nota mínima no teste prático: "))
            notas_min.append(nota_p_min)
            nota_s_min = int(input("Nota mínima na avaliação soft skills: "))
            notas_min.append(nota_s_min)
            if (nota_e_min > 10) or (nota_t_min > 10) or (nota_p_min > 10) or (nota_s_min > 10):
                    raise ValueError('Insira apenas números entre 0 e 10. ')
        except ValueError as e:
            print("Insira apenas números inteiros válidos. Valor inválido:", e)
        else:
            break
    return notas_min

def atualizarListaDeNotas(resultados):
    print(f'Há {len(resultados)} notas no banco de dados atual.')
    contador = len(resultados)
    entrada = input(
        'Deseja adicionar mais algum candidato ao banco de dados? Digite "SIM" ou "NÃO" ')

    if (entrada.upper() == 'NÃO') or (entrada.upper() == 'NAO'):
        return resultados
    if entrada.upper() == 'SIM':
        while True:
            try:
                entrada1 = input(f'Insira a nota no formato "eW_tX_pY_sZ" para o candidato {contador +1}: ')
                i = entrada1
                e = i[i.index('e') + 1: i.index("_")]
                t = i[i.index('t') + 1: i.find("_", i.index('t'))]
                p = i[i.index('p') + 1: i.find("_", i.index('p'))]
                s = i[i.index('s') + 1:]
                if (int(e) > 10) or (int(t)> 10) or (int(p) > 10) or (int(s) > 10):
                    raise ValueError('Insira apenas números entre 0 e 10. ')
            except ValueError as e:
                print("Insira apenas números inteiros válidos. Valor inválido:", e)
            else:
                break
            
        resultados.append(entrada1)
        atualizarListaDeNotas(resultados)        
        return resultados
    else:
        print(f'Digite uma opção válida: SIM ou NÃO')
    return atualizarListaDeNotas(resultados)

def visualizarBanco(resultados):
    print(f'Há {len(resultados)} notas no banco de dados atual.')
    entrada = input(f'Deseja ver as notas de todos os candidatos inscritos? Digite SIM ou NÃO: ')
    if (entrada.upper() == 'NÃO') or (entrada.upper() == 'NAO'):
        return 
    if entrada.upper() == 'SIM':
        contador = 1 
        for i in resultados:
            print(f'Candidato {contador}: {i}')
            contador = contador +1 
        return
    else:
        print(f'Digite uma opção válida: SIM ou NÃO')
    return 

def listarCandidatos(resultados):
    notas_candidatos = []
    for i in resultados:
        notas_individuais = []
        e = i[i.index('e') + 1: i.index("_")]
        notas_individuais.append(e)
        t = i[i.index('t') + 1: i.find("_", i.index('t'))]
        notas_individuais.append(t)
        p = i[i.index('p') + 1: i.find("_", i.index('p'))]
        notas_individuais.append(p)
        s = i[i.index('s') + 1:]
        notas_individuais.append(s)

        notas_candidatos.append(notas_individuais)
    return notas_candidatos

def candidatosAptos(notas_candidatos, notas_min):
    candidatos_aptos = []

    for notas_i in range(len(notas_candidatos)):
        notas = notas_candidatos[notas_i]

        if (int(notas[0]) >= int(notas_min[0])) and (int(notas[1]) >= int(notas_min[1])) and (int(notas[2]) >= int(notas_min[2])) and (int(notas[3]) >= int(notas_min[3])):
            candidatos = [i+1 for i in range(len(notas_candidatos)) if notas_candidatos[i] == notas]
            if len(candidatos) > 1:
                    for i in candidatos:
                        candidato = i
                        if candidato in candidatos_aptos:
                            pass
                        else:
                            candidatos_aptos.append(candidato)
                        
            else: 
                candidato = candidatos[0]
                candidatos_aptos.append(candidato)

    if candidatos_aptos == []:
        return print(f'Nenhum candidato atende aos critérios escolhidos')
    else:
        for i in candidatos_aptos:
            print(f'O candidato {i} atende aos critérios escolhidos.')
    return

# Iniciando o programa:

# Atualizando, ou não, a lista que contém as notas dos candidatos entrevistados:
resultados = atualizarListaDeNotas(resultados)

# Lista as notas dos candidatos no banco de dados atual:
visualizarBanco(resultados)

# Transforma o modelo inicial de armazenamento de notas em apenas números:
notas_candidatos = listarCandidatos(resultados)

# Recebe quais os critério utilizados como mínimos:
notas_min = receberNotasMinimas()

# Diz, por fim, quais candidatos estão aptos de acordo com os requisitos mínimos
candidatosAptos(notas_candidatos, notas_min)
