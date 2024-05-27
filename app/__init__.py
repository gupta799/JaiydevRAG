from flask import Flask
from flask_jwt_extended import JWTManager

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    jwt = JWTManager(app)
    # Register the routes
    with app.app_context():
        from prePocessing.preProcessing import runPreProcessing, getModel
        client = runPreProcessing()
        model = getModel()
        from app.routes import register_routes
        register_routes(app,client,model)

    return app