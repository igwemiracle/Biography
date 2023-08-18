from pathlib import Path
from fastapi.staticfiles import StaticFiles
import data.db_session as db_session
from fastapi import FastAPI
import uvicorn
from views import home

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


def main():
    configure(dev_mode=True)
    uvicorn.run(app, host="127.0.0.1", port=8080)


def configure(dev_mode: bool):
    configure_routes()


def configure_routes():
    app.include_router(home.router)


if __name__ == "__main__":
    main()
else:
    configure(dev_mode=False)
