from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import  declarative_base, sessionmaker

from config.dev_settings import  get_settings

# engine = create_async_engine(get_settings().DATABASE_URL, echo=True)
engine = create_async_engine(get_settings().DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
