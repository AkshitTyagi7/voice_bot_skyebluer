from fastapi import Request, FastAPI
import chatbot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["https://robertogo.000webhostapp.com/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chatbot")
async def read_root(request: Request):
    payload = await request.json()
    print(payload)
    if 'message' in payload:
        ints = chatbot.predict_class(payload['message'].lower())
        res = chatbot.get_response(ints, chatbot.intents)
        return {
            'result': res
        }
