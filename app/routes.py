from flask import  current_app, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import numpy as np

def register_routes(app,client,model):
    @app.route('/login', methods=['POST'])
    def login():
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        # Check if the user exists and the password matches
        user = next((u for u in current_app.config['USERS'] if u['username'] == username), None)
        if user and user['password']== password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        else:
            return jsonify({"msg": "Bad username or password"}), 401
        
    @app.route('/about',methods=['POST'])
    @jwt_required()
    def about():
        current_user = get_jwt_identity()
        data = request.get_json()
        question =data['question']
        query_vector = model.get_text_embedding(question)
        # Execute the query
        query_vector_bytes = np.array(query_vector, dtype=np.float32).tobytes()
        return query_vector,200
