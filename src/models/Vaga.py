from typing import List


class Vaga:
    Nome: str
    Descricao: str
    Salario: float
    Empresa: str
    Requisitos: List[str]

    def __init__(self, Nome: str, Descricao: str, Salario: float, Empresa: str, Requisitos: List[str]):
        self.Nome = Nome
        self.Descricao = Descricao
        self.Salario = Salario
        self.Empresa = Empresa
        self.Requisitos = Requisitos
    
    def __delete__(self):
        del self.Nome
        del self.Descricao
        del self.Salario
        del self.Empresa
        del self.Requisitos
        
    def __str__(self):
        return f"Vaga: {self.Nome} - {self.Descricao} - {self.Salario} - {self.Empresa} - {self.Requisitos}"
    