from flask import jsonify
from flask.views import MethodView
from bson import ObjectId
from bson.errors import InvalidId


class EmployeeAPI(MethodView):
    def __init__(self, db):
        self.collection = db.get_collection("Employees")

    def get(self, employee_id=None):
        if employee_id is None:
            employees = list(self.collection.find({}))
            for d in employees:
                d["_id"] = str(d["_id"])
            return jsonify(employees), 200
        else:
            try:
                employee = self.collection.find_one({"_id": ObjectId(employee_id)})
                if not employee:
                    return jsonify({"error": "Employee not found"}), 404
                employee["_id"] = str(employee["_id"])
                return jsonify(employee), 200
            except InvalidId:
                return jsonify({"error": "Invalid ID format"}), 400

    def post(self):
        data = {"Name":"Shivam", "Age":"22", "Contact No.":"9211290962", "Role":"Chef", "DOJ":"01-07-2026", "DOL":"07-08-2026", "Aadhaar No.":"987654321"}
        if not data:
            return jsonify({"error": "No data provided"}), 400

        result = self.collection.insert_one(data)
        return jsonify({"message": "Employee created", "id": str(result.inserted_id)}), 201

    def put(self, employee_id):
        try:
            data = {"Age":"20","Role":"Waiter"}
            data.pop('_id', None)

            result = self.collection.update_one(
                {"_id": ObjectId(employee_id)},
                {"$set": data}
            )
            if result.matched_count == 0:
                return jsonify({"error": "Employee not found"}), 404
            return jsonify({"message": "Employee updated successfully"}), 200
        except InvalidId:
            return jsonify({"error": "Invalid ID format"}), 400

    def delete(self, employee_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(employee_id)})
            if result.deleted_count == 0:
                return jsonify({"error": "Employee not found"}), 404
            return jsonify({"message": "Employee deleted successfully"}), 200
        except InvalidId:
            return jsonify({"error": "Invalid ID format"}), 400
