# filepath: backend/wsgi.py
from app import app

app = create_app()

if __name__ == "__main__":
    app.run()