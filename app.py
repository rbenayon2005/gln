from flask import Flask, request, jsonify

app = Flask(__name__)

def validate_gln(gln):
    if len(gln) != 13 or not gln.isdigit():
        return False
    weights = [1, 3] * 6
    sum_of_weights = sum(int(gln[i]) * weights[i] for i in range(12))
    check_digit = (10 - (sum_of_weights % 10)) % 10
    return check_digit == int(gln[12])

@app.route('/validate_gln', methods=['POST'])
def validate_gln_endpoint():
    data = request.get_json()
    gln = data.get('gln')
    if gln and validate_gln(gln):
        return jsonify({'valid': True})
    else:
        return jsonify({'valid': False})

if __name__ == '__main__':
    app.run(debug=True)
