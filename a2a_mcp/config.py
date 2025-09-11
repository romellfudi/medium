from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
import yaml

class AzureDevOpsConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="AZURE_DO_", extra="allow")
    organization: str
    project: str
    pat: str
    client_id: str 
    tenant_id: str 
    secret: str 

class AzureConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="AZURE_OPENAI_", extra="allow")
    api_key: str
    api_version: str
    base_url: str
    model_name: str
    model_temperature: float
    embedding_model: str
    
class ModelSettings(BaseModel):
    model_temperature: float

class Neo4jConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="NEO4J_", extra="allow")
    url: str
    password: str

class MongoDBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="MONGO_DB_", extra="allow")
    user: str
    password: str
    cluster_name: str

class Prompts(BaseSettings):
    azure_agent_system_prompt: str
    calendar_agent_system_prompt: str
    orchestrator_follow_steps: str
    orchestrator_response: dict[str, str]
    orchestrator_system_prompt: str
    optimizer: str
    optimizer_agent_system_prompt: str
    outlook_agent_system_prompt: str
    
    def __init__(self):
        config_data = yaml.safe_load(open("config.yaml"))
        super().__init__(**config_data)


class SaiaConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="SAIA_AI_", extra="allow")
    api_key: str
    base_url: str
     
class CorpConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="CORP_GEAI_", extra="allow")
    api_key: str
    base_url: str

prompts = Prompts()
azure_config = AzureConfig()
model_settings = ModelSettings(model_temperature=azure_config.model_temperature,)
#neo4j_config = Neo4jConfig()
#mongodb_config = MongoDBConfig()
azure_devops_config = AzureDevOpsConfig()
saia_config = SaiaConfig()
corp_config = CorpConfig()