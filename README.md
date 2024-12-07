# Sistema de Cadastro de Talentos e Empregos em Tecnologia 

## Autores

- [@Kevin7Denker](https://www.github.com/Kevin7Denker)
- [@ArturSimoni](https://github.com/ArturSimoni)
- [@JefersonAdriano](https://github.com/JefersonAdrianoSerafim)
- [@NathanSchrot](https://github.com/NSchrot)
- [@MiguelIsaac](https://github.com/Owlazi)
- [@YasmimMarcega](https://github.com/yasmimarcega)

## Objetivo

O objetivo deste sistema é oferecer um sistema para gerenciar candidatos e vagas de emprego, permitindo a realização de operações como cadastro, listagem e exclusão, bem como filtros baseados em habilidades específicas.

## Descrição das Entidades

### Candidato
Representa uma pessoa interessada em se candidatar às vagas. Cada candidato possui os seguintes atributos:

* **Nome:** Nome completo do candidato.
* **Email:** Endereço de email para contato.
* **Telefone:** Número de telefone do candidato.
* **Habilidades:** Lista de habilidades específicas do candidato.

### Vaga
Representa uma oportunidade de emprego oferecida por uma empresa. Cada vaga possui os seguintes atributos:

* **Nome:** Nome da vaga.
* **Descrição:** Breve descrição da vaga e responsabilidades associadas.
* **Salário:** Remuneração oferecida pela vaga.
* **Empresa:** Nome da empresa contratante.
* **Requisitos:** Lista de habilidades ou qualificações exigidas para a vaga.

### Funcionalidades do Sistema

* **Cadastrar Candidato:**
Permite o cadastro de um novo candidato no sistema.

Entrada: O sistema solicita ao usuário os dados do candidato, incluindo nome, email, telefone e uma lista de habilidades.

Processo: Os dados fornecidos são usados para criar um objeto candidato que é adicionado à lista de candidatos do sistema.
Saída: Mensagem confirmando que o candidato foi cadastrado com sucesso.

### Cadastrar Vaga
Permite o cadastro de uma nova vaga no sistema.

Entrada: O sistema solicita os detalhes da vaga, como nome, descrição, salário, empresa e requisitos.
Processo: Os dados fornecidos são usados para criar um objeto vaga que é adicionado à lista de vagas do sistema.
Saída: Mensagem confirmando que a vaga foi cadastrada com sucesso.

### Listar Candidatos
Exibe a lista de todos os candidatos cadastrados no sistema.

Entrada: Nenhuma.
Saída: Uma lista com as informações de todos os candidatos, incluindo nome, email, telefone e habilidades.
### Listar Vagas
Exibe a lista de todas as vagas cadastradas no sistema.

Entrada: Nenhuma.
Saída: Uma lista com os detalhes de todas as vagas, incluindo nome, descrição, salário, empresa e requisitos.
### Listar Vagas por Habilidade
Exibe todas as vagas disponíveis que exigem uma habilidade específica.

Entrada: O usuário informa uma habilidade desejada.
Processo: O sistema percorre a lista de vagas e exibe aquelas que possuem a habilidade informada em seus requisitos.
Saída: Lista de vagas compatíveis com a habilidade solicitada.
### Listar Candidatos por Habilidade
Exibe todos os candidatos que possuem uma habilidade específica.

Entrada: O usuário informa uma habilidade desejada.
Processo: O sistema percorre a lista de candidatos e exibe aqueles que possuem a habilidade informada em sua lista de habilidades.
Saída: Lista de candidatos compatíveis com a habilidade solicitada.
### Deletar Vaga
Remove uma vaga específica do sistema.

Entrada: O sistema solicita o nome da vaga a ser deletada.
Processo: O sistema localiza a vaga na lista e a remove, caso exista.
Saída: Mensagem confirmando que a vaga foi deletada ou informando que ela não foi encontrada.
### Deletar Candidato
Remove um candidato específico do sistema.

Entrada: O sistema solicita o nome do candidato a ser deletado.
Processo: O sistema localiza o candidato na lista e o remove, caso exista.
Saída: Mensagem confirmando que o candidato foi deletado ou informando que ele não foi enc  ontrado.
Fluxo de Operações
O usuário é apresentado a um menu com as opções listadas acima.
Após escolher uma opção, o sistema solicita os dados necessários para a operação.
O sistema executa a funcionalidade correspondente e exibe uma mensagem de confirmação ou os resultados, conforme o caso.
O processo continua até que o usuário opte por encerrar o programa.

## Erros Conhecidos e Melhorias Futuras

### Erros Conhecidos:
Ausência de persistência de dados (informações são perdidas ao fechar o programa).

### Melhorias Futuras:
Implementar persistência com banco de dados para salvar candidatos e vagas.
Melhorar as validações para evitar inconsistências nos dados.
Adicionar a funcionalidade de edição de candidatos e vagas.


## Conclusão
O sistema oferece uma solução inicial para gerenciar candidatos e vagas de forma simplificada. Ele pode ser expandido e aprimorado para incluir funcionalidades mais robustas e atender a requisitos mais complexos.
