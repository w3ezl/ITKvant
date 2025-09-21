from web_app import app, db, models

db.connect()
model_classes = [getattr(models, name) for name in models.__all__ if name != "BaseModel"]
db.create_tables(model_classes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)