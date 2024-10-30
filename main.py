from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routes import router
from .config import Config
from .services import openai_service
from .utils import openai_utils
from .models import base
from . import dependencies

app = FastAPI(
    title="OpenAI Python Wrapper",
    description="A backend service for seamless OpenAI API integration.",
    version="1.0.0",
    debug=Config.DEBUG,
)

# Configure CORS for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes defined in the 'routes.py' module
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    await base.database.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await base.database.disconnect()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "detail": exc.detail,
    }

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return {
        "detail": f"An unexpected error occurred: {exc}",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)