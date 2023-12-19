#!/usr/bin/python3
""" exports data in CSV format """
import csv
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

    USER_ID = user["id"]
    filename = "{}.csv".format(USER_ID)
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
# all fields should be enclosed in quotes

        for todo in todos:
            USERNAME = user["username"]
            TASK_COMPLETED_STATUS = str(todo["completed"])
            TASK_TITLE = todo["title"]
            writer.writerow([USER_ID, USERNAME,
                            TASK_COMPLETED_STATUS, TASK_TITLE])
