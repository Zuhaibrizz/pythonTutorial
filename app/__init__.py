from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes.customer_shipment_routes import customer_shipment_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(customer_shipment_bp)

    return app
