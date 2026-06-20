# app.py - Flask 後端伺服器
# 負責提供靜態網頁，所有遊戲邏輯均在前端 JS 執行

import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """提供遊戲主頁面"""
    return render_template('index.html')

if __name__ == '__main__':
    # Railway 會透過環境變數 PORT 指定埠號，本機開發預設 5000
    port = int(os.environ.get('PORT', 5000))
    print(f"⚽ 足球遊戲伺服器啟動中... port={port}")
    print("本機遊玩：http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=port, debug=False)
