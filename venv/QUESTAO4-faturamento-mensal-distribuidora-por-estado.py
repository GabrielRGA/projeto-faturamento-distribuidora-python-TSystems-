# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,
# Outros – R$19.849,53
#
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do
# valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

part_sp = (sp*100)/total
part_rj = (rj*100)/total
part_mg = (mg*100)/total
part_es = (es*100)/total
part_outros = (outros*100)/total

print("-----> No mes as participacoes foram de: \n"
      f"São Paulo: {round(part_sp,2)}%,\n"+("|"*int(part_sp))+"\n"
       f"Rio de Janeiro: {round(part_rj,2)}%,\n"+("|"*int(part_rj))+"\n"
       f"Minas Gerais: {round(part_mg,2)}%,\n"+("|"*int(part_mg))+"\n"
       f"Espirito Santo:{round(part_es,2)}%,\n"+("|"*int(part_es))+"\n"
       f"Já os demais estado foi de: {round(part_outros,2)}%\n"+("|"*int(part_outros)))
