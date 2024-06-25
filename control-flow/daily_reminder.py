# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
def get_reminder(task, priority, time_bound):
    if priority == "high":
        reminder = f"'{task}' is a high priority task"
    elif priority == "medium":
        reminder = f"'{task}' is a medium priority task"
    elif priority == "low":
        reminder = f"'{task}' is a low priority task"
    else:
        reminder = f"'{task}' has an unspecified priority level"
    
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    return reminder

# Generate and print the reminder
reminder_message = get_reminder(task, priority, time_bound)
print("\nReminder:", reminder_message)
