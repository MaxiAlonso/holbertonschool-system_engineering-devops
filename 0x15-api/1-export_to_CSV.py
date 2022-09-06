#!/usr/bin/python3
"""
Sscript to export data in the CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    usrId = int(argv[1])
    todo_api_url = "https://jsonplaceholder.typicode.com/todos"
    todo_response = requests.get(todo_api_url).json()
    user_api_url = "https://jsonplaceholder.typicode.com/users/{}".\
        format(usrId)
    user_response = requests.get(user_api_url).json()
    with open("{}.csv".format(usrId), mode='w') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todo_response:
            if todo.get("userId") == usrId:
                USERNAME = user_response.get("username")
                TASK_COMPLETED_STATUS = todo.get("completed")
                TASK_TITLE = todo.get("title")
                writer.writerow([usrId, USERNAME, TASK_COMPLETED_STATUS,
                                TASK_TITLE])
