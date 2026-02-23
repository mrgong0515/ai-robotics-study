from flask import (Flask, render_template)
from flask import render_template # flask server가 run되는 위치와 동일한
from flask import request # 요청 관련 처리 라이브러리
# reder_template : flask server가 run되는 위치와 동일한
# 위치에 있는 templates 폴더 내 html 문서를 load
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cal", methods=["GET"])
def cal():
    # get방식으로 data가 넘어온다
    if request.method == "GET":
        # args -> GET 방식
        num1 = request.args["num1"]
        num2 = request.args["num2"]
        result = int(num1) + int(num2)

    return f"{num1} + {num2} = {result}"   
    # key 값은 num1, num2다

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
