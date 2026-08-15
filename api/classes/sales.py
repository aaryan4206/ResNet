from flask import jsonify
from flask.views import MethodView
from bson import ObjectId
from bson.errors import InvalidId


class SalesAPI(MethodView):
    def __init__(self, db):
        self.collection = db.get_collection("Sales")

    def get(self, sale_id=None):
        if sale_id is None:
            sales = list(self.collection.find({}))
            for d in sales:
                d["_id"] = str(d["_id"])
            return jsonify(sales), 200
        else:
            try:
                sale = self.collection.find_one({"_id": ObjectId(sale_id)})
                if not sale:
                    return jsonify({"error": "Sale not found"}), 404
                sale["_id"] = str(sale["_id"])
                return jsonify(sale), 200
            except InvalidId:
                return jsonify({"error": "Invalid ID format"}), 400

    def post(self):
        data = {"Date":"03-08-2026", "Amount":"16000"}
        if not data:
            return jsonify({"error": "No data provided"}), 400

        result = self.collection.insert_one(data)
        return jsonify({"message": "Sale data stored", "id": str(result.inserted_id)}), 201

    def put(self, sale_id):
        try:
            data = {"Amount":"20000"}
            data.pop('_id', None)

            result = self.collection.update_one(
                {"_id": ObjectId(sale_id)},
                {"$set": data}
            )
            if result.matched_count == 0:
                return jsonify({"error": "Sale not found"}), 404
            return jsonify({"message": "Sale updated successfully"}), 200
        except InvalidId:
            return jsonify({"error": "Invalid ID format"}), 400

    def delete(self, sale_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(sale_id)})
            if result.deleted_count == 0:
                return jsonify({"error": "Sale not found"}), 404
            return jsonify({"message": "Sale deleted successfully"}), 200
        except InvalidId:
            return jsonify({"error": "Invalid ID format"}), 400