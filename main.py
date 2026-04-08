import os
import functions_framework
import requests

# ❌ シークレットスキャン用：ダミーのAPIキー（Push Protectionで弾かれるはず）
DUMMY_API_KEY = "AIzaSyA1234567890ExampleKeyForScanning"

@functions_framework.http
def hello_world(request):
    """Simple Cloud Function with intentional vulnerabilities."""
    
    # ❌ CodeQL (SAST) 用：OSコマンドインジェクションの脆弱性
    # ユーザー入力をそのままシェルコマンドに渡す極めて危険なコード
    cmd = request.args.get('cmd', 'echo hello')
    os.system(cmd) 

    return f"Executed: {cmd}. Requests version: {requests.__version__}"
