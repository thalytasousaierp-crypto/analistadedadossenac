import pandas as pd

# Quais são as máximas e mínimas de operação de compra e venda das transações?

df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
df_ativo = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')

df_compra = df_transacoes[df_transacoes['operacao'] == 'compra']
df_venda = df_transacoes[df_transacoes['operacao'] == 'venda']

max_compra_preco = df_compra['preco'].max()
min_compra_preco = df_compra['preco'].min()
max_venda_preco = df_venda['preco'].max()
min_venda_preco = df_venda['preco'].min()
print(max_compra_preco)

#Qual CNPJ tem o ativo de maior valor?

df_transacoes ['valor_total'] = df_transacoes['quantidade'] * df_transacoes['preco']
print(df_transacoes)

valor_por_ativo = df_transacoes.groupby('id_ativo')['valor_total'].sum()
print(valor_por_ativo)
id_ativo_maior_valor = valor_por_ativo.idxmax()
print(valor_por_ativo)
cnpj_maior_valor = df_ativo [df_ativo['id_ativo'] == id_ativo_maior_valor] ['cnpj'].iloc[0]
print(valor_por_ativo)
print("---cnpj_maior_valor ---")
print(f" O cnpj para o ativo com o maior valor total é: {cnpj_maior_valor}")
print("\n")

# Qual valor total em transações de cada participante?
valor_por_participante = df_transacoes.groupby('id_participante')