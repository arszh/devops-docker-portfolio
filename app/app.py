import os
from flask import Flask, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://devops:devops_password@db:5432/devops_portfolio",
)

engine = create_engine(DATABASE_URL, echo=False, future=True)

def init_db():
    with engine.begin() as conn:
        conn.execute(
            text(
                '''
                CREATE TABLE IF NOT EXISTS visits (
                    id SERIAL PRIMARY KEY,
                    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                '''
            )
        )

@app.before_first_request
def setup():
    init_db()

@app.route("/")
def index():
    with engine.begin() as conn:
        conn.execute(text("INSERT INTO visits DEFAULT VALUES;"))
        result = conn.execute(text("SELECT COUNT(*) FROM visits;"))
        count = result.scalar_one()
    return jsonify({"message": "DevOps Docker Portfolio App","visits_total": count})

@app.route("/health")
def health():
    try:
        with engine.begin() as conn:
            conn.execute(text("SELECT 1;"))
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500
