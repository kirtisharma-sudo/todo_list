# 📝 Simple To-Do List App
# Day 3 Project

tasks = []

while True:
    print("\n📋 TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        if not tasks:
            print("⚠️ No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("⚠️ No tasks to remove.")
        else:
            task_no = int(input("Enter task number to remove: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"🗑️ Removed: {removed}")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")