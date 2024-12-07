from pydantic import BaseModel, Field, HttpUrl, ValidationError
from typing import List, Optional


class ItemValidator(BaseModel):
    """Validador para especificações técnicas de itens.

    Esta classe define a estrutura e as regras de validação para as especificações
    técnicas de itens em documentos de licitação. Utiliza o Pydantic para garantir
    que todos os campos obrigatórios estejam presentes e válidos.

    Attributes:
        item (str): Nome do item a ser especificado. Deve ter pelo menos 1 caractere.
        fabricante (str): Nome do fabricante do item. Deve ter pelo menos 1 caractere.
        modelo (str): Código ou nome do modelo do item. Deve ter pelo menos 1 caractere.
        descricao (str): Descrição técnica detalhada do item. Deve ter pelo menos 1 caractere.
        tecnologia (str): Especificações da tecnologia utilizada. Deve ter pelo menos 1 caractere.
        quantidade (int): Quantidade do item a ser adquirida. Deve ser maior que 0.
        sustentabilidade (str): Critérios de sustentabilidade aplicáveis. Deve ter pelo menos 1 caractere.
        normas (str): Normas técnicas e certificações aplicáveis. Deve ter pelo menos 1 caractere.
        site (Optional[HttpUrl]): URL do site do fabricante ou do produto. Opcional.

    Example:
        >>> item = ItemValidator(
        ...     item="Computador Desktop",
        ...     fabricante="Dell",
        ...     modelo="OptiPlex 5090",
        ...     descricao="Computador Desktop com processador Intel Core i7",
        ...     tecnologia="Intel vPro",
        ...     quantidade=10,
        ...     sustentabilidade="Energy Star 8.0, EPEAT Gold",
        ...     normas="ISO 9001, RoHS",
        ...     site="https://www.dell.com"
        ... )
    """
    item: str = Field(..., min_length=1)
    fabricante: str = Field(..., min_length=1)
    modelo: str = Field(..., min_length=1)
    descricao: str = Field(..., min_length=1)
    tecnologia: str = Field(..., min_length=1)
    quantidade: int = Field(..., gt=0)
    sustentabilidade: str = Field(..., min_length=1)
    normas: str = Field(..., min_length=1)
    site: Optional[HttpUrl] = None


class Item(BaseModel):
    """Modelo para representar uma lista de itens com suas especificações técnicas.

    Esta classe serve como um contêiner para agrupar múltiplas especificações técnicas
    relacionadas a um determinado item ou conjunto de itens.

    Attributes:
        name (str): Nome identificador do conjunto de itens.
        especificacoes_tecnicas (List[ItemValidator]): Lista de especificações técnicas
            para cada item do conjunto.

    Example:
        >>> specs = [
        ...     ItemValidator(
        ...         item="Computador Desktop",
        ...         fabricante="Dell",
        ...         modelo="OptiPlex 5090",
        ...         descricao="Computador Desktop com processador Intel Core i7",
        ...         tecnologia="Intel vPro",
        ...         quantidade=10,
        ...         sustentabilidade="Energy Star 8.0",
        ...         normas="ISO 9001"
        ...     )
        ... ]
        >>> item_list = Item(name="Equipamentos TI", especificacoes_tecnicas=specs)
    """
    name: str
    especificacoes_tecnicas: List[ItemValidator]