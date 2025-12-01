import os

## NOTE ===========
# Prefer environment variables so OpenRouter keys are not hardcoded.
# Intentionally default to empty to avoid leaking secrets.
openrouter_api_key = os.getenv("OPENROUTER_API_KEY", "")
openrouter_base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

openai_api_key = os.getenv("OPENAI_API_KEY", "")
openai_base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

llm_provider = os.getenv("LLM_PROVIDER", "openai")  # or "openai"
llm_model = os.getenv("LLM_MODEL", "gpt-5-mini-2025-08-07")
key_owner = os.getenv("KEY_OWNER", "unknown")  # for usage tracking

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



'''

>>> --- myLog ---
---GPT Response---
Operation: buy, Stock name: C, Quantity: 44 shares, Investment Amount: $19,580.00, Best Buying Price: $445.00
---end of GPT Response---
Valid Response: None
---- repeat count: 0
Operation: buy, Stock name: C, Quantity: 44 shares, Investment Amount: $19,580.00, Best Buying Price: $445.00
    [Decision] person 1 buy decision: Operation: hold. Because output is None.
Valid Response: True
    [Decision] person 1 sell decision: Operation: hold, Stock name: B, The number of shares: 0, Best Selling Price: N/A
    [Decision] person 1 fallback buy 1 of A
    [Analysis] person 2 starting
Valid Response: False
    [Analysis] person 2 complete

>>> --- Codex --- 
That log is from the “fallback” block in Stock_Main/behavior.py (lines ~134-171). If the LLM’s buy and sell outputs both resolve to “hold” (your log shows “Because output is None.”), the code injects a tiny trade to keep the market moving:

If the person is cash-poor (cash < 2× minimum living expense) and has holdings, it trims a small % of the largest position (prints “fallback sell …”).
Otherwise, if the person has enough cash, it randomly picks an affordable stock and buys a small amount (prints “fallback buy …”).


'''
