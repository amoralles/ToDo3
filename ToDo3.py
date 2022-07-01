resultados = ['e5_t10_p8_s8', 'e10_t7_p7_s8', 'e8_t5_p4_s9', 'e2_t2_p2_s1', 'e10_t10_p8_s9']

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

    print(notas_min)

    lista_notas = []

    for i in resultados:
        notas_ind = []
        e = i[i.index('e') + 1 : i.index("_")]
        notas_ind.append(e)
        t = i[i.index('t') + 1 : i.find("_", i.index('t'))]
        notas_ind.append(t)
        p = i[i.index('p') + 1 : i.find("_", i.index('p'))]
        notas_ind.append(p)
        s = i[i.index('s') + 1 : ]
        notas_ind.append(s)

        lista_notas.append(notas_ind)     

      

    print(lista_notas)

print(buscar_notas(resultados))
