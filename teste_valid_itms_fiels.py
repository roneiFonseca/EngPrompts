# Import Guard and Validator
from guardrails import Guard
from valid_items_field import ItemValidator

# Dados de teste para validação
valid_item = {
    "item": "Televisor 85 polegadas",
    "descricao": "Televisor LED 85'' com resolução 4K UHD e taxa de atualização de 120Hz.",
    "tecnologia": "LED, 4K UHD, HDR10",
    "quantidade": 5,
    "fabricante": "Samsung",
    "sustentabilidade": "Produto certificado com selo Energy Star.",
    "normas": ["ABNT NBR 15129", "ISO 9001"],
    "modelo": "QLED85Q80A",
    "site": "https://www.samsung.com/br/televisor85",
}

invalid_item = {
    "item": "Televisor 85 polegadas",
    "descricao": "",  # Empty description (invalid)
    "tecnologia": "LED, 4K UHD, HDR10",
    "quantidade": 0,  # Invalid quantity (must be > 0)
    "fabricante": "Samsung",
    "sustentabilidade": "Produto certificado com selo Energy Star.",
    "normas": ["ABNT NBR 15129", "ISO 9001"],
    "modelo": "QLED85Q80A",
    "site": "not-a-valid-url",  # Invalid URL
}

# Test valid item
# try:
#     result = ItemValidator(**valid_item)
#     print("Valid item passed validation:", result)
# except Exception as e:
#     print("Error validating valid item:", str(e))

# Test invalid item
try:
    result = ItemValidator(**invalid_item)
    print("Invalid item passed validation:", result)
except Exception as e:
    print("Error validating invalid item:", str(e))
