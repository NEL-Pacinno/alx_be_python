#promt user for daily task reminder
task = input("Enter your task: ")
priority = input("Enter the priority (high, medium, low): ")
time_bound = input("Is this task time-bound? (yes/no): ")

#process the task using match-case
match priority.lower():
    case "high":
        print(f"High priority task: {task}")
    case "medium":
        print(f"Medium priority task: {task}")
    case "low":
        print(f"Low priority task: {task}")
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
if time_bound.lower() == "yes":
    print(f"Reminder: {task} is time-bound.")

#check if task is time bound
if time_bound == "yes":
    print(f"Reminder: {task} is a high priority task that requires immediate attention today.")
else:
    print(f"Reminder: {task} that you can schedule later.")
# This code prompts the user for a daily task reminder, including its priority and whether it is time-bound, and processes the input using Python's match-case statement.