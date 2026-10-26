
habits = []

def show_habits():
    if not habits:
        print("No habits added yet.")
        return

    for index, habit in enumerate(habits, start=1):
        status = "Done" if habit["completed"] else "Pending"
        print(f"{index}. {habit['name']} - {status}")


def add_habit():
    name = input("Enter a habit: ").strip()

    if name:
        habits.append({
            "name": name,
            "completed": False
        })
        print("Habit added successfully!")
    else:
        print("Habit name cannot be empty.")


def complete_habit():
    show_habits()

    if not habits:
        return

    try:
        number = int(input("Enter habit number to mark done: "))

        if 1 <= number <= len(habits):
            habits[number - 1]["completed"] = True
            print("Habit marked as completed!")
        else:
            print("Invalid habit number.")

    except ValueError:
        print("Please enter a valid number.")


def show_progress():
    total = len(habits)
    completed = sum(habit["completed"] for habit in habits)

    if total == 0:
        print("Add habits to track your progress.")
        return

    percentage = (completed / total) * 100

    print(f"Completed: {completed}/{total}")
    print(f"Daily progress: {percentage:.1f}%")


while True:
    print("\n--- DAILY HABIT TRACKER ---")
    print("1. Add habit")
    print("2. View habits")
    print("3. Mark habit completed")
    print("4. Show progress")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_habit()
    elif choice == "2":
        show_habits()
    elif choice == "3":
        complete_habit()
    elif choice == "4":
        show_progress()
    elif choice == "5":
        print("Keep building good habits. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
