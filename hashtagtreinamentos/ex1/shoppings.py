import pandas as pd  # importa a biblioteca pandas com o nome pd

tabela = pd.read_excel("Vendas.xlsx") # define a tabela como um elemento que está dentro da biblioteca pandas
# e que o elemento é um read_excel com o nome de Vendas.xlsx

print('-'*100)

print(tabela) # mostra o elemento tabela definido acima 

print('-'*100)

faturamento_total_shopping = tabela["Valor Final"].sum() # define o elemento faturamento_total_shopping como uma soma
# de todos os elemtnos da "Valor Final" da tabela definida acima 

print(f"Faturamento total shoppings: R$ {faturamento_total_shopping}")

print('-'*100)
# Verificar o faturamento por loja shopping

faturamento_separado = tabela[["ID Loja","Valor Final"]].groupby("ID Loja").sum() # define o faturamento separado como
# uma união das colunas ID Loja e Valor Final da tabela TABELA, realizando uma agrupação pelo ID Loja (parâmetro .groupby) 
# e por um fim realizando a soma de cada ID Loja para obter uma separação por loja

print(faturamento_separado) # mostra o resultado do faturamento separado

print('-'*100)

# Verificando qual item mais vendeu em cada shopping 

faturamento_produto = tabela[["ID Loja","Produto","Valor Final"]].groupby(["ID Loja","Produto"]).sum() # define a variavel
# faturamento_produto com os itens ID Loja, Produto e Valor Final da tabela definida antes, realizando um agrupamento pelo ID da
# loja e o produto que cada uma vendeu, ao final, realizando uma soma do valor final de cada produto vendido por loja

print(faturamento_produto) # mostra o resultado do requerimento

print('-'*100)