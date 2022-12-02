from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DEBUGGER: bool = Field(False)
    VERSION: str = Field("0.0.0")
    TITLE: str = Field("Logging Prototipe")
    DESCRIPTION: str = Field("Logging Prototipe code")
    ENVIRONMENT: str = Field("dev")

    # logging
    LOGGING_MODE: str = Field("a")
    LOGGING_MAX_BYTES: int = Field(10000000)
    LOGGING_BACKUP_COUNT: int = Field(9)


settings: Settings = Settings()
