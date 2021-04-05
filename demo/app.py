import flask
import json
import bcrypt

app = flask.Flask(__name__)


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
