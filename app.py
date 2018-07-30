from chalice import Chalice, Response
from chalicelib.util.logger import getLogger
from chalicelib.util.util import safe_bool
import os

app = Chalice(app_name=os.getenv("APP_NAME", "chalice-test"))
app.debug = safe_bool(os.getenv("DEBUG", "0"))
logger = getLogger(app.app_name)


@app.route("/check", methods=["GET"], api_key_required=True)
def check():
    result = {
        "response_code": 200,
        "input": {
            "shop_id": 234,
            "product_id": 3000,
            "price": 200
        },
        "result": {
            "result": "NG",
            "product_id": 3000,
            "product_name": "テスト商品",
            "price": 180,
        },
    }
    logger.info(result)
    return Response(body=result, status_code=200)
