from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

class Settings(BaseSettings):
    # ... existing fields ...
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()

# Create async engine & session factory
engine = create_async_engine(settings.DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)