from guardrails import Guard
from dotenv import load_dotenv
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from valid_items_field import ItemValidator

load_dotenv()


# Setup Guard
guard = Guard.from_pydantic(output_class=ItemValidator)


prompt = """

Você é um técnico especializado em equipamentos eletroeletrônicos 
com experiência em desenvolver Termos de Referência para aquisição 
de equipamentos. Sua tarefa é criar uma descrição técnica detalhada 
de um equipamento delimitado por {item}, pronto para uso em documentos 
oficiais de licitação. Utilize o esquema delimitado por <exemplo>  como exemplo 
de como a descrição deve ser fornecido e inclua outras informações técnicas 
relevantes e específicas de cada {item}. 


Pense passo a passo para elaborar cada especificação. Analise as principais
características técnicas do {item}, selecione as mais importantes e redija em 
até 800 caracteres. Certifique-se de que os outros campos estão completos e 
coerentes. Explique brevemente a razão de cada decisão antes de apresentar
o resultado final.

Utilizando o grau de escrita técnica definido por {técnica} de 1 a 5 onde 1 significa que 
que o campo  'descrição' deve ser redigido para pessoas não especialistas e 5 significa que a descrição
o campo 'descrição' deve ser redigido para pessoas especialistas e deve ser a mais técnica possivel.

Siga estas diretrizes:

1. ESPECIFICAÇÕES TÉCNICAS:
   - Liste todas as especificações técnicas relevantes
   - Inclua dimensões, potência, capacidade e outras métricas importantes
   - Mencione tecnologias e recursos específicos

2. REQUISITOS DE QUALIDADE:
   - Cite certificações necessárias
   - Mencione normas técnicas aplicáveis
   - Especifique requisitos de garantia

3. CRITÉRIOS DE SUSTENTABILIDADE:
   - Inclua requisitos de eficiência energética
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


item_name = "item: 'Televisor 85 polegadas'"
# item_name = "item: 'Forno de micro-ondas'"
# item_name = "item: 'café'"
# item_name = "papel higienico"
tecnica_level = 5

# Format the content as a single string
content = f"""
item: {item_name}
técnica: {tecnica_level}
"""

try:
    res = guard(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
    )
    print(f"Saida: {res.raw_llm_output}")
    print(f"Saida Validada: {res.validated_output}")

except Exception as e:
    print("Error:", str(e))
