from flask import Blueprint, request, jsonify
import sqlite3

watchlist_bp = Blueprint("watchlist", __name__)

DB_NAME = "database.db"

@watchlist_bp.route("/add", methods=["POST"])
def add_to_watchlist():
    coin_id = request.json.get("coin_id")
    print("ADDING COIN:", coin_id)


    try:
        db = sqlite3.connect(DB_NAME)
        cursor = db.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO watchlist (coin_id) VALUES (?)",
            (coin_id,)
        )
        db.commit()
        return jsonify({"message": "Coin added to watchlist"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


@watchlist_bp.route("/all", methods=["GET"])
def get_watchlist():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT coin_id FROM watchlist")
    data = cursor.fetchall()
    db.close()

    coins = [row[0] for row in data]
    return jsonify(coins)

