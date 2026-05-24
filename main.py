from fastapi import FastAPI

from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from agents.coordinator import coordinator

from memory.memory_store import save_memory


app=FastAPI()

app.add_middleware(

CORSMiddleware,

allow_origins=["*"],

allow_methods=["*"],

allow_headers=["*"]

)


class Prompt(BaseModel):

    prompt:str


@app.get("/")

def home():

    return {

        "message":

        "NeuroSync Running"

    }


@app.post("/chat")

def chat(data:Prompt):

    response=coordinator(
        data.prompt
    )

    save_memory(

        data.prompt,

        response

    )

    return {

        "response":

        response

    }