#!/bin/bash

# function to create a new task
function createTask() {
  read -p "Enter task name: " name
  read -p "Enter task description: " desc

  # insert new task into the tasks table in the todo.db database
  sqlite3 todo.db "insert into todo (task, description) values ('$name' ,'$desc')"
  echo "Task created successfully."
}

# function to read all tasks
function readTasks() {
  # select all tasks from the tasks table in the todo.db database and print them
  sqlite3 todo.db "select * from todo"
}

# function to update a task
function updateTask() {
  read -p "Enter task ID: " id
  read -p "Enter updated task name: " name
  read -p "Enter updated task description: " desc

  # update the task with the specified ID in the tasks table in the todo.db database
  sqlite3 todo.db "update todo set task = '$name', description = '$desc' where id = $id"
  echo "Task updated successfully."
}

# function to delete a task
function deleteTask() {
  read -p "Enter task ID: " id

  # delete the task with the specified ID from the tasks table in the todo.db database
  sqlite3 todo.db "delete from todo where id = $id"
  echo "Task deleted successfully."
}

# display menu
echo "CRUD To-Do CLI"
echo "1. Create Task"
echo "2. Read Tasks"
echo "3. Update Task"
echo "4. Delete Task"
echo "5. Exit"

# get user input
read -p "Enter your choice [1-5]: " choice

# take action based on user input
case $choice in
  1)
    createTask
    ;;
  2)
    readTasks
    ;;
  3)
    updateTask
    ;;
  4)
    deleteTask
    ;;
  5)
    exit
    ;;
  *)
    echo "Invalid choice. Please try again."
    ;;
esac
