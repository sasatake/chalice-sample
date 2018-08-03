from chalice import Chalice
from chalicelib.usecases.product import get_product as get_product_usecase
from chalicelib.util.util import safe_bool
import os

app = Chalice(app_name=os.getenv("APP_NAME", "chalice-test"))
app.debug = safe_bool(os.getenv("DEBUG", "0"))


@app.route("/product/{id}", methods=["GET"], api_key_required=True)
def get_product(id):
    return get_product_usecase(app.current_request.to_dict())
