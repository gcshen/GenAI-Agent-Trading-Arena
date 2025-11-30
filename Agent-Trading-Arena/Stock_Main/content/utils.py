import os

## NOTE ===========
# Prefer environment variables so OpenRouter keys are not hardcoded.
# Intentionally default to empty to avoid leaking secrets.
openrouter_api_key = os.getenv("OPENROUTER_API_KEY", "")
openrouter_base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

openai_api_key = os.getenv("OPENAI_API_KEY", "")
openai_base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

llm_provider = os.getenv("LLM_PROVIDER", "openrouter")  # or "openai"

default_model = os.getenv("OPENROUTER_MODEL", "openai/gpt-5-mini")
key_owner = os.getenv("KEY_OWNER", "unknown")  # for OpenRouter usage tracking

## ================

# Optional offline switch to skip network calls and use deterministic fallbacks
offline_mode = os.getenv("OFFLINE_MODE", "").lower() in {"1", "true", "yes"}

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

# Verbose
debug = True
