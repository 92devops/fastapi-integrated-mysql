from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # DATABASE_URL: str = "sqlite+aiosqlite:///user.db"
    DATABASE_URL: str = "mysql+asyncmy://root:rootPwd@127.0.0.1:13306/testdb"

@lru_cache()
def get_settings():
    return Settings()