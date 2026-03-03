from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

print("**********")
print(Path(__file__).resolve().parents[1] / ".env")

class Settings(BaseSettings):
    database_url: str
    pythonpath: str
    model_config = SettingsConfigDict(env_file=Path(__file__).resolve().parents[1] / ".env")

env = Settings()

