# lista_de_tarefas.py

# Função para ler o arquivo de tarefas
def ler_tarefas():
    try:
        with open("tarefas.txt", "r") as file:
            tarefas = [line.strip() for line in file.readlines()]
            return tarefas
    except FileNotFoundError:
        return []

# Função para gravar o arquivo de tarefas
def gravar_tarefas(tarefas):
    with open("tarefas.txt", "w") as file:
        for tarefa in tarefas:
            file.write(tarefa + "\n")

# Função para adicionar uma tarefa
def adicionar_tarefa():
    tarefa = input("Insira uma descrição de tarefa: ")
    tarefas = ler_tarefas()
    tarefas.append(tarefa)
    gravar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

# Função para remover uma tarefa
def remover_tarefa():
    tarefas = ler_tarefas()
    if not tarefas:
        print("Não há tarefas para remover.")
        return
    print("Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")
    num_tarefa = int(input("Insira o número da tarefa a ser removida: ")) - 1
    if num_tarefa < 0 or num_tarefa >= len(tarefas):
        print("Número de tarefa inválido.")
        return
    del tarefas[num_tarefa]
    gravar_tarefas(tarefas)
    print("Tarefa removida com sucesso!")

# Função para marcar uma tarefa como concluída
def marcar_concluida():
    tarefas = ler_tarefas()
    if not tarefas:
        print("Não há tarefas para marcar como concluídas.")
        return
    print("Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")
    num_tarefa = int(input("Insira o número da tarefa a ser marcada como concluída: ")) - 1
    if num_tarefa < 0 or num_tarefa >= len(tarefas):
        print("Número de tarefa inválido.")
        return
    tarefas[num_tarefa] += " (Concluída)"
    gravar_tarefas(tarefas)
    print("Tarefa marcada como concluída com sucesso!")

# Função para exibir todas as tarefas
def exibir_tarefas():
    tarefas = ler_tarefas()
    if not tarefas:
        print("Não há tarefas para exibir.")
        return
    print("Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")

# Função para exibir apenas tarefas concluídas
def exibir_concluidas():
    tarefas = ler_tarefas()
    concluidas = [tarefa for tarefa in tarefas if " (Concluída)" in tarefa]
    if not concluidas:
        print("Não há tarefas concluídas para exibir.")
        return
    print("Tarefas Concluídas:")
    for i, tarefa in enumerate(concluidas, 1):
        print(f"{i}. {tarefa}")

# Função para exibir apenas tarefas pendentes
def exibir_pendentes():
    tarefas = ler_tarefas()
    pendentes = [tarefa for tarefa in tarefas if " (Concluída)" not in tarefa]
    if not pendentes:
        print("Não há tarefas pendentes para exibir.")
        return
    print("Tarefas Pendentes:")
    for i, tarefa in enumerate(pendentes, 1):
        print(f"{i}. {tarefa}")

# Menu principal
while True:
    print("Menu:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Marcar Tarefa como Concluída")
    print("4. Exibir Tarefas")
    print("5. Exibir Tarefas Concluídas")
    print("6. Exibir Tarefas Pendentes")
    print("7. Sair")
    opcao = input("Insira a opção desejada: ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        remover_tarefa()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        exibir_tarefas()
    elif opcao == "5":
        exibir_concluidas()
    elif opcao == "6":
        exibir_pendentes()
    elif opcao == "7":
        break
    else:
        print("Opção inválida. Tente novamente.")