from app.adapters.openai_adapter import OpenAIAdapter
from app.adapters.anthropic_adapter import AnthropicAdapter
from app.config import settings

class QAModule:
    def __init__(self, settings):
        self.settings = settings
        self.adapters = {
            'openai': OpenAIAdapter(settings.OPENAI_API_KEY),
            'anthropic': AnthropicAdapter(settings.ANTHROPIC_API_KEY),
        }

    async def answer(self, message: str) -> str:
        engine = self.settings.DEFAULT_ENGINE
        adapter = self.adapters.get(engine)
        if not adapter:
            adapter = self.adapters['openai']
        return await adapter.send(message)