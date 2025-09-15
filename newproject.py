def task():
    tasks=[]
    print("-----welcome to task management app------")
    total_tasks=int(input("how many tasks you want  to enter\n::"))
    for i in range(1,total_tasks+1):
        task_name=input(f"enter task {i}\n:")
        tasks.append(task_name)
    print(f"today's tasks are \n:{tasks}")

    while True:  
        operation=int(input("do you want to \n: 1--add\n 2--update\n 3--delete\n4--view\n5--exit\n enter their no\n:"))
        if operation==1:
            add=input("enter what you want to add\n:")
            tasks.append(add)
            print(f"your {add} task is successfully added\n:")  
        elif operation==2:
            update=input("enter what you want to update\n:")
            if update in tasks:
                up=input("enter new task\n:")
                index=tasks.index(update)
                tasks[index]= up 
                print(f"your {up} task has been updated successfully")  
        elif operation==3:
            delete=input("enter what you want to delete\n:")
            if delete in tasks:
                index=tasks.index(delete)
                tasks.pop(index)
            print(f"your {delete} is successfully deleted")
        elif operation==4:
            print(tasks) 
        elif operation==5:
            print("thankyou for using task management app") 
            break;             
task()            