""" Simple fizzbuzz REST API """
import json
import gzip
from flask import Flask, request, jsonify, make_response
from raccoon import raccoon_api

app = Flask(__name__)
app.register_blueprint(raccoon_api)

# Homepage
@app.route("/", methods=["GET"])
def homepage():
    """ Homepage """
    return 'Hello Anaelle'

@app.route('/fizzbuzz', methods=['GET'])
def get_fizzbuzz():
    """ Endpoint that returns a list of strings with numbers from 1 to limit
        all multiple of int1 are replaced by str1
        all multiples of int2 are replaced by str2
        all multiples of int1 and int2 are replaced by str1str2
    """
    # get params passed through the url
    int1 = request.args.get('int1', type = int)
    int2 = request.args.get('int2', type = int)
    limit = request.args.get('limit', type = int)
    str1 = request.args.get('str1', type = str)
    str2 = request.args.get('str2', type = str)

    # verify that no arguments are None
    if [x for x in (int1, int2, limit, str1, str2) if x is None]:
        return make_response(jsonify("Error: arguments cannot be None"), 400)
    # prevent from having negative numbers passed
    if int1 <= 0 or int2 <= 0 or limit <= 0:
        return make_response(jsonify("Error: given number must be greater than 0"), 400)
    # check if str1 and str2 are correct
    if str1 != "fizz" or str2 != "buzz":
        return make_response(jsonify("Error: wrong strings were given"), 400)

    # Fizzbuzz logic
    # pylint: disable=no-else-continue
    fizzbuzz = []
    for i in range(1, limit+1):
        if i % int1 == 0 and i % int2 == 0:
            fizzbuzz.append(str1 + str2)
            continue
        elif i % int1 == 0:
            fizzbuzz.append(str1)
            continue
        elif i % int2 == 0:
            fizzbuzz.append(str2)
            continue
        else:
            fizzbuzz.append(i)

    # compress result to get a lightweight response
    data = gzip.compress(json.dumps(fizzbuzz).encode('utf8'))

    res = make_response(data)

    # specify which encodings were applied to the message payload
    # and the length of the content
    res.headers['Content-Length'] = len(data)
    res.headers['Content-Encoding'] = 'gzip'
    return res

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
