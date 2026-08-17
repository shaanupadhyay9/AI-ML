from flask import Flask, jsonify , request

app = Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "department": "Coding",
        "salary": 50000
    },
    {
        "id": 2,
        "name": "Priya Mehta",
        "department": "Electronics",
        "salary": 55000
    },
    {
        "id": 3,
        "name": "Aarav Patel",
        "department": "Mechanical",
        "salary": 60000
    }
]


@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees), 200

@app.route("/employees1", methods=["POST"])
def add_employee():

    data = request.get_json()

    new_employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "department": data["department"],
        "salary": data["salary"]
    }

    employees.append(new_employee)

    return jsonify({
        "message": "Employee created successfully",
        "employee": new_employee
    }), 201
    
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):

    data = request.get_json()

    for employee in employees:

        if employee["id"] == employee_id:

            employee["name"] = data.get(
                "name",
                employee["name"]
            )

            employee["department"] = data.get(
                "department",
                employee["department"]
            )

            employee["salary"] = data.get(
                "salary",
                employee["salary"]
            )

            return jsonify({
                "message": "Employee updated successfully",
                "employee": employee
            }), 200

    return jsonify({
        "error": "Employee not found"
    }), 404
    
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):

    for employee in employees:

        if employee["id"] == employee_id:

            employees.remove(employee)

            return jsonify({
                "message": "Employee deleted successfully"
            }), 200

    return jsonify({
        "error": "Employee not found"
    }), 404



if __name__ == "__main__":
    app.run(debug=True)
    