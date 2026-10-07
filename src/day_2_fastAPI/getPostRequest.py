from fastapi import FastAPI

app = FastAPI(title="My First API")


@app.get("/health")
def health():
    return {"status": "ready"}


@app.post("/items")
def create_item(item: dict):
    return {
        "message": "Item received successfully",
        "item": item,
    }