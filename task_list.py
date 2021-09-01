
tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Print a list of uncompleted tasks..

# def print_incomplete_tasks( list ):
#     uncompleted_tasks = []
#     for task in list:
#         if task["completed"] == False:
#             uncompleted_tasks.append(task)
    
#     return uncompleted_tasks

# print(print_incomplete_tasks( tasks ))


# Print a list of completed tasks..

# def print_complete_tasks( list ):
#     completed_tasks = []
#     for task in list:
#         if task["completed"] == True:
#             completed_tasks.append(task)
    
#     return completed_tasks

# print(print_complete_tasks( tasks ))


# Print a list of all task descriptions..

# def print_all_task_descriptions( list ):
#     all_task_descriptions = []
#     for task in list:
#             all_task_descriptions.append(task["description"])
        
#     return all_task_descriptions

# print(print_all_task_descriptions( tasks ))


# # Print a list of tasks where time_taken is at least a given time..

# def print_tasks_by_time_taken( list ):
#     tasks_by_time_taken = []
#     for task in list:
#         if task["time_taken"] <= 15:
#             tasks_by_time_taken.append(task)
    
#     return tasks_by_time_taken

# print(print_tasks_by_time_taken( tasks ))


# # Print any task with a given description..

# def print_task_by_description( list, task_description ):
#     for task in list:
#         if task["description"] == task_description:
#             return task
    
#     return "Task not listed"

# print(print_task_by_description( tasks, "Walk Dog" ))


# Extension..

# Given a description, update that task to mark it as complete.

# def mark_complete_by_description( list, task_description ):
#     for task in list:
#         if task["description"] == task_description:
#             task["completed"] = True
#             return task

# print(mark_complete_by_description( tasks, "Feed Cat" ))


# Add a task to the list.

# tasks.append({ "description": "Make Breakfast", "completed": True, "time_taken": 15 })

# print(tasks)

# Further Extensions..

# Use a while loop to display the following menu and allow the use to enter an option.

Use a while loop to display the following menu and allow the use to enter an option.
print("Menu:")
print("1: Display All Tasks")
print("2: Display Uncompleted Tasks")
print("3: Display Completed Tasks")
print("4: Mark Task as Complete")
print("5: Get Tasks Which Take Longer Than a Given Time")
print("6: Find Task by Description")
print("7: Add a new Task to list")
print("M or m: Display this menu")
print("Q or q: Quit")

# Call the appropriate function depending on the users choice.
