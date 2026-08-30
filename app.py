tasks = []


def add_task(task):
    tasks.append({"name": task, "completed": False})


def complete_task(index):
    tasks[index]["completed"] = True


def show_tasks():
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        print(f'{status} {task["name"]}')


add_task("Pythonを勉強する")
add_task("Gitを勉強する")
complete_task(0)

show_tasks()
