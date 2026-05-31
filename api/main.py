from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="AI Film Studio",
    version="1.0.0"
)

app.include_router(
    router,
    prefix="/api"
)


@app.get("/")
def root():

    return {
        "name": "AI Film Studio",
        "status": "running",
        "version": "1.0.0"
    }
