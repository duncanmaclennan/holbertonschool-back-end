#!/usr/bin/python3
""" returns info about employee TODO list progress using REST API """
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users").json()
    # gets list of users
    user_tasks = {}
    # create dictionary

    for user in users:
        # gets TODO list for each user
        user_id = str(user['id'])
        todos = requests.get(url + "/users/" + user_id + "/todos").json()
        user_todos = [{"username": user["username"], "task": todo["title"],
                       "completed": todo["completed"]} for todo in todos]
        # creates list of dictionaries with task info
        user_tasks[user_id] = user_todos

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file)
    # writes user_tasks dict to a JSON file
