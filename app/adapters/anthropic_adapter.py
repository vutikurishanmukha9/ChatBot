import anthropic

class AnthropicAdapter:
    def __init__(self, api_key):
        self.client = anthropic.Client(api_key)

    async def send(self, prompt: str) -> str:
        resp = await self.client.completions.create(
            model="claude-3",  # or other Claude version
            prompt=prompt,
            max_tokens_to_sample=500,
            temperature=0.7
        )
        return resp.completion