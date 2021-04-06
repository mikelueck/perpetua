import flask
import json
import bcrypt
from prometheus_flask_exporter import PrometheusMetrics


app = flask.Flask(__name__)
metrics = PrometheusMetrics(app)

# Imports the Google Cloud client library
#from google.cloud import logging

# Instantiates a client
#logging_client = logging.Client()

# The name of the log to write to
#log_name = "my-log"
# Selects the log to write to
#logger = logging_client.logger(log_name)

# The data to log
#text = "Hello, world!"

# Writes the log entry
#logger.log_text(text)

#print("Logged: {}".format(text))


@app.route("/gethash/<password>/")
def compute_passwords(password):
    salt = bcrypt.gensalt()
    result = flask.Response(
        response=json.dumps(
            {
                "salt": salt.hex(),
                "hash": bcrypt.hashpw(
                    password.encode('utf8'), salt
                ).hex(),
            }
        ),
        status=200,
        mimetype="application/json",
    )
    return result
