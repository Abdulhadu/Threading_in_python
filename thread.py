
import threading
import time
import queue
import heapq 
import sys
from inputimeout import inputimeout, TimeoutOccurred


incomplete_tasks = []
priority_queue = []  

class Task:
    def __init__(self, name, priority, execution_time, dependencies=None):
        self.name = name
        self.priority = priority
        self.dependencies = dependencies or []
        self.state = "pending"
        self.execution_time = execution_time
        self.operations = [] 
        self.completed_event = threading.Event()
        self.operation_type = "addition" 
        # self.input_required = input_required  

    def add_operation(self, operation):
        self.operations.append(operation)

    def execute(self):
        
        self.state = "running"
        print(f"Task '{self.name}' (Priority {self.priority}) is running.")
        
       

        for operation in self.operations:
            operation(self) 
            
        if self.state == "paused":
            self.state = "completed"
            incomplete_tasks.append(self)   
            return
        
        self.state = "completed"
        self.completed_event.set()  
        print(f"Task '{self.name}' is completed.")



    def __lt__(self, other):
        return self.priority < other.priority 

# ------------------------- Function to Perform ------------------------
def addition_subtraction_operation(task):
    
    try:
        user_input = inputimeout(prompt=f"Enter two numbers separated by ',' for {task.name} (or press Enter to terminate): ", timeout=10)
        if not user_input: 
            print(f"No input provided for task '{task.name}'. Task marked as incomplete.")
            task.state = "paused"
            return None
    except TimeoutOccurred:
        print(f"No input provided for task '{task.name}' within 10 seconds. Task marked as incomplete.")
        task.state = "paused" 
        return None
    except KeyboardInterrupt:
        sys.exit("Input interrupted by the user.")
        
    if task.operation_type == "addition":
      if user_input:
        num1, num2 = map(int,  user_input.split(','))
        time.sleep(task.execution_time)
        result = num1 + num2 
        print(f"Addition result for {task.name}: {result}")
        1
    elif task.operation_type == "subtraction":
      
        num1, num2 = map(int,  user_input.split(','))
        time.sleep(task.execution_time)
        result = num1 - num2  
        print(f"Subtraction result for {task.name}: {result}")


def multiplication_operation(task):
    
    try:
        user_input = inputimeout(prompt=f"Enter two numbers separated by ',' for {task.name} (or press Enter to terminate): ", timeout=10)
        if not user_input: 
            print(f"No input provided for task '{task.name}'. Task marked as incomplete.")
            task.state = "paused" 
            return None
    except TimeoutOccurred:
        print(f"No input provided for task '{task.name}' within 10 seconds. Task marked as incomplete.")
        task.state = "paused" 
        return None
    except KeyboardInterrupt:
        sys.exit("Input interrupted by the user.")
        
    if user_input:
       num1, num2 =map(float, user_input.split(','))
        
    else:
        num1 = 6
        num2 = 2
      
    time.sleep(task.execution_time)
    result = num1 * num2  
    print(f"Multiplication result for {task.name}: {result}")

def division_operation(task):
    try:
        user_input = inputimeout(prompt=f"Enter two numbers separated by ',' for {task.name} (or press Enter to terminate): ", timeout=10)
        if not user_input: 
            print(f"No input provided for task '{task.name}'. Task marked as incomplete.")
            task.state = "paused"
            return None
    except TimeoutOccurred:
        print(f"No input provided for task '{task.name}' within 10 seconds. Task marked as incomplete.")
        task.state = "paused" 
        return None
    except KeyboardInterrupt:
        sys.exit("Input interrupted by the user.")
        
    if user_input:
        num1, num2 =map(float, user_input.split(','))
    else:
        num1 = 12
        num2 = 4
      
    time.sleep(task.execution_time)
    result = num1 / num2  
    print(f"Division result for {task.name}: {result}")

def display_task(task):
    print(f"{task.name} is executing for {task.execution_time} seconds")
    time.sleep(task.execution_time) 
    
    
def display_number_10_times(task):
    try:
        user_input = inputimeout(prompt=f"Enter single number for {task.name} (or press Enter to terminate): ", timeout=10)
        if not user_input: 
            print(f"No input provided for task '{task.name}'. Task marked as incomplete.")
            task.state = "paused"
            return None
    except TimeoutOccurred:
        print(f"No input provided for task '{task.name}' within 10 seconds. Task marked as incomplete.")
        task.state = "paused" 
        return None
    except KeyboardInterrupt:
        sys.exit("Input interrupted by the user.")
    if user_input:
        num1 =user_input
    else:
        num1 = 12
    print(f"{task.name} is executing for {task.execution_time} seconds")

    for _ in range(10):
        
        print(num1)
        
        
# ---------------------------------------------------------------------
        
        

def create_task_menu():
    while True:
        print("\nCreate Task Menu:")
        print("1. Add Task")
        print("2. Return to Main Menu")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task_submenu()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

def add_task_submenu():
    while True:
        print("\n_______________Task Menue______________")
        print("\nAdd Tasks from the given below options:")
        print("1. [Number Addition] task")
        print("2. [Number Mulitplication] task")
        print("3. [Number divisiion] task")
        print("4. [Print displaying] task")
        print("5. [Display 10 times] Task")
        print("6. Return to Create Task Menu")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_numbers_task()
        elif choice == "2":
            mulitplication_number_task()
        elif choice == "3":
            division_number_task()
        elif choice == "4":
            simple_display_task()
        elif choice == "5":
            add_display_number_10_times_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
            


# -------------------------------- Create different tasks ----------------------

def add_numbers_task():
    name = input("Enter task name: ")
    priority = int(input("Enter priority: "))
    execution_time = int(input("Enter execution time: "))
    
    try:
        task = Task(name, priority, execution_time)
        task.add_operation(addition_subtraction_operation)

        heapq.heappush(priority_queue, task)
        print("Task added Successfully...")
        
    except:
        print("Error occured in adding a new task!")



    
def add_display_number_10_times_tasks():
    name = input("Enter task name: ")
    priority = int(input("Enter priority: "))
    execution_time = int(input("Enter execution time: "))
    
    try:
        task = Task(name, priority, execution_time)
        task.add_operation(display_number_10_times)

        heapq.heappush(priority_queue, task)
        print("Task added Successfully...")
    
    except:
        print("Error occured in adding a new task!")
        
        



def mulitplication_number_task():
    name = input("Enter task name: ")
    priority = int(input("Enter priority: "))
    execution_time = int(input("Enter execution time: "))
    
    try:
        task = Task(name, priority, execution_time)
        task.add_operation(multiplication_operation)

        heapq.heappush(priority_queue, task)
        print("Task added Successfully...")
        
    except:
        print("Error occured in adding a new task!")
        
        
        

def division_number_task():
    name = input("Enter task name: ")
    priority = int(input("Enter priority: "))
    execution_time = int(input("Enter execution time: "))

    
    try:
        task = Task(name, priority, execution_time)
        task.add_operation(division_operation)

        heapq.heappush(priority_queue, task)
        print("Task added Successfully...")
        
    except:
        print("Error occured in adding a new task!")
        
        

    
def simple_display_task():
    name = input("Enter task name: ")
    priority = int(input("Enter priority: "))
    execution_time = int(input("Enter execution time: "))

    
    try:
        task = Task(name, priority, execution_time)
        task.add_operation(display_task)

        heapq.heappush(priority_queue, task)
        print("Task added Successfully...")
        
    except:
        print("Error occured in adding a new task!")
        


    
    
    
# --------------------------------------------------------------------
 

def list_tasks():
    print("\nList of All Tasks:")
    try:
        for task in priority_queue:
             print(f"Task Name: {task.name}, Priority: {task.priority}, Execution Time: {task.execution_time}")
    except:
        print("No Task Founnd ...!")
        
    
        
        
def delete_task():
    name = input("Enter the name of the task to delete: ")
    task_to_delete = None

    for task in priority_queue:
        if task.name == name:
            task_to_delete = task
            break

    if task_to_delete:
        priority_queue.remove(task_to_delete)
        print(f"Task '{name}' has been deleted.")
    else:
        print(f"Task '{name}' not found.")




def execute_task():
    global incomplete_tasks
    while priority_queue:
        task = heapq.heappop(priority_queue)
        task.execute()
        
        for dependency in task.dependencies:
            dependency.completed_event.wait()

    # Wait for the completion of incomplete tasks in a separate thread
    incomplete_task_thread = threading.Thread(target=task_to_handle)
    incomplete_task_thread.start()
    incomplete_task_thread.join()

    print("All tasks are completed.")

def task_to_handle():
    global incomplete_tasks
    while incomplete_tasks:
        task = incomplete_tasks.pop(0)
        task.execute()
        for dependency in task.dependencies:
            dependency.completed_event.wait()

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Create Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Execute Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_task_menu()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            execute_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            
            
            
if __name__ == "__main__":
    task_thread = threading.Thread(target=task_to_handle)
    task_thread.start()
    main_menu()
    
    
    
    
    
    
    
# def main():
#     main_menu()
    
#     global incomplete_tasks
#     while priority_queue:
#         task = heapq.heappop(priority_queue)
#         task.execute()
     
#         for dependency in task.dependencies:
#             dependency.completed_event.wait()

#     # Wait for the completion of incomplete tasks
#     for task in incomplete_tasks:
#         task.completed_event.wait()
#         task.execute()

#     # Clear the incomplete tasks list after execution
#     incomplete_tasks = []


#     # Check if there are still incomplete tasks
#     if incomplete_tasks:
#         print("There are incomplete tasks. Waiting for input or completion...")
#         for task in incomplete_tasks:
#             task.completed_event.wait()
#     else:
#         print("All tasks are completed.")
    

    # while priority_queue:
    #     task = heapq.heappop(priority_queue)  
    #     task.execute()
    #     for dependency in task.dependencies:
    #         dependency.completed_event.wait()
          
    # # task1.operation_type = "subtraction"
    # # task1.execute()

    # incomplete_task_thread = threading.Thread(target=task_to_handle)
    # incomplete_task_thread.start()
    # # Execute incomplete tasks
    # for task in incomplete_tasks:
    #   task.completed_event.wait()        
            


    
    
    
    
    
# def main():
#     incomplete_tasks = []
#     priority_queue = []  
#     # task1 = Task("Task1", priority, quantumsize, execution_time, input_required=True) 
#     task1 = Task("Task1", 1, 2, 5, input_required=True)  
#     task1.add_operation(addition_subtraction_operation) 
#     heapq.heappush(priority_queue, task1)

#     task2 = Task("Task2", 2, 1, 5, dependencies=[task1], input_required=True) 
#     task2.add_operation(multiplication_operation) 
#     heapq.heappush(priority_queue, task2)  


#     task3 = Task("Task3", 3, 3, 5)  
#     task3.add_operation(division_operation) 
#     heapq.heappush(priority_queue, task3)  

#     task4 = Task("Task4", 2, 3, 5)  
#     task4.add_operation(display_task) 
#     heapq.heappush(priority_queue, task4)  




#     while priority_queue:
#         task = heapq.heappop(priority_queue)  
#         task.execute()
#         for dependency in task.dependencies:
#             dependency.completed_event.wait()
          
#     task1.operation_type = "subtraction"
#     task1.execute()

#     incomplete_task_thread = threading.Thread(target=task_to_handle)
#     incomplete_task_thread.start()
#     # Execute incomplete tasks
#     for task in incomplete_tasks:
#       task.completed_event.wait()

# if __name__ == "__main__":
#     main()
