import os
import functions_framework
import requests

# ❌ Secret Scanning 用: より本物に近い形式のダミーAPIキー
# (GitHubの標準パターンにマッチしやすい形式)
GOOGLE_API_KEY = "AIzaSyB-8jK9L0M1N2O3P4Q5R6S7T8U9V0W1X2Y"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@functions_framework.http
def hello_world(request):
    """Extremely vulnerable function for DevSecOps demo."""
    
    # ❌ CodeQL (SAST) 用: 絶対に検知される OS Command Injection
    # ユーザー入力を直接 os.popen や subprocess.check_output に渡す
    target_host = request.args.get('host', '8.8.8.8')
    # 危険: "8.8.8.8; rm -rf /" のような攻撃が可能
    response = os.popen(f"ping -c 1 {target_host}").read()

    return {
        "message": "Ping result processed",
        "output": response,
        "requests_version": requests.__version__
    }
