from flask import url_for

from web_app import app


@app.context_processor
def utility_processor():
    def static_versioned(filename):
        return url_for("static", filename=filename) + "?v=" + app.config["APP_VERSION"]
    def version_view():
        return app.config["APP_VERSION"]
    return dict(static_versioned=static_versioned, version_view=version_view)