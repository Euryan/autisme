from flask import Flask
from flask_cors import CORS
from backend.routes import routes
from backend.face_routes import face_routes   # ⬅️ tambahin ini

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:3000", "http://localhost:8000"])  # tambahin kalau serve static pakai http.server

# register blueprint
app.register_blueprint(routes)
app.register_blueprint(face_routes)   # ⬅️ tambahin ini juga

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
