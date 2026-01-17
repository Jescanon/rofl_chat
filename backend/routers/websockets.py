from fastapi import APIRouter, WebSocket, Query
from starlette.websockets import WebSocketDisconnect

from backend.service.auth import get_current_user
from backend.database.base import async_session

from backend.service.gemini import get_response_on_gemini

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str = Query(...)):
    async with async_session() as db:
        user = await get_current_user(token, db)

        if not user:
            await websocket.close(code=1008)
            return

        await websocket.accept()
        print(f"User '{user.username}' connected.")

        try:
            while True:
                data = await websocket.receive_text()
                print(f"Received from {user.username}: {data}")
                info = await get_response_on_gemini(db=db, msg=data, user=user)
                await websocket.send_text(info)

        except WebSocketDisconnect as e:
            print(f"User '{user.username}' disconnected. Code: {e.code}")