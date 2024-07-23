#pip install fastapi
#pip install uvicorn - servidor local


from fastapi import FastAPI

app = FastAPI()

#uvicorn FastAPI:app --reload -> colocar o site no ar(localmente), nome do arq:variavel
#o reload serve pra q qualquer alteraçao q for feita, ele vai jogar p api

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750mL", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}

#Criando rotas

@app.get("/") #quando entrar no caminho padrao, vai rodar a funçao home
def home():
    return {"Vendas": len(vendas)}

#se colocar a variavel no decorator, tem q passar ela na funçao
@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID venda inexistente"}