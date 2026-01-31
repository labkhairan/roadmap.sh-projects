# Task Tracker CLI 

This is a simple **Command Line Interface (CLI)** application that helps you manage your tasks. You can add, update, delete, and list tasks, as well as filter tasks based on their status. Tasks are stored in a JSON file (`tasks.json`), which will be automatically created in the project directory when the application is first run.

## Features

- **Add tasks**: Create a new task with a description.
- **Update tasks**: Change the description.
- **Delete tasks**: Remove a task from the list.
- **Mark a task**: Mark a task as `in progress`, or `done`.
- **List tasks**: View all tasks, or filter them by status (`todo`, `in-progress`, or `done`).

## Getting Started

### Prerequisites

- **Python** installed on your machine (version 3 or higher).

### Installation

1. **Clone the repository** or download the `01-task-tracker.py` file to your project folder.

### Usage

You can interact with the Task Tracker using the following commands.

#### 1. **Add a Task**

```bash
./01-task-tracker.py add "<task_description>"
```

#### 2. **Update a Task's Description**

```bash
./01-task-tracker.py update <task_id> "<task_description>"
```

#### 3. **Delete a Task**

```bash
./01-task-tracker.py delete <task_id>
```

#### 4. **List All Tasks**

```bash
./01-task-tracker.py list
```

#### 5. **List Tasks by Status**

- To list all tasks that are todo:

    ```bash
    ./01-task-tracker.py list todo
    ```

- To list all tasks that are in-progress:

    ```bash
    ./01-task-tracker.pylist in-progress
    ```

- To list all tasks that are done:

    ```bash
    ./01-task-tracker.py list done
    ```

### Example Usage

```bash
# Adding a new task
./01-task-tracker.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
./01-task-tracker.py update 1 "Buy groceries and cook dinner"
./01-task-tracker.py delete 1

# Marking a task as in progress or done
./01-task-tracker.py mark-in-progress 1
./01-task-tracker.py mark-done 1

# Listing all tasks
./01-task-tracker.py list

# Listing tasks by status
./01-task-tracker.py list done
./01-task-tracker.py list todo
./01-task-tracker.py list in-progress

```


### Notes

- All tasks are stored in a `tasks.json` file located in the same directory as `01-task-tracker.py`.
- The `tasks.json` file will be created automatically when you first run the program.
- Make sure to run the commands from the directory where `task-tracker.py` is located, or provide the full path to the file.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).