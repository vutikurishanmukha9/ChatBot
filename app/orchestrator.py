from app.db.models import QueryLog, Base
from app.config import AsyncSessionLocal, engine
# at module top, ensure tables exist
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

class Orchestrator:
    def __init__(self, settings):
        self.settings = settings
        self.redis = aioredis.from_url(settings.REDIS_URL)
        self.qa = QAModule(settings)
        self.prompt_gen = PromptModule(settings)
        # initialize tables
        import asyncio; asyncio.create_task(init_models())

    async def route(self, message: str, mode: str) -> str:
        # ... existing cache & generation logic ...
        # After obtaining `out`:
        # persist to DB
        async with AsyncSessionLocal() as session:
            log = QueryLog(
                engine=self.settings.DEFAULT_ENGINE,
                mode=mode,
                prompt=message,
                response=out
            )
            session.add(log)
            await session.commit()
        return out