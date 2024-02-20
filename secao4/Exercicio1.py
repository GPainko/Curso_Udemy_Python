from datetime import datetime, timedelta

# Cria a data do empréstimo utilizando a biblioteca datetime
data_emprestimo = datetime.strptime('20/12/2020', '%d/%m/%Y')
valor_total_emprestimo = 1000000  # Total do empréstimo
duracao_anos = 5  # Duração do empréstimo em anos

# Cálculo do número total de parcelas 
numero_parcelas = duracao_anos * 12
valor_parcela = valor_total_emprestimo / numero_parcelas  # Valor de cada parcela

# Cria a data do final do empréstimo, somando a duração à data inicial
data_final = data_emprestimo + timedelta(days=365 * duracao_anos)

print(f"Empréstimo no valor de R$ {valor_total_emprestimo} com início em {data_emprestimo.strftime('%d/%m/%Y')} e término em {data_final.strftime('%d/%m/%Y')}")
print(f"Valor de cada parcela: R$ {valor_parcela:.2f}\n")

print("Datas de vencimento de cada parcela:")
# Loop para calcular e imprimir cada data de vencimento
for num_parcela in range(1, numero_parcelas + 1):
    # Gera a data de vencimento para a parcela atual
    data_vencimento = data_emprestimo + timedelta(days=30 * num_parcela)

    # Assegura que o dia do vencimento é o esperado
    data_vencimento = data_vencimento.replace(day=20)

    print(f"Parcela {num_parcela}: Data de vencimento = {data_vencimento.strftime('%d/%m/%Y')} - Valor = R$ {valor_parcela:.2f}")