# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um
# programa, na linguagem que desejar, que calcule e retorne:

# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;

# b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
# Estes dias devem ser ignorados no cálculo da média;

from xml.dom import minidom
import json

teclado = input("Qual base de dados deseja usar?\n"
      "DIGITE 1 PARA USAR A BASE DE DADOS XML \n"
      "DIGITE 2 PARA USAR A BASE DE DADOS JSON\n"
      "--------->: ")
while(True):
    match teclado:
        case "1": #--------------------------------------------------------------------------------------------------------------
            print("BASE DE DADOS: -----> XML")
            with open("../dados(2).xml", 'r') as f:
                xml = minidom.parse(f)
                tag_dia = xml.getElementsByTagName("dia")
                tag_valor = xml.getElementsByTagName("valor")

                dia = []
                valor = []
                faturamento_mensal = []

                for tag in tag_dia:
                    dia.append(tag.firstChild.data)

                for tag in tag_valor:
                    valor.append(tag.firstChild.data)

                for i in range(len(dia)):
                    a = dia[i]
                    b = valor[i]
                    faturamento_mensal.append({"dia": int(a), "valor": float(b)})

                var_MaiorValorFaturamento_diaEValor = [0, 0]
                var_menorValorFaturamento_diaEValor = [0, 0]
                var_NumeroDias_FaturamentoSuperiorMedia = 0

            contadorMedia = 0
            valorTotal = 0
            for i in faturamento_mensal:
                dia = int(i["dia"])
                valor = int(i["valor"])

                if (valor != 0):
                    contadorMedia += 1
                    valorTotal += valor

                    if (valor > var_MaiorValorFaturamento_diaEValor[1]):
                        var_MaiorValorFaturamento_diaEValor[0] = dia
                        var_MaiorValorFaturamento_diaEValor[1] = valor
                        var_menorValorFaturamento_diaEValor[1] = valor

            for i in faturamento_mensal:
                dia = int(i["dia"])
                valor = int(i["valor"])

                if (valor != 0):
                    if (valor < var_menorValorFaturamento_diaEValor[1]):
                        var_menorValorFaturamento_diaEValor[0] = dia
                        var_menorValorFaturamento_diaEValor[1] = valor

            print("--> Seu dia de Maior Faturamento: dia " + str(var_MaiorValorFaturamento_diaEValor[0])
                  + " ,com valor de:" + str(var_MaiorValorFaturamento_diaEValor[1]))
            print()
            print("--> Seu dia de Menor Faturamento: dia " + str(var_menorValorFaturamento_diaEValor[0])
                  + " ,com valor de:" + str(var_menorValorFaturamento_diaEValor[1]))
            print()
            mediaFaturamento = valorTotal / contadorMedia
            print("--> Sua media de Faturamento Mensal foi:" + str(mediaFaturamento))

            break
        case "2": #--------------------------------------------------------------------------------------------------------------
            print("BASE DE DADOS: -----> JSON")
            with open("../dados.json") as meu_json:
                dados = json.load(meu_json)

                var_MaiorValorFaturamento_diaEValor = [0, 0]
                var_menorValorFaturamento_diaEValor = [0, 0]
                var_NumeroDias_FaturamentoSuperiorMedia = 0

            # print(dados)

            contadorMedia = 0
            valorTotal = 0
            for i in dados:
                dia = int(i["dia"])
                valor = int(i["valor"])

                if (valor != 0):
                    contadorMedia += 1
                    valorTotal += valor

                    if (valor > var_MaiorValorFaturamento_diaEValor[1]):
                        var_MaiorValorFaturamento_diaEValor[0] = dia
                        var_MaiorValorFaturamento_diaEValor[1] = valor
                        var_menorValorFaturamento_diaEValor[1] = valor

            # preferi separar em 2 'fors' diferentes para resolver o problema do menor valor do faturamento ser 0,
            # sendo que eu gostaria que fosse diferente desse.
            for i in dados:
                dia = int(i["dia"])
                valor = int(i["valor"])

                if (valor != 0):
                    if (valor < var_menorValorFaturamento_diaEValor[1]):
                        var_menorValorFaturamento_diaEValor[0] = dia
                        var_menorValorFaturamento_diaEValor[1] = valor

            print("--> Seu dia de menor Faturamento: dia " + str(var_MaiorValorFaturamento_diaEValor[0])
                  + " ,com valor de:" + str(var_MaiorValorFaturamento_diaEValor[1]))
            print()
            print("--> Seu dia de menor Faturamento: dia " + str(var_menorValorFaturamento_diaEValor[0])
                  + " ,com valor de:" + str(var_menorValorFaturamento_diaEValor[1]))
            print()
            mediaFaturamento = valorTotal / contadorMedia
            print("--> Sua media de Faturamento Mensal foi:" + str(mediaFaturamento))

            break
        case _: #--------------------------------------------------------------------------------------------------------------
            teclado = input("Digite apenas  1 ou 2! \n"
                  "----->: ")
            continue

