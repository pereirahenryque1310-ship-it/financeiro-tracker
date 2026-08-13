def registrar_transacao():
    descricao = input("Descrição da transação: ")
    
    tipo = input("Tipo (receita/despesa): ").lower()
    while tipo not in ("receita", "despesa"):
        print("Digite apenas 'receita' ou 'despesa'.")
        tipo = input("Tipo (receita/despesa): ").lower()
    
    try:
        valor = float(input("Valor (use ponto para decimais, ex: 150.50): "))
    except ValueError:
        print("Erro: valor inválido. Digite apenas números.")
        return None
    
    transacao = {
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo
    }
    
    print(f"Transação registrada: {descricao} - R$ {valor:.2f} ({tipo})")
    return transacao


def main():
    transacoes = []
    continuar = "s"
    
    while continuar == "s":
        nova_transacao = registrar_transacao()
        
        if nova_transacao is not None:
            transacoes.append(nova_transacao)
        
        continuar = input("Registrar outra transação? (s/n): ").lower()
    
    saldo = 0
    print(f"\nTotal de transações registradas: {len(transacoes)}")
    for t in transacoes:
        print(f"- {t['descricao']}: R$ {t['valor']:.2f} ({t['tipo']})")
        if t['tipo'] == "receita":
            saldo += t['valor']
        else:
            saldo -= t['valor']
    
    print(f"\nSaldo final: R$ {saldo:.2f}")


main()