pecas = []
caixas_fechadas = []
CAPACIDADE_CAIXA = 10
contador_id = 1

PESO_MIN = 95
PESO_MAX = 105
CORES_ACEITAS = ["azul", "verde"]
COMP_MIN = 10
COMP_MAX = 20

def validar_peca(peso, cor, comprimento):
    peso_ok = PESO_MIN <= peso <= PESO_MAX
    cor_ok = cor.lower() in CORES_ACEITAS
    comp_ok = COMP_MIN <= comprimento <= COMP_MAX
    return peso_ok and cor_ok and comp_ok

def cadastrar_peca():
    global contador_id
    print("\n--- CADASTRAR NOVA PEÇA ---")
    try:
        peso = float(input("Peso (g): "))
        cor = input("Cor (azul/verde/outra): ").strip().lower()
        comprimento = float(input("Comprimento (cm): "))
    except ValueError:
        print("Valor invalido! Digite numeros para peso e comprimento.")
        return

    aprovada = validar_peca(peso, cor, comprimento)
    status = "aprovada" if aprovada else "reprovada"

    peca = {
        "id": contador_id,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status
    }
    pecas.append(peca)
    contador_id += 1

    print(f"\nPeca #{peca['id']} cadastrada como: {status.upper()}")

    aprovadas = [p for p in pecas if p["status"] == "aprovada"]
    if len(aprovadas) > 0 and len(aprovadas) % CAPACIDADE_CAIXA == 0:
        numero_caixa = len(caixas_fechadas) + 1
        caixas_fechadas.append({
            "numero": numero_caixa,
            "pecas": aprovadas[-CAPACIDADE_CAIXA:]
        })
        print(f"CAIXA #{numero_caixa} FECHADA com {CAPACIDADE_CAIXA} pecas aprovadas!")

def listar_pecas():
    print("\n--- LISTA DE PECAS ---")
    if not pecas:
        print("Nenhuma peca cadastrada ainda.")
        return
    for p in pecas:
        icone = "OK" if p["status"] == "aprovada" else "XX"
        print(f"[{icone}] Peca #{p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comp: {p['comprimento']}cm | {p['status'].upper()}")

def remover_peca():
    print("\n--- REMOVER PECA ---")
    listar_pecas()
    if not pecas:
        return
    try:
        id_remover = int(input("\nDigite o ID da peca para remover: "))
    except ValueError:
        print("ID invalido.")
        return

    for p in pecas:
        if p["id"] == id_remover:
            pecas.remove(p)
            print(f"Peca #{id_remover} removida com sucesso.")
            return
    print(f"Peca com ID {id_remover} nao encontrada.")

def listar_caixas():
    print("\n--- CAIXAS FECHADAS ---")
    if not caixas_fechadas:
        print("Nenhuma caixa fechada ainda. Sao necessarias 10 pecas aprovadas.")
        return
    for caixa in caixas_fechadas:
        ids = [str(p["id"]) for p in caixa["pecas"]]
        print(f"Caixa #{caixa['numero']} | Pecas: {', '.join(ids)}")

def gerar_relatorio():
    print("\n========== RELATORIO FINAL ==========")
    total = len(pecas)
    aprovadas = len([p for p in pecas if p["status"] == "aprovada"])
    reprovadas = len([p for p in pecas if p["status"] == "reprovada"])
    percentual = (aprovadas / total * 100) if total > 0 else 0

    print(f"Total de pecas cadastradas : {total}")
    print(f"Pecas aprovadas            : {aprovadas}")
    print(f"Pecas reprovadas           : {reprovadas}")
    print(f"Caixas fechadas            : {len(caixas_fechadas)}")
    print(f"Taxa de aprovacao          : {percentual:.1f}%")
    print("=====================================")

def menu():
    while True:
        print("\n========== SISTEMA DE INSPECAO ==========")
        print("1. Cadastrar nova peca")
        print("2. Listar pecas aprovadas/reprovadas")
        print("3. Remover peca cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatorio final")
        print("0. Sair")
        print("=========================================")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("Encerrando sistema. Ate logo!")
            break
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    menu()
