from flask import Blueprint, request, jsonify
import mysql.connector, json
from backend.config import Config

routes = Blueprint("routes", __name__)

def get_db_connection():
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )

@routes.route('/kirim-jawaban', methods=['POST'])
def kirim_jawaban():
    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO hasil_form (data_json) VALUES (%s)",
        [json.dumps(data)]
    )
    conn.commit()
    conn.close()

    return jsonify({'status': 'sukses'})
