from fastapi import FastAPI
from routers import games, users, orders

app = FastAPI()

# Inclure les différentes routes
app.include_router(games.router)
app.include_router(users.router)
app.include_router(orders.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API des jeux de société !"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

