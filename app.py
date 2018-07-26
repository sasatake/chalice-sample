from chalice import Chalice, Response
from chalicelib.util.logger import getLogger

app = Chalice(app_name="chalice-sample")
app.debug = True


@app.route("/check", methods=["GET"], api_key_required=True, name='MyFunction')
def check():
    logger = getLogger("/check")
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
