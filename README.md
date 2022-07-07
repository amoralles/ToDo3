![banner](https://doity.com.br/blog/wp-content/uploads/2019/03/avalia%C3%A7%C3%A3o-de-trabalhos-cient%C3%ADficos.png)

# Deu Match!

### ToDo3 do Curso de Data Analyst da RESILIA

Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade de um candidato com uma vaga de acordo com seu resultado nas etapas do processo seletivo. Para isso foi criado um teste que devolve uma string no seguinte formato: eX_tX_pX_sX (sendo que cada X é substituído pela avaliação da pessoa em uma das etapas do processo - entrevista, teste teórico, teste prático e avaliação de soft skills).

*Temos a seguinte lista de candidatos como exemplo e os resultados:*

**Candidato 1:** e5_t10_p8_s8

**Candidato 2:** e10_t7_p7_s8

**Candidato 3:** e8_t5_p4_s9

**Candidato 4:** e2_t2_p2_s1

**Candidato 5:** e10_t10_p8_s9

O desafio é criar em Pyhton um algoritmo que armazene esses dados (e outros, no mesmo formato, a serem adicionados) e depois busque o candidato que corresponda a critérios digitados pelo usuário. O usuário vai informar qual a nota mínima de e, t, p e s que ele deseja buscar, nossa aplicação deve listar quem são os candidatos disponíveis com nota maior ou igual a essas informadas. Ao buscar por alguém com resultados '4,4,8,8', por exemplo, vamos receber que os candidatos 1 e 5 atendem a esse critério.

Inicialmente, já há uma lista com as notas desses 5 candidatos. Em seguida, ao executar o programa, é solicitado ao usuário se ele deseja adicionar mais notas a essa lista, ou não. As notas só serão aceitas se forem incluidas no formato apresentado acima. Em seguida, o programa pergunta se o usuário deseja ver a lista completa de candidatos e notas. Depois solicita que sejam incluidas notas entre 0 e 10 para cada critério de avaliação. Então avalia qual dos candidatos da lista possui os critérios mínimos desejados.

Esse projeto foi desenvolvido individualmente como atividade do curso, mas também como meio de treinar e colocar em práticas as *skills* de programação desenvolvidas até agora. O foco é a utilização de listas, funções, condicionais e loop. Qualquer feedback é bem vindo!  <img src="https://images.emojiterra.com/google/noto-emoji/v2.034/128px/1faf0.png" width="20">



