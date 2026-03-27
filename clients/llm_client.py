import json
import requests
from config.settings import Settings


class LLMClient:
    def analyze_incident(self, prompt: str) -> dict:
        response = requests.post(
            f"{Settings.OLLAMA_BASE_URL}/api/generate",
            json={
                "model": Settings.OLLAMA_MODEL,
                "prompt": prompt,
                "format": "json",
                "stream": False,
                "keep_alive": Settings.OLLAMA_KEEP_ALIVE,
            },
            timeout=Settings.OLLAMA_TIMEOUT_SECONDS,
        )

        response.raise_for_status()
        data = response.json()
        content = data.get("response", "{}")
        return json.loads(content)