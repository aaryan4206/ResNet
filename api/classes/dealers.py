from flask import jsonify
from flask.views import MethodView
from bson import ObjectId
from bson.errors import InvalidId


class DealerAPI(MethodView):
    def __init__(self, db):
        self.collection = db.get_collection("Dealers")

    def get(self, dealer_id=None):
        if dealer_id is None:
            dealers = list(self.collection.find({}))
            for d in dealers:
                d["_id"] = str(d["_id"])
            return jsonify(dealers), 200
        else:
            try:
                dealer = self.collection.find_one({"_id": ObjectId(dealer_id)})
                if not dealer:
                    return jsonify({"error": "Dealer not found"}), 404
                dealer["_id"] = str(dealer["_id"])
                return jsonify(dealer), 200
            except InvalidId:
                return jsonify({"error": "Invalid ID format"}), 400

    def post(self):
        data = {"Name":"Shivam", "Organisation":"Haldiram", "Items":"Namkeens", "Type":"Credit", "Status":"Clear", "Transaction History":{"03-08-2026":"3600","08-08-2026":"5000"}}
        if not data:
            return jsonify({"error": "No data provided"}), 400

        result = self.collection.insert_one(data)
        return jsonify({"message": "Dealer created", "id": str(result.inserted_id)}), 201

    def put(self, dealer_id):
        try:
            data = {"Items":"Dairy","Organisation":"Mother Dairy"}
            data.pop('_id', None)

            result = self.collection.update_one(
                {"_id": ObjectId(dealer_id)},
                {"$set": data}
            )
            if result.matched_count == 0:
                return jsonify({"error": "Dealer not found"}), 404
            return jsonify({"message": "Dealer updated successfully"}), 200
        except InvalidId:
            return jsonify({"error": "Invalid ID format"}), 400

    def delete(self, dealer_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(dealer_id)})
            if result.deleted_count == 0:
                return jsonify({"error": "Dealer not found"}), 404
            return jsonify({"message": "Dealer deleted successfully"}), 200
        except InvalidId:
            return jsonify({"error": "Invalid ID format"}), 400
