from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorite_characters: Mapped[List["Character"]] = relationship(
        secondary = "favorite_character",
        back_populates="favorited_by")
    favorite_planets: Mapped[List["Planet"]] = relationship(
        secondary = "favorite_planet",
        back_populates="favorited_by")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

favorite_character = Table(
     "favorite_character",
     db.metadata,
     Column("user_id", ForeignKey("user.id")),
     Column("character_id", ForeignKey("character.id"))   
)    

favorite_planet = Table(
     "favorite_planet",
     db.metadata,
     Column("user_id", ForeignKey("user.id")),
     Column("planet_id", ForeignKey("planet.id"))  
)

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    age: Mapped[str] = mapped_column(String(120))
    planet_of_origin: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    favorited_by: Mapped[List["User"]] = relationship(
        secondary = "favorite_character",
        back_populates="favorite_characters")

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "age": self.age,
            "planet_of_origin": self.planet_of_origin.serialize
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    density: Mapped[str] = mapped_column(String(120))
    population: Mapped[str] = mapped_column(String(120))
    favorited_by: Mapped[List["User"]] = relationship(
        secondary ="favorite_planet",
        back_populates="favorite_planets")
    
    def serialize(self):
         return {
            "id": self.id,
            "density": self.density,
            "population": 
        }
        
        


