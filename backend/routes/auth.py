from flask import Blueprint, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)
DB_NAME = "database.db"

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    hashed = generate_password_hash(password)

    try:
        db = sqlite3.connect(DB_NAME)
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (email, password, role) VALUES (?,?,?)",
            (email, hashed, "user")
        )
        db.commit()
        return jsonify({"message": "User registered successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, password, role FROM users WHERE email=?",
        (email,)
    )
    user = cursor.fetchone()
    db.close()

    if user and check_password_hash(user[1], password):
        token = create_access_token(
            identity={"id": user[0], "role": user[2]}
        )
        return jsonify(access_token=token)

    return jsonify({"error": "Invalid credentials"}), 401

