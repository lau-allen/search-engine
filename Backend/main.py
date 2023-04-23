from typing import Union
from enum import Enum
from fastapi import FastAPI

app = FastAPI()



class Engine(str, Enum):
    ggl = "Google"
    bng = "Bing"
    yho = "Yahoo"
    ddg = "DuckDuckGo"

@app.get("/")
def read_root():
    return {"Backend": "testing"}

@app.post("/search")
async def search_query(query: Union[str, None] = None):
    query = query*2
    return {"q": query}

@app.post("/populate")
async def populate_DB(search_engine: Engine=Engine.bng, query: Union[str, None] = None):
    return f'searching {query} in {search_engine}'