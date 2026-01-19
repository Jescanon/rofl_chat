from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers.registration import router
from backend.routers.user import router as user_router
from backend.routers.websockets import router as websockets_router

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(user_router)
app.include_router(websockets_router)
