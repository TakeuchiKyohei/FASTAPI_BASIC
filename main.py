from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI() #インスタンス化

# パスパラメータについて
# @app.get("/countries/{country_name}") #ルートパスにアクセスしたときの処理
# async def country(country_name: str): #型ヒントをベースにデータを制限できる
#     return {"country_name": country_name} 

# # クエリパラメータについて
# @app.get("/countries/") 
# async def country(country_name: str = "Japan", country_no: int = 1): 
#     return {
#         "country_name": country_name, 
#         "country_no": country_no
#     } 

# オプションパラメータについて
# @app.get("/countries/") 
# async def country(country_name: Optional[str] = None, country_no: Optional[int] = None): 
#     return {
#         "country_name": country_name, 
#         "country_no": country_no
#     } 

# リクエストボディについて(入れ子構造、バリデーション)
class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=20) 
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]

@app.post("/")
async def index(data: Data):
    return {
        "data": data
    }