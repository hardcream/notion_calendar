import uvicorn

from src.calendar.app import get_app


if __name__ == '__main__':
    app = get_app()
    uvicorn.run(app)