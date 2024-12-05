from typing import Any, Dict
from guardrails.logger import logger
from guardrails.validator_base import (
    FailResult,
    PassResult,
    ValidationResult,
    Validator,
    register_validator,
)
from pydantic import BaseModel, Field, HttpUrl, ValidationError
from typing import List, Optional

class ItemValidator(BaseModel):
    tem: str = Field(..., min_length=1)
    fabricante: str = Field(..., min_length=1)
    modelo: str = Field(..., min_length=1)
    descricao: str = Field(..., min_length=1)
    tecnologia: str = Field(..., min_length=1)
    quantidade: int = Field(..., gt=0)
    sustentabilidade: Optional[str] = None
    site: Optional[HttpUrl] = None

    # class Config:
    #     extra = "allow"


@register_validator(name="guardrails/valid_item_fields", data_type=["object"])
class ValidItemFields(Validator):
    """Validates the fields of an item object.

    **Key Properties**

    | Property                      | Description                                       |
    | ----------------------------- | ------------------------------------------------- |
    | Name for `format` attribute   | `guardrails/valid_item_fields`                   |
    | Supported data types          | `object`                                         |
    | Programmatic fix              | None                                             |
    """

    def validate(self, value: Any, metadata: Dict) -> ValidationResult:
        logger.debug(f"Validating fields for item: {value}")

        try:
            ItemValidator(**value)
            return PassResult()
        except ValidationError as e:
            return FailResult(error_message=str(e))
