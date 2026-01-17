from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    gemini_api: str = "!@#"
    base_url: str = "asunpg+hueta"
    secret: str = "НАХУЙИДИТВАРЬЧЕРНОЖЕПАЯ"

    model_config = SettingsConfigDict(
        env_file=".env"
    )

@lru_cache()
def get_all_settings() -> Settings:
    return Settings()
