from flask import Flask
from flask_restful import Resource, Api, reqparse

parser = reqparse.RequestParser()

class EmployeesList(Resource):
  def get(self):
    return EMPLOYEES
  def post(self):
    parser.add_argument("name")
    parser.add_argument("age")
    parser.add_argument("spec")
    args = parser.parse_args()
    employee_id = int(max(EMPLOYEES.keys())) + 1
    employee_id = '%i' % employee_id
    EMPLOYEES[employee_id] = {
      "name": args["name"],
      "age": args["age"],
      "spec": args["spec"],
      }
    return EMPLOYEES[employee_id], 201

class Employee(Resource):
  def get(self, employee_id):
    if employee_id not in EMPLOYEES:
      return "Not found", 404
    else:
      return EMPLOYEES[employee_id]
    
  def put(self, employee_id):
    parser.add_argument("name")
    parser.add_argument("age")
    parser.add_argument("spec")
    args = parser.parse_args()
    if employee_id not in EMPLOYEE:
      return "Record not found", 404
    else:
      employee = EMPLOYEE[employee_id]
      employee["name"] = args["name"] if args["name"] is not None else employee["name"]
      employee["age"] = args["age"] if args["age"] is not None else employee["age"]
      employee["spec"] = args["spec"] if args["spec"] is not None else employee["spec"]
      return employee, 200
    
  def delete(self, employee_id):
    if employee_id not in EMPLOYEES:
      return "Not found", 404
    else:
      del EMPLOYEES[employee_id]
      return ' ', 204
    
app = Flask(__name__)
api = Api(app)
EMPLOYEES = {'1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
            '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
            '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
            '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
            }

api.add_resource(EmployeesList, '/employees/')
api.add_resource(Employee, '/employees/<employee_id>')


if __name__ == "__main__":
    app.run(debug=False)
