import requests
from datetime import datetime
from pydantic import BaseModel, Field
import pandas as pd

# Модель для валидации JSON
class DocumentsResponse(BaseModel):
    Columns: list[str]
    Description: str
    RowCount: int
    Rows: list[list[str]]

    class Config:
        fields = {
            "key1": "document_id",
            "key2": "document_dt",
            "key3": "document_name"
        }

# Получение JSON из API
today = datetime.now().timestamp()
url = f"https://api.gazprombank.ru/very/important/docs?documents_date={today}"
response = requests.get(url)
data = response.json()

# Валидация JSON
docs_response = DocumentsResponse(**data)

# Преобразование в DataFrame
columns = docs_response.Columns
rows = docs_response.Rows
df = pd.DataFrame(rows, columns=columns)

# Переименование столбцов
df = df.rename(columns=DocumentsResponse.Config.fields)

# Добавление столбца "load_dt"
df["load_dt"] = datetime.now()

print(df)