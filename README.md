# Trabalho de EngPrompts

Este projeto é um gerador de especificações técnicas para equipamentos eletroeletrônicos, projetado para auxiliar na criação de Termos de Referência para licitações. 
A parir da entrada de um item e um nível de descrição tecnica, o programa utiliza um modelo GPT-4 com guardrails para gerar especificações detalhadas e formatadas.


## Funcionalidades

O arquivo `main.py` é o componente principal do projeto que:

- Utiliza o modelo GPT-4 com guardrails para gerar especificações técnicas detalhadas
- Permite ajustar o nível técnico da descrição em uma escala de 1 a 5
- Gera especificações seguindo diretrizes específicas:
  - Especificações técnicas (dimensões, potência, capacidade)
  - Requisitos de qualidade (certificações, normas técnicas)
  - Critérios de sustentabilidade (eficiência energética, certificações ambientais)

## Estrutura da Saída

O programa gera especificações no formato:
- Descrição detalhada do item
- Quantidade
- Fabricante
- Modelo
- Site do fabricante

## Dependências

O projeto utiliza:
- python 3.12
- guardrails 0.515
- python-dotenv
- pydantic

## Como Executar

1. Instale o uv (gerenciador de pacotes):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Configure o ambiente virtual e instale as dependências:
   ```bash
   uv sync
   source .venv/bin/activate  # Linux/MacOS
   
   ```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave API do OpenAI:
     ```
     OPENAI_API_KEY=sua_chave_aqui
     ```

4. Execute o programa: Passe os itens e nível de descrição tecnicas nas variaveis no aqurivo main.py:  "item_name = "item: 'Televisor 85 polegadas'" e ""tecnica_level = 5"

   ```bash
   python main.py
   ```
