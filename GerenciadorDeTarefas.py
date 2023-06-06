import csv
import os

#local armazenamento do arquivo
arquivo_csv ='GerenciadorTarefas/tarefas.csv'

def exibir_menu():
    print("------ GERENCIADOR DE TAREFAS ------")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Ver tarefas em Realizadas! ")
    print("5. Sair")

def ver_tarefas():
    if not os.path.exists(arquivo_csv):
        print('Ainda nao há tarefas adicionadas.')
        return
    with open(arquivo_csv,'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print (f"[{linha[0]}] {linha[1]}")

def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = [get_proximo_id(), descricao]

    with open(arquivo_csv, 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(tarefa)

    print("Tarefa adicionada com sucesso!")
    
def marcar_tarefa_concluida():
    id_tarefa = input("Digite o ID da tarefa concluída: ")

    tarefas = []
    with open(arquivo_csv, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            tarefas.append(linha)

    encontrada = False
    with open(arquivo_csv, 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for tarefa in tarefas:
            if tarefa[0] == id_tarefa:
                encontrada = True
                tarefa.append("Concluida")
            escritor.writerow(tarefa)

    if encontrada:
        print("Tarefa marcada como concluída!")
    else:
        print("Nenhuma tarefa encontrada com o ID fornecido.")

def get_proximo_id():
    if not os.path.exists(arquivo_csv):
        return 1
    with open(arquivo_csv, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        linhas = list(leitor)
        if len(linhas) == 0:
            return 1
        ultimo_id = int(linhas[-1][0])
        return ultimo_id + 1

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def ver_tarefas_concluidas():
    if not os.path.exists(arquivo_csv):
        print('Ainda nao há tarefas adicionadas.')
        return
    with open(arquivo_csv,'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if(len(linha)==2):
                print (f"[{linha[0]}] {linha[1]}")
                #print("")
            else:
                print (f"[{linha[0]}] {linha[1]} - {linha[2]}")

def contar_colunas():
    with open(arquivo_csv, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        primeira_linha = next(leitor_csv)  # Lê a primeira linha do arquivo CSV
        num_colunas = len(primeira_linha)
        return num_colunas


def main():
    while True:
        exibir_menu()
        opcao = input('Digite a opcao desejada:')

        if opcao == "1":
            ver_tarefas()
        elif opcao == "2":
            adicionar_tarefa()
            limpar_tela()  
        elif opcao == "3":
            marcar_tarefa_concluida()
            #limpar_tela() 
        elif opcao == "4":
            ver_tarefas_concluidas()          
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente Novamente.")
        
        print()
  
if __name__ == "__main__":
    main() 


    