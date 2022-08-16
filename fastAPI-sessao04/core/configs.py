from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base




class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "mysql+asyncmy://CursoFastAPI:senhaSenha.123@localhost/cursofastapi"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()