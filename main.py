# Importações necessárias
import openai  # Cliente OpenAI para interação com a API
from typing import List, Optional  # Tipos para anotações
from rich import print  # Formatação rica para output no terminal
from dotenv import load_dotenv  # Carregamento de variáveis de ambiente
import guardrails as gd  # Framework para validação de saídas do LLM
from valid_items_field import ItemValidator  # Schema de validação Pydantic

# Carrega variáveis de ambiente do arquivo .env (incluindo OPENAI_API_KEY)
load_dotenv()

# Define o prompt principal que instrui o GPT-4 sobre seu papel e tarefas
# O prompt inclui diretrizes específicas para:
# - Especificações técnicas
# - Requisitos de qualidade
# - Critérios de sustentabilidade
prompt = """

Você é um técnico especializado em equipamentos eletroeletrônicos 
com experiência em desenvolver Termos de Referência para aquisição 
de equipamentos. Sua tarefa é criar uma descrição técnica detalhada 
de um equipamento delimitado por {item}, pronto para uso em documentos 
oficiais de licitação. Utilize o esquema delimitado por <exemplo>  como guia 
de como a descrição deve ser fornecida e inclua outras informações técnicas 
relevantes e específicas de cada {item}. 


Pense passo a passo para elaborar cada especificação. Analise as principais
características técnicas do {item}, selecione as mais importantes e redija em 
até 800 caracteres. Certifique-se de que os outros campos estão completos e 
coerentes. Explique brevemente a razão de cada decisão antes de apresentar
o resultado final.

Utilizando o grau de escrita técnica definido por {técnica} de 1 a 5 onde 1 significa que 
que o campo  'descrição' deve ser redigido para pessoas não especialistas e 5 significa que a descrição
do campo 'descrição' deve ser redigido para pessoas especialistas e deve ser a mais técnica possivel.

Siga estas diretrizes:

1. ESPECIFICAÇÕES TÉCNICAS:
   - Liste todas as especificações técnicas relevantes
   - Inclua tecnologias diferenciais, dimensões, potência, capacidade e outras métricas importantes
   - Mencione tecnologias e recursos específicos

2. REQUISITOS DE QUALIDADE:
   - Cite certificações necessárias como  PROCEL, ISO 9001
   - Mencione normas técnicas aplicáveis como ISO, ABNT NBR  entre outras
   - Especifique requisitos de garantia

3. CRITÉRIOS DE SUSTENTABILIDADE:
   - Inclua requisitos de eficiência energética 
   - Inclua requisitos de sustentabilidade com certificações relevantes
   - Mencione certificações ambientais relevantes
   - Especifique critérios de descarte e reciclagem



<exemplo>

item: Computador Desktop
descricao: Computador Desktop com processador Intel Core i7, 16GB RAM,
SSD 512GB, placa de vídeo dedicada NVIDIA GTX 1660, monitor de 27 polegadas 
Full HD. Ideal para processamento gráfico e multitarefa.
quantidade: 10
fabricante: Dell
modelo: OptiPlex 5090
site: www.dell.com

</exemplo>



"""

# Configuração dos parâmetros de entrada
# item_name: nome do item para gerar especificações
# tecnica_level: nível de complexidade técnica (1-5)
item_name = "café"
tecnica_level = 5

# Formata o conteúdo para envio ao modelo
content = f"""
item: {item_name}
técnica: {tecnica_level}
"""

# Estrutura as mensagens no formato esperado pela API OpenAI
# - system: define o comportamento do modelo
# - user: contém a entrada específica do usuário
messages = [{
  "role": "system",
  "content": prompt
}, {
  "role": "user",
  "content": content
}]

# Cria um guard usando o modelo Pydantic ItemValidator
# Isso garante que a saída do modelo seguirá a estrutura definida
guard = gd.Guard.for_pydantic(ItemValidator)

# Executa o modelo com os parâmetros definidos
# - raw_llm_output: saída bruta do modelo
# - validated_output: saída validada conforme o schema
# - temperature=0.0: mantém as respostas consistentes
# - max_tokens=1024: limite máximo de tokens na resposta
raw_llm_output, validated_output, *rest = guard(
    messages=messages,
    model="gpt-4o-mini",
    max_tokens=1024,
    temperature=0.0,
)

# Mostra a árvore de validação da última execução
# Útil para debug e entender como o modelo estruturou a resposta
# print(validated_output)
print(guard.history.last.tree)