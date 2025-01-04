from flask import render_template


def register_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/dice-selection", methods=["GET"])
    def dice_selection():
        return render_template("dice_selection.html")
