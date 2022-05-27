from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

from car_factory import CarFactory
from model import Car

app = Flask(__name__)
metrics = PrometheusMetrics(app)

car_factory = CarFactory()

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')


@app.route("/produce/car")
def produce_car() -> Car:
    res = car_factory.produce()
    return jsonify(res.__dict__)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)
