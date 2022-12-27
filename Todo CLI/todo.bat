@echo off

:main
cls
echo ~~~ To-Do List ~~~
echo.
echo 1. Add a task
echo 2. View all tasks
echo 3. Update a task
echo 4. Delete a task
echo 5. Exit
echo.
set /p choice="Enter your choice: "

if %choice% == 1 goto add
if %choice% == 2 goto view
if %choice% == 3 goto update
if %choice% == 4 goto delete
if %choice% == 5 goto exit-todo

rem Add a new to-do list item
:add
set /p task="Enter a task to add to your to-do list: "
set /p description="Enter a description for the task: "
sqlite3 todo.db "INSERT INTO todo (task, description) VALUES ('%task%', '%description%');"
goto main

rem View all to-do list items
:view
cls
echo Your to-do list:
echo.
sqlite3 todo.db "SELECT * FROM todo;"
echo.
pause
goto main

rem Update a to-do list item
:update
cls
set /p id="Enter the ID of the task to update: "
set /p task="Enter the updated task: "
set /p description="Enter the updated description: "
sqlite3 todo.db "UPDATE todo SET task = '%task%', description = '%description%' WHERE id = %id%;
goto main

rem Delete a to-do list item
:delete
cls
set /p id="Enter the ID of the task to delete: "
sqlite3 todo.db "DELETE FROM todo WHERE id = %id%;
goto main

:exit-todo
cls
exit
