from fastapi import FastAPI
from routers import games, users, orders

app = FastAPI(
    title="BoardGames API",
    description="API pour la gestion d'un catalogue de jeux, utilisateurs et commandes.",
    version="1.0.0"
)

# Inclusion des routers
app.include_router(games.router, prefix="/games", tags=["Jeux"])
app.include_router(users.router, prefix="/users", tags=["Utilisateurs"])
app.include_router(orders.router, prefix="/orders", tags=["Commandes"])

# Point d'entrée de l'API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
