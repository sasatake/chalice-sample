from chalice import Chalice
from chalicelib.services.top import main

app = Chalice(app_name='chalice-sample')


@app.route('/')
def index():
    return main()
