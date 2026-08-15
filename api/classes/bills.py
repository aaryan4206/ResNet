from flask import jsonify
from flask.views import MethodView
from bson import ObjectId
from bson.errors import InvalidId


class BillingAPI(MethodView):
    def __init__(self, db):
        self.collection = db.get_collection("Bills")

    def get(self, bill_id=None):
        if bill_id is None:
            bills = list(self.collection.find({}))
            for d in bills:
                d["_id"] = str(d["_id"])
            return jsonify(bills), 200
        else:
            try:
                bill = self.collection.find_one({"_id": ObjectId(bill_id)})
                if not bill:
                    return jsonify({"error": "Bill not found"}), 404
                bill["_id"] = str(bill["_id"])
                return jsonify(bill), 200
            except InvalidId:
                return jsonify({"error": "Invalid ID format"}), 400

    def post(self):
        data = {"Date/Time":"03-08-2026/16:35:56", "Items":{"Masala Dosa":{"Qty": "2", "Price":"120", "Total Price":"240"}}, "Total Amount":"240"}
        if not data:
            return jsonify({"error": "No data provided"}), 400

        result = self.collection.insert_one(data)
        return jsonify({"message": "Bill created successfully", "id": str(result.inserted_id)}), 201

    def put(self, bill_id):
        try:
            data = {"Items":{"Masala Dosa":{"Qty": "3", "Price":"120", "Total Price":"360"}}}
            data.pop('_id', None)

            result = self.collection.update_one(
                {"_id": ObjectId(bill_id)},
                {"$set": data}
            )
            if result.matched_count == 0:
                return jsonify({"error": "Bill not found"}), 404
            return jsonify({"message": "Bill updated successfully"}), 200
        except InvalidId:
            return jsonify({"error": "Invalid ID format"}), 400

    def delete(self, bill_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(bill_id)})
            if result.deleted_count == 0:
                return jsonify({"error": "Bill not found"}), 404
            return jsonify({"message": "Bill deleted successfully"}), 200
        except InvalidId:
            return jsonify({"error": "Invalid ID format"}), 400