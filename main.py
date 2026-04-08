import sqlite3
import os
from flask import Flask, request
import functions_framework

# ❌ Secret Scanning 用: 以前のシークレット露出はそのまま維持
FAKE_GCP_KEY = "AIzaSyA" + "B" * 32
FAKE_AWS_KEY = "AKIA" + "1234567890" + "ABCDEF"

app = Flask(__name__)

@app.route("/vulnerable")
def vulnerable():
    # ユーザーからの入力を取得
    user_id = request.args.get("id")
    file_name = request.args.get("file")

    # --- 脆弱性 1: SQL Injection ---
    # 文字列結合でクエリを作成しているため、CodeQLが確実に検出します
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id 
    cursor.execute(query)

    # --- 脆弱性 2: OS Command Injection ---
    # ユーザー入力をシェルコマンドに直接渡しているため、確実に検出します
    os.system("ls -l " + file_name)

    return "Process completed"

# Cloud Functions 用のデプロイメント・エントリポイント
@functions_framework.http
def hello_world(request):
    # Flaskのコンテキストを模して関数を呼び出し
    return vulnerable()

if __name__ == "__main__":
    app.run()
