from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/sample_response', methods=['GET'])
def sample_response():
    mess = request.args.get('id', default=None)
    
    if mess is not None:
        response_data = {'message': 'This is a sample response 2', 'status': mess}
        status_code = 200  # 200 OK
    else:
        response_data = {'message': 'No "id" parameter provided', 'status': 'error'}
        status_code = 404  # 404 Not Found
    
    return jsonify(response_data), status_code

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv("PORT", 5000))
