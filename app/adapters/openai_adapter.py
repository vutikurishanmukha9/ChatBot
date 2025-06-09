import openai

class OpenAIAdapter:
    def __init__(self, api_key):
        openai.api_key = api_key

    async def send(self, prompt: str) -> str:
        resp = await openai.ChatCompletion.acreate(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return resp.choices[0].message.content