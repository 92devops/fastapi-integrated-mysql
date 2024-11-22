from fastapi import  FastAPI
from contextlib import  asynccontextmanager
from services.user import UserService

@asynccontextmanager
async def lifespan(app: FastAPI):
    await UserService.init_table()
    yield

app = FastAPI(
    title='FastAPI集成SQLAlchemy示例',
    description="关于该API文档一些描述信息补充说明",
    lifespan=lifespan,
)

from  api.user import router_user
app.include_router(router_user, prefix="/api", ) # /api/users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="127.0.0.1", port=8000)