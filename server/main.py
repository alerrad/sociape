import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from routes import link_router, user_router


# Load .env file
load_dotenv()

app = FastAPI()

# Register API routes
app.include_router(user_router, prefix="/api")
app.include_router(link_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app)
