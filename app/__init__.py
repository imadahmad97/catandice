from flask import Flask
import logging


def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info("Flask app is being created.")

    logger.info("Registering Routes")
    from .routes import register_routes

    register_routes(app)
    logger.info("Routes Registered")

    return app
