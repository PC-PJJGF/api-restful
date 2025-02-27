from flask import Flask
from config import Config
from routes.user_routes import user_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)

def create_app():
    return app

def main():
    create_app()