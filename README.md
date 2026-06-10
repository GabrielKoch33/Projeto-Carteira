# Dashboard de Gastos Pessoais

## Descrição

O Dashboard de Gastos Pessoais é um sistema desenvolvido em Python para auxiliar no controle financeiro pessoal. O projeto permite registrar receitas e despesas, organizar gastos por categorias, armazenar informações de forma persistente e gerar relatórios para acompanhamento financeiro.

Além de servir como uma ferramenta de gestão financeira, o projeto tem como objetivo consolidar conhecimentos de programação, estrutura de dados, modularização, persistência de dados e análise de informações, criando uma base sólida para futuras aplicações em Engenharia e Ciência de Dados.

---

## Funcionalidades

### Receitas

* Cadastro de receitas
* Edição de receitas
* Exclusão de receitas
* Consulta de receitas cadastradas

### Despesas

* Cadastro de despesas
* Edição de despesas
* Exclusão de despesas
* Consulta de despesas cadastradas

### Categorias

* Categorias padrão do sistema
* Cadastro de categorias personalizadas
* Listagem de categorias disponíveis
* Validação de categorias durante os lançamentos

### Relatórios

* Total de receitas
* Total de despesas
* Saldo atual
* Gastos por categoria
* Gastos por período
* Histórico de movimentações

### Persistência

* Armazenamento dos dados em arquivos JSON
* Carregamento automático dos dados salvos

---

## Estrutura dos Dados

### Receita

```python
{
    "id": 1,
    "descricao": "Salário",
    "valor": 3500.00,
    "data": "2026-06-10"
}
```

### Despesa

```python
{
    "id": 1,
    "descricao": "Mercado",
    "valor": 250.00,
    "categoria": "Alimentação",
    "data": "2026-06-10"
}
```

### Categoria

```python
{
    "nome": "Alimentação",
    "default": True
}
```

---

## Estrutura do Projeto

```text
dashboard-gastos/
│
├── main.py
├── receitas.py
├── despesas.py
├── categorias.py
├── relatorios.py
├── persistencia.py
├── dados.py
│
├── data/
│   ├── receitas.json
│   ├── despesas.json
│   └── categorias.json
│
└── README.md
```

---

## Regras de Negócio

* Todo lançamento possui um identificador único (ID).
* Toda receita e despesa deve possuir uma data.
* O saldo não é armazenado diretamente; ele é calculado a partir das receitas e despesas registradas.
* Categorias padrão do sistema não podem ser removidas.
* Os valores monetários são armazenados numericamente para facilitar cálculos e análises futuras.
* As categorias informadas em despesas devem existir previamente no sistema.

---

## Tecnologias Utilizadas

* Python
* JSON
* Programação Modular
* Estruturas de Dados (listas e dicionários)

---

## Objetivos de Aprendizagem

Este projeto foi desenvolvido para praticar:

* Lógica de programação
* Modularização
* Manipulação de arquivos
* Persistência de dados
* Estruturas de dados
* CRUD (Create, Read, Update, Delete)
* Organização de projetos Python
* Boas práticas de desenvolvimento

---

## Evoluções Futuras

Planejadas para versões posteriores:

* Interface gráfica
* Dashboard interativo
* Gráficos de gastos
* Exportação para CSV e Excel
* Integração com Pandas
* Análise temporal de gastos
* Metas financeiras
* Alertas de orçamento
* Indicadores financeiros
* Previsão de gastos utilizando análise de dados

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/dashboard-gastos.git
```

2. Acesse a pasta do projeto:

```bash
cd dashboard-gastos
```

3. Execute o sistema:

```bash
python main.py
```

---

## Licença

Este projeto foi desenvolvido para fins educacionais e de aprendizado.
