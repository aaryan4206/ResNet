# Libraries
import os
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
import certifi
from dotenv import load_dotenv
from api.routes import create_dealers_blueprints, create_employees_blueprints, create_sales_blueprints, create_bills_blueprints, create_menu_blueprints


# Initializing .env reader
load_dotenv()

# Initializing flask app
app = Flask(__name__)
CORS(app)

# Initializing MongoDB connection
MONGO_URI = os.environ.get("MONGODB_URI")
if MONGO_URI:
    client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
    db = client.get_database("ResNetDB")

# Initializing class blueprints
employees_blueprint = create_employees_blueprints(db)
app.register_blueprint(employees_blueprint)

dealers_blueprint = create_dealers_blueprints(db)
app.register_blueprint(dealers_blueprint)

sales_blueprint = create_sales_blueprints(db)
app.register_blueprint(sales_blueprint)

menu_blueprint = create_menu_blueprints(db)
app.register_blueprint(menu_blueprint)

bills_blueprint = create_bills_blueprints(db)
app.register_blueprint(bills_blueprint)

if __name__ == "__main__":
    app.run(port=5000, debug=True)