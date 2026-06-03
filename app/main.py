from fastapi import FastAPI, Depends


def get_message():
    return "Hello world from dependency"


def get_db():
    pass


app = FastAPI()


@app.get("/")
def handle_root(message: str = Depends(get_message), db: str = Depends(get_db)):
    return {"message": "Hello world!"}
