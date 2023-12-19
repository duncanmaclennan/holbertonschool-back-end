#!/usr/bin/python3
""" returns info about employee TODO list progress using REST API """
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]
    user = requests.get(url + "/users/{}".format(employee_id)).json()
    todos = requests.get(url + "/users/" + employee_id + "/todos").json()

    EMPLOYEE_NAME = user.get("name")

    TOTAL_NUMBER_OF_TASKS = len(todos)
    NUMBER_OF_DONE_TASKS = sum(1 for todo in todos if todo["completed"])
# each task that meets condition is counter as 1, then added all together
    print("Employee {} is done with tasks({}/{}):".format(
          EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    [print(f"\t {todo['title']}") for todo in todos if todo["completed"]]
