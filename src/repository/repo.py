from typing import List
from models import Candidato, Vaga


class Repo():
    
    Candidatos: List[Candidato.Candidato] = []
    Vagas: List[Vaga.Vaga] = []
    
        
    def  cadastrar_candidato(self, nome: str, email: str, telefone: str, habilidades: List[str]):

        try:
            candidato = Candidato.Candidato(nome, email, telefone, habilidades)
            self.Candidatos.append(candidato) 
            
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        
        
    def cadastrar_vaga(self, nome: str, descricao: str, salario: float, empresa: str, requisitos: List[str]):
        try:    
            vaga = Vaga.Vaga(nome, descricao, salario, empresa, requisitos)
            self.Vagas.append(vaga)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            
    def listar_candidatos(self):
        i = False
        
        for candidato in self.Candidatos:
            print(candidato)
            if(candidato in self.Candidatos):
                i = True
        
        if(i==False):
            print("não existem candidatos!")
            
            
           
            
    def listar_vagas(self):
        i = False
        for vaga in self.Vagas:
            print(vaga)
            if(vaga in self.Vagas):
                i = True

        if(i==False):
            print("não existem vagas!")
            
        
    def listar_vagas_por_habilidade(self, requisitos: str):
        i = False
        for vaga in self.Vagas:
            if requisitos in vaga.Requisitos:
                print(vaga)
                i = True
        if not i :
            print("não existem vagas com os requisitos selecionados!")            
    
    def listar_candidatos_por_habilidade(self, habilidade: str):
        i = False
        for candidato in self.Candidatos:
            if habilidade in candidato.habilidades:
                print(candidato)
                i = True
        if not i:
            print("não existem candidatos com essa habilidade(s)")
            
    def DeletarVaga(self, Nome: str):
        
        for vaga in self.Vagas:
            if vaga.Nome == Nome:
                self.Vagas.remove(vaga)
                break 
    
    def DeletarCandidato(self, nome: str):
            
            for candidato in self.Candidatos:
                if candidato.nome == nome:
                    self.Candidatos.remove(candidato)
                    break

    def vagas_compativeis(self):
        for candidato in self.Candidatos:
            for vaga in self.Vagas:
                if all(req in candidato.habilidades for req in vaga.Requisitos):
                    print("\n")
                    print(f"{candidato.nome} é compatível com a vaga {vaga.Nome}")
                    print("habilidades do candidato: ", candidato.habilidades)