import os
import functions_framework
import requests

# ❌ Secret Scanning 用: 本物と全く同じ形式のテスト用文字列
# (GitHubの正規表現に確実にマッチさせます)
FAKE_GCP_KEY = "AIzaSyA" + "B" * 32  # Google API Key 形式
FAKE_AWS_KEY = "AKIA" + "1234567890" + "ABCDEF"  # AWS Access Key ID 形式

@functions_framework.http
def hello_world(request):
    """Dangerous function for DevSecOps verification."""
    
    # ❌ CodeQL が 100% 反応する「最悪」のコード
    # ユーザー入力をそのまま Python で実行 (Remote Code Execution)
    user_code = request.args.get('code', 'print("hello")')
    eval(user_code) # 危険極まりない: CodeQL が確実に「重大」と判定します

    # ❌ コマンドインジェクション
    host = request.args.get('host', '8.8.8.8')
    os.system(f"ping -c 1 {host}")

    return "Processing completed."
