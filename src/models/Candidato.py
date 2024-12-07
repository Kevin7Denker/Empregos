from typing import List


class Candidato:
    nome: str
    email: str
    telefone: str
    habilidades: List[str]
    
    def __init__(self,nome: str, email: str, telefone: str, habilidades: List[str]):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.habilidades = habilidades

    def __delete__(self):
        del self.nome
        del self.email
        del self.telefone
        del self.habilidades
    
    
    def __str__(self):
        return f"Candidato: {self.nome} - {self.email} - {self.telefone} - {self.habilidades}"
    