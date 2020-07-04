from chalice import Chalice
from chalice import BadRequestError
from chalice import NotFoundError


app = Chalice(app_name="helloworld")
app.debug = True


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/hello/{name}")
def hello_name(name):
    # '/hello/james' -> {"hello": "james"}
    return {"hello": name}


# @app.route("/users", methods=["POST"])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {"user": user_as_json}


CITIES_TO_STATE = {
    "seattle": "WA",
    "portland": "OR",
}


@app.route("/cities/{city}")
def state_of_city(city):
    try:
        return {"state": CITIES_TO_STATE[city]}
    except:
        raise BadRequestError(
            "wrong city you can try, '%s'" % (", or ".join(CITIES_TO_STATE.keys()))
        )


@app.route("/change/{value}", methods=["PUT"])
def change_value(value):
    return {"value": value}


OBJECTS = {"new": {"new": "enwdata"}}


@app.route("/objects/{key}", methods=["GET", "PUT"])
def myobject(key):
    request = app.current_request
    print(request.json_body)
    if request.method == "PUT":
        OBJECTS[key] = request.json_body
    elif request.method == "GET":
        try:
            return {key: OBJECTS[key]}
        except KeyError:
            raise NotFoundError(key)
