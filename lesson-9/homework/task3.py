import json
import csv

def load_tasks(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []

def save_tasks(file_name, tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\nTask List:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

def convert_json_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    if not tasks:
        return
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

    print(f"\nTasks converted to CSV and saved as {csv_file}")

task_file = "tasks.json"
csv_file = "tasks.csv"

tasks_data = load_tasks(task_file)
display_tasks(tasks_data)
calculate_statistics(tasks_data)
convert_json_to_csv(task_file, csv_file)
