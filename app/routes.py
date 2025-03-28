from flask import render_template, request
import logging

logger = logging.getLogger(__name__)


def register_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/dice-selection", methods=["GET", "POST"])
    def dice_selection():
        logger.info("Dice selection page loading")
        if request.method == "POST":
            logger.info("Post request received on dice selection page.")

            dice_type = request.form.get("dice_type")
            roll_type = request.form.get("roll_type")

            logger.info(
                f"Dice selected as {dice_type} and roll type selected as {roll_type}"
            )

            if dice_type == "regular":
                return render_template("regular_catan.html")
            else:
                return render_template("cities_and_knights.html")

        return render_template("dice_selection.html")
