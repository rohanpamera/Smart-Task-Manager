    def create_task(tasks):
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        tasks.append({"Name": name, "Description": description})
        print("Task created successfully!")
        return tasks

    def edit_task(tasks):
        name = input("Enter the name of the task you want to edit: ")
        for task in tasks:
            if task["Name"] == name:
                new_name = input("Enter new task name (press enter to skip): ")
                new_description = input("Enter new task description (press enter to skip): ")
                if new_name:
                    task["Name"] = new_name
                if new_description:
                    task["Description"] = new_description
                print("Task edited successfully!")
                break
        else:
            print("Task not found!")
        return tasks

    def delete_task(tasks):
        name = input("Enter the name of the task you want to delete: ")
        for i, task in enumerate(tasks):
            if task["Name"] == name:
                tasks.pop(i)
                print("Task deleted successfully!")
                break
        else:
            print("Task not found!")
        return tasks

    def show_tasks(tasks):
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for task in tasks:
                print("Name:", task["Name"])
                print("Description:", task["Description"])
                print()

    def save_tasks(tasks):
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task["Name"] + "," + task["Description"] + "\n")

    def load_tasks():
        try:
            with open("tasks.txt", "r") as f:
                tasks = []
                for line in f:
                    name, description = line.strip().split(",")
                    tasks.append({"Name": name, "Description": description})
        except FileNotFoundError:
            tasks = []
        return tasks

    def main():
        tasks = load_tasks()

        while True:
            print("\nTask Manager\n")
            print("1. Create a new task")
            print("2. Edit a task")
            print("3. Delete a task")
            print("4. Show all tasks")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                tasks = create_task(tasks)
            elif choice == "2":
                tasks = edit_task(tasks)
            elif choice == "3":
                tasks = delete_task(tasks)
            elif choice == "4":
                show_tasks(tasks)
            elif choice == "5":
                save_tasks(tasks)
                print("Exiting...")
                break
            else:
                print("Invalid choice! Try again.")

    if __name__ == "__main__":
        main()

