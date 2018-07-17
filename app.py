from chalice import Chalice

app = Chalice(app_name='chalice-sample')


@app.route('/')
def index():
    return {'hello': 'world'}
