from flask import jsonify
from flask.views import MethodView
from bson import ObjectId
from bson.errors import InvalidId


class MenuAPI(MethodView):
    def __init__(self, db):
        self.collection = db.get_collection("Menu")

    def get(self, menu_id=None):
        if menu_id is None:
            menu_items = list(self.collection.find({}))
            for d in menu_items:
                d["_id"] = str(d["_id"])
            return jsonify(menu_items), 200
        else:
            try:
                menu_item = self.collection.find_one({"_id": ObjectId(menu_id)})
                if not menu_item:
                    return jsonify({"error": "Item not found"}), 404
                menu_item["_id"] = str(menu_item["_id"])
                return jsonify(menu_item), 200
            except InvalidId:
                return jsonify({"error": "Invalid ID format"}), 400

    def post(self):
        data = {"Item Name":"Masala Dosa", "Item Type":"South Indian", "Price":"120"}
        if not data:
            return jsonify({"error": "No data provided"}), 400

        result = self.collection.insert_one(data)
        return jsonify({"message": "Item created", "id": str(result.inserted_id)}), 201

    def put(self, menu_id):
        try:
            data = {"Item Name":"Rava Masala Dosa", "Price":"140"}
            data.pop('_id', None)

            result = self.collection.update_one(
                {"_id": ObjectId(menu_id)},
                {"$set": data}
            )
            if result.matched_count == 0:
                return jsonify({"error": "Item not found"}), 404
            return jsonify({"message": "Item updated successfully"}), 200
        except InvalidId:
            return jsonify({"error": "Invalid ID format"}), 400

    def delete(self, menu_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(menu_id)})
            if result.deleted_count == 0:
                return jsonify({"error": "Item not found"}), 404
            return jsonify({"message": "Item deleted successfully"}), 200
        except InvalidId:
            return jsonify({"error": "Invalid ID format"}), 400