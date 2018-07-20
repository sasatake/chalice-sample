from chalice import Chalice, Response
from datetime import datetime
import logging
import json

# from chalicelib.services.top import main

app = Chalice(app_name="chalice-sample")
app.debug = True
app.log.setLevel(logging.INFO)


@app.route("/check", methods=["GET"], api_key_required=True)
def index():
    result = {
        "appId": 1,
        "app-name": app.app_name,
        "input": {
            "shop-id": 234,
            "product-id": 3000,
            "price": 200
        },
        "result": {
            "result": "NG",
            "product-id": 3000,
            "product-name": "テスト商品",
            "price": 180,
        },
        "timestamp": datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    }
    app.log.info(json.dumps(result))
    return Response(body=result, status_code=200)
