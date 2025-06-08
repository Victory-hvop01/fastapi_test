from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/users")
async def get_users():
    return [{"id":1, "name":"Vika"}]

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True, host="0.0.0.0")

