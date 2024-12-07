from pydantic import BaseModel, Field, HttpUrl, ValidationError
from typing import List, Optional


class ItemValidator(BaseModel):
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
    """Nome dos itens"""

    name: str
    especificacoes_tecnicas: List[ItemValidator]