import json
from jinja2 import Template
from app.config import settings

class PromptModule:
    def __init__(self, settings):
        self.settings = settings
        self.templates = {}
        for engine in ['openai', 'anthropic']:
            path = f"app/templates/{engine}.json"
            with open(path) as f:
                self.templates[engine] = json.load(f)

    async def generate(self, intent: str) -> str:
        engine = self.settings.DEFAULT_ENGINE
        tpl = self.templates.get(engine, self.templates['openai'])['prompt']
        return Template(tpl).render(intent=intent)