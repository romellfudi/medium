from pydantic_settings import BaseSettings, SettingsConfigDict

class AzureConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="AZURE_OPENAI_", extra="allow")
    endpoint: str
    api_key: str
    model_name: str
    api_version: str
    embedding_model_name: str

azure_config = AzureConfig()