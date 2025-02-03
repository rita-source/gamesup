from pydantic import BaseModel  

# Schéma pour créer un utilisateur
class UserCreate(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True  


# Schéma pour afficher un utilisateur (par exemple avec l'ID)
class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


# Schéma pour la réponse d'un jeu (Exemple d'une entité Game)
class Game(BaseModel):
    id: int
    title: str
    publisher: str

    class Config:
        orm_mode = True


# Schéma pour la commande (Order)
class Order(BaseModel):
    id: int
    user_id: int
    game_id: int

    class Config:
        orm_mode = True
