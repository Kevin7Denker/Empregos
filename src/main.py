from repository import repo

def populate_system():
    sis = repo.Repo()
            
    sis.cadastrar_candidato("Alice", "alice@example.com", "123456789", ["Python", "Django"])
    sis.cadastrar_candidato("Bob", "bob@example.com", "987654321", ["Java", "Spring"])
    sis.cadastrar_candidato("Charlie", "charlie@example.com", "456123789", ["JavaScript", "React"])
            
    sis.cadastrar_vaga("Desenvolvedor Python", "Desenvolvimento de aplicações web", 5000.0, "Tech Corp", ["Python", "Django"])
    sis.cadastrar_vaga("Desenvolvedor Java", "Desenvolvimento de sistemas corporativos", 6000.0, "Enterprise Inc", ["Java", "Spring"])
    sis.cadastrar_vaga("Desenvolvedor Frontend", "Desenvolvimento de interfaces de usuário", 5500.0, "Web Solutions", ["JavaScript", "React"])

    
def menu():
        sis = repo.Repo()
        
        print("\n")
        print("1 - Candidato")
        print("2 - Vagas")
        print("3 - Compativeis")
        print("4 - Sair")
        
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            menuCandidato()
        if opcao == 2:
            menuVagas()
        if opcao == 3:
            sis.vagas_compativeis()
            menu()
        if opcao == 4:
            print("\n")
            print("Saindo do sistema...")
            exit(0)    
        

def menuCandidato():
        
        sis = repo.Repo()
        
        print("\n")
        print("1 - Cadastrar Candidato")
        print("2 - Listar Candidatos")
        print("3 - Listar Candidatos por habilidade")
        print("4 - Deletar Candidato")
        print("5 - Voltar")
        
        opcao = int(input("Digite a opção desejada: "))
        

        if opcao == 1:
            nome = input("Digite o nome do candidato: ")
            email = input("Digite o email do candidato: ")
            telefone = input("Digite o telefone do candidato: ")
            habilidades = []
            
            while True:
                habilidade = input("Digite uma habilidade do candidato (ou 'sair' para finalizar): ")
                if habilidade.lower() == 'sair':
                    break
                if habilidade == '':
                    print("Habilidade não pode ser vazia. Tente novamente.")
                    continue
                habilidades.append(habilidade)
            
            sis.cadastrar_candidato(nome, email, telefone, habilidades)
            print("Candidato cadastrado com sucesso!")
            menuCandidato()

        if opcao == 2:
            print("\n")
            sis.listar_candidatos()
            menuCandidato()
            
        if opcao == 3:
            habilidade = input("Digite a habilidade desejada: ")
            sis.listar_candidatos_por_habilidade(habilidade)
            menuCandidato()
            
        if opcao == 4:
            print("\n")
            sis.listar_candidatos()
            print("\n")
            nome = input("Digite o nome do candidato que deseja deletar: ")
            sis.DeletarCandidato(nome)
            print("Candidato deletado com sucesso!")
            menuCandidato()
            
        if opcao == 5:
            menu()
            
def menuVagas():
        
        sis = repo.Repo()
        
        print("\n")
        print("1 - Cadastrar Vaga")
        print("2 - Listar Vagas")
        print("3 - Listar Vagas por habilidade")
        print("4 - Deletar Vaga")
        print("5 - Voltar")
        
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            Nome = input("Digite o nome da vaga: ")
            Descricao = input("Digite a descrição da vaga: ")
            Salario = float(input("Digite o salário da vaga: "))
            Empresa = input("Digite a empresa da vaga: ")
            Habilidades = []
            
            while True:
                habilidade = input("Digite uma habilidade do candidato (ou 'sair' para finalizar): ")
                if habilidade.lower() == 'sair':
                    break
                if habilidade == '':
                    print("Habilidade não pode ser vazia. Tente novamente.")
                    continue
                Habilidades.append(habilidade)
            sis.cadastrar_vaga(Nome, Descricao, Salario, Empresa, Habilidades)
            print("Vaga cadastrada com sucesso!")
            menuVagas()
        
        if opcao == 2:
            print("\n")
            sis.listar_vagas()
            menuVagas()
            
        if opcao == 3:
            habilidade = input("Digite a habilidade desejada: ")
            sis.listar_vagas_por_habilidade(habilidade)
            menuVagas()
        
        if opcao == 4:  
            print("\n")
            sis.listar_vagas()
            print("\n")
            Nome = input("Digite o nome da vaga que deseja deletar: ")
            sis.DeletarVaga(Nome)
            print("Vaga deletada com sucesso!")
            menuVagas()
        
        if opcao == 5:
            menu()
        

def main():
        populate_system()
        menu()
        
if __name__ == "__main__":
        main()