resultados = ['e5_t10_p8_s8', 'e10_t7_p7_s8', 'e8_t5_p4_s9', 'e2_t2_p2_s1', 'e10_t10_p8_s9', 'e8_t5_p6_s9']


def buscar_notas(resultados):
    notas_min = []
    nota_e_min = (input("Nota mínima na entrevista: "))
    notas_min.append(nota_e_min)
    nota_t_min = (input("Nota mínima no teste teórico: "))
    notas_min.append(nota_t_min)
    nota_p_min = (input("Nota mínima no teste prático: "))
    notas_min.append(nota_p_min)
    nota_s_min = (input("Nota mínima na avaliação soft skills: "))
    notas_min.append(nota_s_min)

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

        candidatos_aptos = []

    for notas_i in range(len(notas_candidatos)):
        notas = notas_candidatos[notas_i]

        if (int(notas[0]) >= int(notas_min[0])) and (int(notas[1]) >= int(notas_min[1])) and (int(notas[2]) >= int(notas_min[2])) and (int(notas[3]) >= int(notas_min[3])):
            candidato = (notas_candidatos.index(notas_candidatos[notas_i]) + 1)
            candidatos_aptos.append(candidato)

    if candidatos_aptos == []:
        return print(f'Nenhum candidato atende aos critérios escolhidos')
    else:    
        for i in candidatos_aptos:
            print(f'O candidato {i} atende aos critérios escolhidos.')
    
    return 

(buscar_notas(resultados))
