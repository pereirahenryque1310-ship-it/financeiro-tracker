def registrar_transacao():
    descricao = input("Descrição da transação: ")
    
    try:
        valor = float(input("Valor (use ponto para decimais, ex: 150.50): "))
    except ValueError:
        print("Erro: valor inválido. Digite apenas números.")
        return None
    
    transacao = {
        "descricao": descricao,
        "valor": valor
    }
    
    print(f"Transação registrada: {descricao} - R$ {valor:.2f}")
    return transacao


def main():
    transacoes = []  # lista vazia que vai guardar todas as transações
    continuar = "s"
    
    while continuar == "s":
        nova_transacao = registrar_transacao()
        
        if nova_transacao is not None:  # só adiciona se não deu erro
            transacoes.append(nova_transacao)
        
        continuar = input("Registrar outra transação? (s/n): ").lower()
    
    print(f"\nTotal de transações registradas: {len(transacoes)}")
    for t in transacoes:
        print(f"- {t['descricao']}: R$ {t['valor']:.2f}")


main()