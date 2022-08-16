from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int  # deve ser maior que 12
    horas: int  # deve ser maior que 10


    @validator('titulo')
    def validar_titulo(cls, value: str):
        # validação 1
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError("O título deve ter pelo menos 3 palavras.")
        
        # validação 2
        if value.islower():
            raise ValueError("O título deve ser capitalizado.")

        return value

    
    # validação 3
    @validator('aulas')
    def validar_aulas(cls, value: int):
        if value <= 12:
            raise ValueError("O Curso deve ter pelo menos 12 aulas.")
        
        return value
    
    # validação 4
    @validator('horas')
    def validar_horas(cls, value: int):
        if value <= 10:
            raise ValueError("O Curso deve ter pelo menos 10 horas.")
        
        return value





cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=112, horas=58),
    Curso(id=1, titulo="Algoritmos e Lógica de Programação", aulas=87, horas=67),
]