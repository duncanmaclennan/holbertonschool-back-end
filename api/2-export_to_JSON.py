#!/usr/bin/python3
""" exports data in json format """
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]
    # get ID from command line
    user = requests.get(url + "/users/{}".format(employee_id)).json()
    todos = requests.get(url + "/users/" + employee_id + "/todos").json()
    # get user infro and TODO lists for specified user

    task_details = [{"task": todo["title"], "completed": todo["completed"],
                    "username": user["username"]} for todo in todos]
    # create list of dict with task info

    employee_data = {employee_id: task_details}
    # create dict with ID as key and tasks as values

    with open(f"{employee_id}.json", "w") as outfile:
        json.dump(employee_data, outfile)
    # write dict to JSON file
