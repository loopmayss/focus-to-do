import datetime
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Functionalities:
    def __init__(self, accounts, email, account_type):
        self.email = email
        self.accounts = accounts
        self.option = 0
        self.id_task = 0
        self.task_information = {}
        
        self.user_list = {}
        self.id_list = 0
        self.id_list_task = 0
        self.list_task_information = {}
        
        self.account_type = account_type

    def save_data(self, filename, data):
        with open(filename, 'a') as file:
            file.write(data)
    
    def create_task(self):
        task_description, due_date, reminder, repeat, flag =  self.my_day_functionality(1)
        
        if flag:
            self.load_the_last_id(self.accounts[self.email]['id'])
            self.id_task += 1
            
            if self.account_type == 1:
                filename = "user_database/tasks_personal_or_student.txt"
            else:
                filename = "user_database/tasks_professional.txt"
                
            important = 0
            completed = 0
            
            data = f"{self.accounts[self.email]['id']}|{self.id_task}|{task_description}|{due_date}|{reminder}|{repeat}|{important}|{completed}\n"
            self.save_data(filename, data)
            print("\t\tTask created ✅")
            time.sleep(2)
    
    def load_the_last_id(self, user_id):
        if self.account_type == 1:
            filename = "user_database/tasks_personal_or_student.txt"
        else:
            filename = "user_database/tasks_professional.txt"
        
        
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if lines:
                    user_lines = [line for line in lines if line.startswith(f"{user_id}|")]
                    
                    if user_lines:
                        last_line = user_lines[-1].rstrip("\n")
                        self.id_task = int(last_line.split("|")[1])
                    else:
                        self.id_task = 0
                else:
                    self.id_task = 0
                    
        except FileNotFoundError:
            self.id_task = 0
    
    def modify_task(self, id_user, id_task_user, option_selected):
        tasks = []
        
        if self.account_type == 1:
            filename = "user_database/tasks_personal_or_student.txt"
        else:
            filename = "user_database/tasks_professional.txt"
        
        with open(filename, "r") as file:
            for line in file:
                user_id, task_id, description_task, due_date, reminder, repeat, important, completed  = line.rstrip().split("|")
                
                if user_id == str(id_user) and task_id == str(id_task_user):
                    if option_selected == 1:
                        completed = 1
                    elif option_selected == 2:
                        important = 1
                    elif option_selected == 3:
                        self.id_task = id_task_user

                        self.task_information[self.id_task] = {
                            'task_description': description_task,
                            'due_date': due_date,
                            'reminder': reminder,
                            'repeat': repeat
                        }
                        
                        new_description_task, new_due_date, new_reminder, new_repeat, _ = self.my_day_functionality(2)
                        
                        description_task = new_description_task
                        due_date = new_due_date
                        reminder = new_reminder
                        repeat = new_repeat
                        
                    elif option_selected == 4 :
                        completed = 0
                    elif option_selected == 5 :
                        important = 0

                    modified_task = f"{user_id}|{task_id}|{description_task}|{due_date}|{reminder}|{repeat}|{important}|{completed}\n"
                    tasks.append(modified_task)
                    
                else:
                    unmodified_task = f"{user_id}|{task_id}|{description_task}|{due_date}|{reminder}|{repeat}|{important}|{completed}\n"
                    tasks.append(unmodified_task)
            
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task)
    
    def load_data_tasks_personal_or_student(self, id_user):
        continue_view_task = "y"
        flag = False
        try:
            while continue_view_task == "y":
                clear_console()
                self.header()
                print("\n\t\t👀 View Tasks\n\n")
                
                if self.account_type == 1:
                    filename = "user_database/tasks_personal_or_student.txt"
                else:
                    filename = "user_database/tasks_professional.txt"
                
                with open(filename, "r") as file:
                    
                    for line in file:
                        tasks = line.rstrip().split("|")
                        
                        if tasks[0] == id_user:
                            task_id, task_description, due_date, reminder, repeat, important, completed = tasks[1:]
                            current_date = datetime.datetime.now().date()
                            
                            if completed == "0" and due_date == str(current_date):
                                flag = True
                                print(f"\t\t{task_id}|  ☐  {task_description} 👈")
                                
                                if due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "1": 
                                    print("\t\t⭐ Important\n") 
                                elif due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "0": 
                                    print("\t\t☆ not Important\n")   
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "1": 
                                    print(f"\t\t⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "0": 
                                    print(f"\t\t⭕ {repeat} ▪ ☆ not Important\n")
                                elif due_date == "none-none-none" and important == "1":   
                                    print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and important == "0":
                                        print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭐ Important\n")
                                
                                elif important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                    
                    if flag:      
                        answer = input("\t\tSee task options? [Yes: y/ No: n]: ").lower()
                        
                        if answer == "y":
                            id_select_task = int(input("\n\n\t\tTask number: "))
                            
                            completed_task = input(f"\t\tMark task {id_select_task} as completed? [Yes: y/ No: n]: ").lower()
                            if completed_task == "y":
                                self.modify_task(id_user, id_select_task, 1)
                            else:
                                                
                                important_task = input(f"\t\tMark task {id_select_task} as important? [Yes: y/ No: n]: ").lower()
                                if important_task == "y":
                                    self.modify_task(id_user, id_select_task, 2)
                                    
                                
                                modify_task_option = input(f"\t\tModify task {id_select_task}? [Yes: y/ No: n]: ").lower()
                                if modify_task_option == "y":
                                    self.modify_task(id_user, id_select_task, 3)

                            continue_view_task = input("\n\n\t\tKeep seeing the tasks? [Yes: y/ No: n]: ").lower()
                        else:
                            continue_view_task = "n"
                            
                    else:
                        print("\t\tThere are no pending tasks 📖")
                        continue_view_task = input("\n\n\t\tKeep seeing the tasks? [Yes: y/ No: n]: ").lower()
                    
        except FileNotFoundError:
            print("\t\tThere are no pending tasks 📖")     
            
    def view_completed_task(self, id_user, type):
        continue_view_task = "y"
        flag = False
        
        try:
            while continue_view_task == "y":
                clear_console()
                self.header()
                print("\t\t✅ View completed tasks\n\n")
                
                if self.account_type == 1:
                    filename = "user_database/tasks_personal_or_student.txt"
                else:
                    filename = "user_database/tasks_professional.txt"
                
                with open(filename, "r") as file:
                    for line in file:
                        user_id, task_id, description_task, due_date, reminder, repeat, important, completed  = line.rstrip().split("|")  
                        current_date = datetime.datetime.now().date()
                        
                        if  user_id == str(id_user):
                            if completed == "1" and due_date == str(current_date) and type == 1:
                                flag = True
                                print(f"\t\t{task_id}|  ✅  {description_task} 👈")
                                    
                                if due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "1": 
                                    print("\t\t⭐ Important\n") 
                                elif due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "0": 
                                    print("\t\t☆ not Important\n")   
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "1": 
                                    print(f"\t\t⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "0": 
                                    print(f"\t\t⭕ {repeat} ▪ ☆ not Important\n")
                                elif due_date == "none-none-none" and important == "1":   
                                    print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and important == "0":
                                        print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭐ Important\n")
                                
                                elif important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                            
                            elif completed == "1":
                                flag = True
                                print(f"\t\t{task_id}|  ✅  {description_task} 👈")
                                    
                                if due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "1": 
                                    print("\t\t⭐ Important\n") 
                                elif due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "0": 
                                    print("\t\t☆ not Important\n")   
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "1": 
                                    print(f"\t\t⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "0": 
                                    print(f"\t\t⭕ {repeat} ▪ ☆ not Important\n")
                                elif due_date == "none-none-none" and important == "1":   
                                    print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and important == "0":
                                        print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭐ Important\n")
                                
                                elif important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")

                    if flag:            
                        answer = input("\t\tUnmark tasks as completed? [Yes: y/ No: n]: ").lower()  
                            
                        if answer == "y":
                            id_select_task = int(input("\n\n\t\tTask number: "))
                                
                            completed_task = input(f"\t\tMark task {id_select_task} as not completed? [Yes: y/ No: n]: ").lower()
                            if completed_task == "y":
                                self.modify_task(id_user, id_select_task, 4)
                                print("\t\tUnchecked tasks ✔")
                            continue_view_task = input("\n\n\t\tContinue seeing completed tasks? [Yes: y/ No: n]: ").lower()
                            flag = False
                        else:
                            continue_view_task = "n"

                    else:
                        print("\t\tThere are no tasks completed 📖")
                        continue_view_task = input("\n\n\t\tContinue seeing completed tasks? [Yes: y/ No: n]: ").lower()
        
        except   FileNotFoundError:
            print("\t\tThere are no tasks completed 📖")    
        
    def view_important_task(self, id_user):
        continue_view_task = "y"
        flag = False
        try:
            while continue_view_task == "y":
                clear_console()
                self.header()
                print("\t\t⭐️ IMPORTANT")
                
                if self.account_type == 1:
                    filename = "user_database/tasks_personal_or_student.txt"
                else:
                    filename = "user_database/tasks_professional.txt"
                
                with open(filename, "r") as file:
                    for line in file:
                        user_id, task_id, description_task, due_date, reminder, repeat, important, completed  = line.rstrip().split("|")  
                        
                        if  user_id == str(id_user):
                            if important == "1" and completed == "0":
                                flag = True
                                print(f"\t\t{task_id}|  ☐  {description_task} 👈") 
                                # print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                
                                if due_date == "none-none-none" and reminder == "none, none" and repeat == "none": 
                                    print("\t\t⭐ Important\n")  
                                elif due_date == "none-none-none" and reminder == "none, none": 
                                    print(f"\t\t⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none":   
                                    print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and repeat == "none":
                                    print(f"\t\t📆 {due_date} ▪ ⭐ Important\n")
                                elif reminder == "none, none":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif repeat == "none":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭐ Important\n")
                                else:
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")

                    
                    if flag:        
                        answer = input("\t\tRemove importance of  the some task? [Yes: y/ No: n]: ").lower()  
                            
                        if answer == "y":
                            id_select_task = int(input("\n\n\t\tTask number: "))
                                
                            important_task = input("\t\tRemove importance? [Yes: y/ No: n]: ").lower()
                            if important_task == "y":
                                self.modify_task(id_user, id_select_task, 5)
                                print("\t\tImportance removed ✔")
                            continue_view_task = input("\n\n\t\tContinue seeing important tasks? [Yes: y/ No: n]: ").lower()
                            flag = False
                        else:
                            continue_view_task = "n"
                    else:
                        print("\t\tThere are no tasks important 📖")
                        continue_view_task = input("\n\n\t\tContinue seeing important tasks? [Yes: y/ No: n]: ").lower() 
                        
        except   FileNotFoundError:
            print("\t\tThere are no tasks important 📖")   
    
    def view_all_tasks(self, id_user):
        continue_view_task = "y"
        flag = False
        try:
            while continue_view_task == "y":
                clear_console()
                self.header()
                print("\t\t📑 TASKS")
                
                if self.account_type == 1:
                    filename = "user_database/tasks_personal_or_student.txt"
                else:
                    filename = "user_database/tasks_professional.txt"
                
                with open(filename, "r") as file:
                    
                    for line in file:
                        tasks = line.rstrip().split("|")
                        
                        if tasks[0] == id_user:
                            task_id, task_description, due_date, reminder, repeat, important, completed = tasks[1:]
                            
                            if completed == "0" :
                                flag = True
                                print(f"\t\t{task_id}|  ☐  {task_description} 👈")
                                
                                if due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "1": 
                                    print("\t\t⭐ Important\n") 
                                elif due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "0": 
                                    print("\t\t☆ not Important\n")   
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "1": 
                                    print(f"\t\t⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "0": 
                                    print(f"\t\t⭕ {repeat} ▪ ☆ not Important\n")
                                elif due_date == "none-none-none" and important == "1":   
                                    print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and important == "0":
                                        print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭐ Important\n")
                                
                                elif important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                    
                    if flag:      
                        answer = input("\t\tSee task options? [Yes: y/ No: n]: ").lower()
                        
                        if answer == "y":
                            id_select_task = int(input("\n\n\t\tTask number: "))
                            
                            completed_task = input(f"\t\tMark task {id_select_task} as completed? [Yes: y/ No: n]: ").lower()
                            if completed_task == "y":
                                self.modify_task(id_user, id_select_task, 1)
                            else:
                                                
                                important_task = input(f"\t\tMark task {id_select_task} as important? [Yes: y/ No: n]: ").lower()
                                if important_task == "y":
                                    self.modify_task(id_user, id_select_task, 2)
                                    
                                
                                modify_task_option = input(f"\t\tModify task {id_select_task}? [Yes: y/ No: n]: ").lower()
                                if modify_task_option == "y":
                                    self.modify_task(id_user, id_select_task, 3)

                            continue_view_task = input("\n\n\t\tKeep seeing the tasks? [Yes: y/ No: n]: ").lower()
                        else:
                            continue_view_task = "n"
                            
                    else:
                        print("\t\tThere are no pending tasks 📖")
                        continue_view_task = input("\n\n\t\tKeep seeing the tasks? [Yes: y/ No: n]: ").lower()


        except   FileNotFoundError:
            print("\t\tThere are no pending tasks 📖")   
    
    
    
    def load_the_last_id_list(self, user_id):
        
        if self.account_type == 1:
            filename = "user_database/lists_personal_or_student.txt"
        else: 
            filename = "user_database/lists_professional.txt"
        
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if lines:
                    user_lines = [line for line in lines if line.startswith(f"{user_id}|")]
                    
                    if user_lines:
                        last_line = user_lines[-1].rstrip("\n")
                        self.id_list = int(last_line.split("|")[1])
                    else:
                        self.id_list = 0
                else:
                    self.id_list = 0
                    
        except FileNotFoundError:
            self.id_list = 0
    
    def load_the_last_id_list_task(self, user_id, id_list_selected):
        
        if self.account_type == 1:
            filename = "user_database/task_list_personal_or_student.txt"
        else: 
            filename = "user_database/task_list_professional.txt"
        
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if lines:
                    user_lines = [line for line in lines if line.startswith(f"{user_id}|{id_list_selected}|")]
                    
                    if user_lines:
                        last_line = user_lines[-1].rstrip("\n")
                        self.id_list_task = int(last_line.split("|")[2])
                    else:
                        self.id_list_task = 0
                else:
                    self.id_list_task = 0
                    
        except FileNotFoundError:
            self.id_list_task = 0
    
    def modify_list_task(self, id_user, id_list_selected, id_task_list, option_selected):
        tasks = []
        
        if self.account_type == 1:
            filename = "user_database/task_list_personal_or_student.txt"
        else: 
            filename = "user_database/task_list_professional.txt"
        
        with open(filename, "r") as file:
            for line in file:
                user_id, list_id_selected, task_id, description_task, due_date, reminder, repeat, important, completed  = line.rstrip().split("|")
                
                if user_id == str(id_user) and list_id_selected == str(id_list_selected) and  task_id == str(id_task_list):
                    if option_selected == 1:
                        completed = 1
                    elif option_selected == 2:
                        important = 1
                    elif option_selected == 3:
                        self.id_list_task = id_task_list

                        self.list_task_information[self.id_list_task] = {
                            'task_description': description_task,
                            'due_date': due_date,
                            'reminder': reminder,
                            'repeat': repeat
                        }
                        
                        new_description_task, new_due_date, new_reminder, new_repeat, _ = self.my_day_functionality(3)
                        
                        description_task = new_description_task
                        due_date = new_due_date
                        reminder = new_reminder
                        repeat = new_repeat
                        
                    elif option_selected == 4 :
                        completed = 0
                    elif option_selected == 5 :
                        important = 0
                    
                    modified_task = f"{user_id}|{list_id_selected}|{task_id}|{description_task}|{due_date}|{reminder}|{repeat}|{important}|{completed}\n"
                    tasks.append(modified_task)
                    
                else:
                    unmodified_task = f"{user_id}|{list_id_selected}|{task_id}|{description_task}|{due_date}|{reminder}|{repeat}|{important}|{completed}\n"
                    tasks.append(unmodified_task)
            
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task)
    
    def load_the_list_task(self, id_user, list_id):
        continue_view_task = "y"
        flag = False
        count = 0
        
        selected_list = self.user_list[str(list_id)]
        title_list = selected_list["title_list"]
        category = selected_list["category"]
        file_path = selected_list["file_path"]
        note = selected_list["note"]
        
        
        try:
            while continue_view_task == "y":
                clear_console()
                self.header()
                print("\n\t\t👀 VIEW TASKS LISTS\n\n")
                
                if self.account_type == 1:
                    filename = "user_database/task_list_personal_or_student.txt"
                else: 
                    filename = "user_database/task_list_professional.txt"
                
                with open(filename, "r") as file:
                    
                    for line in file:
                        lists = line.rstrip().split("|")
                        
                        if lists[0] == str(id_user) and lists[1] == str(list_id):
                            list_id_selected, task_id, task_description, due_date, reminder, repeat, important, completed = lists[1:]
                            
                            if count == 0:
                                print(f"\t\t🔎 List {list_id_selected}: 📂 {title_list}\n")
                                
                                if  category == "none" and file_path == "none" and note == "none":
                                    print("")
                                elif category == "none" and note == "none":
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "none" and file_path == "none":
                                    print(f"\t\tNote: {note}")
                                elif category == "none":
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                elif category == "Blue Category" and file_path == "none" and note == "none":
                                    print("\t\t🔵 Blue Category")
                                elif category == "Blue Category" and file_path == "none":
                                    print("\t\t🔵 Blue Category")
                                    print(f"\t\tNote: {note}")
                                elif category == "Blue Category" and note == "none":
                                    print("\t\t🔵 Blue Category")
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "Blue Category":
                                    print("\t\t🔵 Blue Category")
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                elif category == "Green Category" and file_path == "none" and note == "none":
                                    print("\t\t🍏 Green Category")
                                elif category == "Green Category" and file_path == "none":
                                    print("\t\t🍏 Green Category")
                                    print(f"\t\tNote: {note}")
                                elif category == "Green Category" and note == "none":
                                    print("\t\t🍏 Green Category")
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "Green Category":
                                    print("\t\t🍏 Green Category")
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                elif category == "Orange Category" and file_path == "none" and note == "none":
                                    print("\t\t🔶 Orange Category")
                                elif category == "Orange Category" and file_path == "none":
                                    print("\t\t🔶 Orange Category")
                                    print(f"\t\tNote: {note}")
                                elif category == "Orange Category" and note == "none":
                                    print("\t\t🔶 Orange Category")
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "Orange Category":
                                    print("\t\t🔶 Orange Category")
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                elif category == "Purple Category" and file_path == "none" and note == "none":
                                    print("\t\t💜 Purple Category")
                                elif category == "Purple Category" and file_path == "none":
                                    print("\t\t💜 Purple Category")
                                    print(f"\t\tNote: {note}")
                                elif category == "Purple Category" and note == "none":
                                    print("\t\t💜 Purple Category")
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "Purple Category":
                                    print("\t\t💜 Purple Category")
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                elif category == "Red Category" and file_path == "none" and note == "none":
                                    print("\t\t🔴 Red Category")
                                elif category == "Red Category" and file_path == "none":
                                    print("\t\t🔴 Red Category")
                                    print(f"\t\tNote: {note}")
                                elif category == "Red Category" and note == "none":
                                    print("\t\t🔴 Red Category")
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "Red Category":
                                    print("\t\t🔴 Red Category")
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                
                                count += 1
                                print("\n\n")
                            
                            if completed == "0":
                                flag = True
                                print(f"\t\t{task_id}|  ☐  {task_description} 👈")
                                
                                if due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "1": 
                                    print("\t\t⭐ Important\n") 
                                elif due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "0": 
                                    print("\t\t☆ not Important\n")   
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "1": 
                                    print(f"\t\t⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "0": 
                                    print(f"\t\t⭕ {repeat} ▪ ☆ not Important\n")
                                elif due_date == "none-none-none" and important == "1":   
                                    print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and important == "0":
                                        print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭐ Important\n")
                                
                                elif important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                    
                    if flag:      
                        answer = input("\t\tSee task options? [Yes: y/ No: n]: ").lower()
                        
                        if answer == "y":
                            id_select_task = int(input("\n\n\t\tTask number: "))
                            
                            completed_task = input(f"\t\tMark task {id_select_task} as completed? [Yes: y/ No: n]: ").lower()
                            if completed_task == "y":
                                self.modify_list_task(id_user, list_id,  id_select_task, 1)
                            else:
                                                
                                important_task = input(f"\t\tMark task {id_select_task} as important? [Yes: y/ No: n]: ").lower()
                                if important_task == "y":
                                    self.modify_list_task(id_user, list_id, id_select_task, 2)
                                    
                                
                                modify_task_option = input(f"\t\tModify task {id_select_task}? [Yes: y/ No: n]: ").lower()
                                if modify_task_option == "y":
                                    self.modify_list_task(id_user, list_id, id_select_task, 3)

                            continue_view_task = input("\n\n\t\tKeep seeing the tasks? [Yes: y/ No: n]: ").lower()
                        else:
                            continue_view_task = "n"
                            
                    else:
                        print("\t\tThere are no pending tasks 📖")
                        continue_view_task = input("\n\n\t\tKeep seeing the tasks? [Yes: y/ No: n]: ").lower()
                    
        except FileNotFoundError:
            print("\t\tThere are no pending tasks 📖")     
    
    def view_completed_task_list(self, id_user, list_id):
        continue_view_task = "y"
        flag = False
        count = 0
        
        selected_list = self.user_list[str(list_id)]
        title_list = selected_list["title_list"]
        category = selected_list["category"]
        file_path = selected_list["file_path"]
        note = selected_list["note"]
        
        try:
            while continue_view_task == "y":
                clear_console()
                self.header()
                print("\t\t✅ View completed tasks\n\n")
                
                if self.account_type == 1:
                    filename = "user_database/task_list_personal_or_student.txt"
                else: 
                    filename = "user_database/task_list_professional.txt"
                
                with open(filename, "r") as file:
                    for line in file:
                        user_id, list_id_selected, task_id, description_task, due_date, reminder, repeat, important, completed  = line.rstrip().split("|")                          
                        
                        if  user_id == str(id_user) and list_id_selected == str(list_id):
                            
                            if count == 0:
                                print(f"\t\t🔎 List {list_id_selected}: 📂 {title_list}\n")
                                
                                if  category == "none" and file_path == "none" and note == "none":
                                    print("")
                                elif category == "none" and note == "none":
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "none" and file_path == "none":
                                    print(f"\t\tNote: {note}")
                                elif category == "none":
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                elif category == "Blue Category" and file_path == "none" and note == "none":
                                    print("\t\t🔵 Blue Category")
                                elif category == "Blue Category" and file_path == "none":
                                    print("\t\t🔵 Blue Category")
                                    print(f"\t\tNote: {note}")
                                elif category == "Blue Category" and note == "none":
                                    print("\t\t🔵 Blue Category")
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "Blue Category":
                                    print("\t\t🔵 Blue Category")
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                elif category == "Green Category" and file_path == "none" and note == "none":
                                    print("\t\t🍏 Green Category")
                                elif category == "Green Category" and file_path == "none":
                                    print("\t\t🍏 Green Category")
                                    print(f"\t\tNote: {note}")
                                elif category == "Green Category" and note == "none":
                                    print("\t\t🍏 Green Category")
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "Green Category":
                                    print("\t\t🍏 Green Category")
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                elif category == "Orange Category" and file_path == "none" and note == "none":
                                    print("\t\t🔶 Orange Category")
                                elif category == "Orange Category" and file_path == "none":
                                    print("\t\t🔶 Orange Category")
                                    print(f"\t\tNote: {note}")
                                elif category == "Orange Category" and note == "none":
                                    print("\t\t🔶 Orange Category")
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "Orange Category":
                                    print("\t\t🔶 Orange Category")
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                elif category == "Purple Category" and file_path == "none" and note == "none":
                                    print("\t\t💜 Purple Category")
                                elif category == "Purple Category" and file_path == "none":
                                    print("\t\t💜 Purple Category")
                                    print(f"\t\tNote: {note}")
                                elif category == "Purple Category" and note == "none":
                                    print("\t\t💜 Purple Category")
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "Purple Category":
                                    print("\t\t💜 Purple Category")
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                elif category == "Red Category" and file_path == "none" and note == "none":
                                    print("\t\t🔴 Red Category")
                                elif category == "Red Category" and file_path == "none":
                                    print("\t\t🔴 Red Category")
                                    print(f"\t\tNote: {note}")
                                elif category == "Red Category" and note == "none":
                                    print("\t\t🔴 Red Category")
                                    print(f'\t\tFile: "{file_path}"')
                                elif category == "Red Category":
                                    print("\t\t🔴 Red Category")
                                    print(f'\t\tFile: "{file_path}"')
                                    print(f"\t\tNote: {note}")
                                
                                count += 1
                                print("\n\n")
                            
                            if completed == "1":
                                flag = True
                                print(f"\t\t{task_id}|  ✅  {description_task} 👈")
                                    
                                if due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "1": 
                                    print("\t\t⭐ Important\n") 
                                elif due_date == "none-none-none" and reminder == "none, none" and repeat == "none" and important == "0": 
                                    print("\t\t☆ not Important\n")   
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "1": 
                                    print(f"\t\t⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and reminder == "none, none" and important == "0": 
                                    print(f"\t\t⭕ {repeat} ▪ ☆ not Important\n")
                                elif due_date == "none-none-none" and important == "1":   
                                    print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif due_date == "none-none-none" and important == "0":
                                        print(f"\t\t⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ☆ not Important\n")
                                elif reminder == "none, none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ⭐ Important\n")
                                elif reminder == "none, none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ☆ not Important\n")
                                elif repeat == "none" and important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭐ Important\n")
                                
                                elif important == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important\n")
                                elif important == "1":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important\n")

                    if flag:            
                        answer = input("\t\tUnmark tasks as completed? [Yes: y/ No: n]: ").lower()  
                            
                        if answer == "y":
                            id_select_task = int(input("\n\n\t\tTask number: "))
                                
                            completed_task = input(f"\t\tMark task {id_select_task} as not completed? [Yes: y/ No: n]: ").lower()
                            if completed_task == "y":
                                self.modify_list_task(id_user, list_id, id_select_task, 4)
                                print("\t\tUnchecked tasks ✔")
                            continue_view_task = input("\n\n\t\tContinue seeing completed tasks? [Yes: y/ No: n]: ").lower()
                            flag = False
                        else:
                            continue_view_task = "n"

                    else:
                        print("\t\tThere are no tasks completed 📖")
                        continue_view_task = input("\n\n\t\tContinue seeing completed tasks? [Yes: y/ No: n]: ").lower()
        
        except   FileNotFoundError:
            print("\t\tThere are no tasks completed 📖")   
    
    def create_task_an_exist_list(self, id_user, id_select_list):
        if self.account_type == 1:
            filename = "user_database/task_list_personal_or_student.txt"
        else: 
            filename = "user_database/task_list_professional.txt"
        
        completed = 0
        important = 0
        
        selected_list = self.user_list[str(id_select_list)]
        title_list = selected_list["title_list"]
        
        clear_console()
        self.header()
        print("\n\t\t📘 CREATE TASKS\n\n")
        print(f"\t\t🔎 List {id_select_list}: 📂 {title_list}\n")
        time.sleep(3)
        
        while True:
            task_description, due_date, reminder, repeat, flag =  self.my_day_functionality(1)
            
            if flag: 
                self.load_the_last_id_list_task(id_user, id_select_list)
                self.id_list_task += 1

                data = f"{self.accounts[self.email]['id']}|{id_select_list}|{self.id_list_task}|{task_description}|{due_date}|{reminder}|{repeat}|{important}|{completed}\n"
                self.save_data(filename, data)
                print("\t\tTask created ✅")
                time.sleep(1)
                
                answer = input("\n\t\tAdd more tasks? [Yes: y/ No: n]: ").lower()
                
                if answer != "y":
                    break
                
            else:
                break     
    
    def create_list(self):
        completed = 0
        important = 0
        id_list_task_temporal = 0
        count = 0
        
        clear_console()
        self.header()
        print("\n\t\t📜 CREATE NEW LIST\n\n")
        
        while True:
            title_list = input("\t\tList Title: ")
            
            if not title_list:
                print("\t\tPlease enter a list title.")
            else:
                self.load_the_last_id_list(self.accounts[self.email]['id'])
                self.id_list += 1
                break
        
        question = input("\n\t\tPick a category? [Yes: y/ No: n]: ").lower()
                
        if question == "y":
            print("\t\t1: 🔵 Blue Category")
            print("\t\t2: 🍏 Green Category")
            print("\t\t3: 🔶 Orange Category")
            print("\t\t4: 💜 Purple Category")
            print("\t\t5: 🔴 Red Category")
            
            while True:
                option_category = int(input("\t\tCategory: "))
                
                if option_category == 1:
                    category = "Blue Category"
                    break
                elif option_category == 2:
                    category = "Green Category"
                    break
                elif option_category == 3:
                    category = "Orange Category"
                    break
                elif option_category == 4:
                    category = "Purple Category"
                    break
                elif option_category == 5:
                    category = "Red Category"
                    break
                else: 
                    print("\t\tOption Invalid :(")
        else:
            category = "none"
                            
        question = input("\n\t\t\Add a file? [Yes: y/ No: n]: ").lower()
        
        if  question == "y":
            file_path = input("\t\tFile Path: ")
        else:
            file_path = "none"
                         
        question = input("\n\t\tAdd a note? [Yes: y/ No: n]: ").lower()
        
        if question == "y":
            note = input("\t\tNote: ")        
        else:
            note = "none"
       
       
        print(f"\n\n\t\t😁 Add at least one task to the {title_list} list ✋")
        time.sleep(2)
        
        while True:
            task_description, due_date, reminder, repeat, flag =  self.my_day_functionality(1)
            
            if flag: 
                
                if count == 0:
                    if self.account_type == 1:
                        filename = "user_database/lists_personal_or_student.txt"
                    else: 
                        filename = "user_database/lists_professional.txt"
                        
                    data = f"{self.accounts[self.email]['id']}|{self.id_list}|{title_list}|{category}|{file_path}|{note}\n"
                    self.save_data(filename, data)
                    count += 1
                
                id_list_task_temporal += 1
                
                if self.account_type == 1:
                    filename = "user_database/task_list_personal_or_student.txt"
                else: 
                    filename = "user_database/task_list_professional.txt"
                
                data = f"{self.accounts[self.email]['id']}|{self.id_list}|{id_list_task_temporal}|{task_description}|{due_date}|{reminder}|{repeat}|{important}|{completed}\n"
                self.save_data(filename, data)
                
                print("\t\tTask created ✅")
                time.sleep(1)
                
                answer = input("\n\t\tAdd more tasks? [Yes: y/ No: n]: ").lower()
                
                if answer != "y":
                    break
                
            else:
                print(f"\t\t😁 Add at least one task to the {title_list} list ✋")
                time.sleep(2)      
    
    def view_lists(self, id_user):
        try:
            while True:
                clear_console()
                self.header()
                print("\n\t\t👀 VIEW LISTS\n\n")
                
                if self.account_type == 1:
                    filename = "user_database/lists_personal_or_student.txt"
                else: 
                    filename = "user_database/lists_professional.txt"
                
                with open(filename, "r") as file:
                    
                    for line in file:
                        user_id, list_id, title_list, category, file_path, note = line.rstrip().split("|")
                        
                        if int(user_id) == int(id_user):
                            self.user_list[list_id] = {
                                "title_list": title_list,
                                "category": category,
                                "file_path": file_path,
                                "note": note
                            }
                            
                            print(f"\t\t{list_id}| 💡 {title_list}\n")
                            
                        
                    
                    print("\n\n\t\tOPTIONS\n")
                    print("\t\t1. 👀 See tasks lists")
                    print("\t\t2. ✅ Show completed tasks from lists")
                    print("\t\t3. 📘 Create tasks to an existing list")
                    print("\t\t4. 🚶 Back")
                    
                    while True:
                        answer = int(input("\n\t\tOPTION: "))

                        if answer >= 1 and answer <= 4:
                            break
                        else:
                            print("\t\tInvalid option :(")

                    if answer == 1:
                        id_select_list = int(input("\n\t\tList number: "))
                        self.load_the_list_task(self.accounts[self.email]['id'], id_select_list)
                        
                    elif  answer == 2:
                        id_select_list = int(input("\n\t\tList number: "))
                        self.view_completed_task_list(self.accounts[self.email]['id'], id_select_list)
                    elif answer == 3:
                        id_select_list = int(input("\n\t\tList number: "))
                        self.create_task_an_exist_list(self.accounts[self.email]['id'], id_select_list)
                    else:
                        break
                        
        except   FileNotFoundError:
            print("\t\tERROR! 📖")  
        
               
    def header(self):
        print("\n\t\t📒 Focus TO-DO 📒\n")
        print(f"\t\t👦 {self.accounts[self.email]['name']} {self.accounts[self.email]['lastname']}\n\n")
    
    def get_option(self):
        return self.option

    def features_menu(self):
        while self.option != 6:
            clear_console()
            self.header()
            print("\t\t1. 🚀 MY DAY")
            print("\t\t2. ⭐️ IMPORTANT")
            print("\t\t3. 📑 TASKS")
            print("\t\t4. ✅ View all completed tasks")
            print("\t\t5. 📚 NEW LIST")
            print("\t\t6. 🚶 EXIT")
            
            while(True):
                self.option = int(input("\t\t⏩ OPTION: "))
                
                if self.option >= 1 and self.option <= 6:
                    break
                else :
                    print("\t\tInvalid Option :(\n")
            
            if self.option == 1:
                self.option = 0
                self.my_day_menu()
            elif self.option == 2:
                self.view_important_task(self.accounts[self.email]['id'])
            elif self.option == 3:
                self.view_all_tasks(self.accounts[self.email]['id'])
            elif self.option == 4:
                self.view_completed_task(self.accounts[self.email]['id'], 2)
            elif self.option == 5:
                self.option = 0
                self.new_list_menu()
            else:
                break
   
    def my_day_menu(self):
        while self.option != 4:
            clear_console()
            self.header()
            print("\t\t🚀 MY DAY\n\n")
            print("\t\t1. ➕ Add Task")
            print("\t\t2. 👀 View Tasks")
            print("\t\t3. ✅ View completed tasks")
            print("\t\t4. 🚶 Back")
            print("\t\t-----------------------\n\n")
            
            while True:
                self.option = int(input("\t\t⏩ OPTION: "))
                
                if self.option >= 1 and self.option <= 4:
                    break
                else:
                    print("Option invalid :(")
            
            if self.option == 1:
                self.create_task()
            elif self.option == 2:
                self.load_data_tasks_personal_or_student(self.accounts[self.email]['id'])
            elif self.option == 3:
                self.view_completed_task(self.accounts[self.email]['id'], 1)
            else:
                break
   
    def new_list_menu(self):
        while self.option != 3:
            clear_console()
            self.header()
            print("\n\t\t📚 NEW LIST\n\n")
            print("\t\t1. 📜 CREATE NEW LIST")
            print("\t\t2. 👀 VIEW LISTS")
            print("\t\t3. 🚶 BACK")
            
            while(True):
                    self.option = int(input("\t\t⏩ OPTION: "))
                    
                    if self.option >= 1 and self.option <= 3:
                        break
                    else :
                        print("\t\tInvalid Option :(\n")
            
            if self.option == 1:
                self.create_list()
            elif self.option == 2:
                self.view_lists(self.accounts[self.email]['id'])
            else:
                break 
   
   
   
    def validate_date(self):
        
        def validate_year(year):
            if year < 2023 :
                return False
            else:
                return True
        
        def validate_month(month):
            if month >= 1 and month <= 12:
                return True
            else:
                return False
        
        def validate_day(day, month):
            if  month % 2 == 0:
                if day >= 1 and day <= 30:
                    return True
                else:
                    return False
            else:
                if day >= 1 and day <= 31:
                    return True
                else:
                    return False

        while(True):
            year = int(input("\t\tYear: "))
            if validate_year(year):
                break
        
        while(True):
            month = int(input("\t\tMonth: "))
            if validate_month(month):
                break
        
        while(True): 
            day = int(input("\t\tDay: "))
            if validate_day(day, month):
                break
        
        due_date = datetime.date(year, month, day)  
        
        return due_date
   
    def validate_hour_and_minute(self):
        
        def validate_hour(hour):
            if hour >= 0 and hour <= 23:
                return True
            else:
                return False
        
        def validate_minute(minute):
            if minute >= 0 and minute <= 59:
                return True
            else:
                return False
        
        time = ""
        while(True):
            hour = int(input("\t\tHour: "))
            if validate_hour(hour):
                break
            
        while(True):
            minute = int(input("\t\tMinute: "))
            if validate_minute(minute):
                break
        
        
        if minute >= 0 and minute <= 9 and hour >= 0 and hour <= 9:
            time = f"0{hour}:0{minute}"
        else:
            time = f"{hour}:{minute}"
            
        return time
   
    def due_date_task(self):
        due_date = "none-none-none"
        print("\n\n")
        print("\t\t📆 Due \n")
        print("\t\t1. TODAY")
        print("\t\t2. TOMORROW")
        print("\t\t3. NEXT WEEK")
        print("\t\t4. PICK a DATE")
        self.option = int(input("\t\t⏩ OPTION: "))
        
        current_date = datetime.datetime.now().date()
        
        if self.option == 1:
            due_date = current_date
        elif self.option == 2:
            due_date = current_date + datetime.timedelta(days=1)    
        elif self.option == 3:
            due_date = current_date + datetime.timedelta(weeks=1)
        else:
            due_date = self.validate_date()
        
        return due_date
    
    def reminder_task(self):
        reminder = "none, none"
        print("\n\n")
        print("\t\t⏰ Reminder \n")
        print("\t\t1. LATER TODAY")
        print("\t\t2. TOMORROW")
        print("\t\t3. NEXT WEEK")
        print("\t\t4. PICK a DATE & TIME")
        self.option = int(input("\t\t⏩ OPTION: "))
        
        current_time = datetime.datetime.now().time()
        new_time = datetime.datetime.combine(datetime.date.today(), current_time) + datetime.timedelta(hours=3)
        date = datetime.date.today()
        if self.option == 1:
            reminder = f"{new_time.hour:02d}:{new_time.minute:02d}"
        elif self.option == 2:
            new_day = date + datetime.timedelta(days=1)
            reminder = f"{new_day.strftime('%A')}, 9:00"
        elif self.option == 3:
            new_day = date + datetime.timedelta(weeks=1)
            reminder = f"{new_day.strftime('%A')}, 9:00"
        else:
            custom_date = self.validate_date()
            print("\n\n")
            custom_time = self.validate_hour_and_minute()
            
            reminder = f"{custom_date}, {custom_time}"
        
        return reminder
   
    def repeat_task(self):
        repeat = "none"
        print("\n\n")
        print("\t\t⭕ Repeat \n")
        print("\t\t1. DAILY")
        print("\t\t2. WEEKDAYS")
        print("\t\t3. WEEKLY")
        print("\t\t4. MONTHLY")
        print("\t\t5. YEARLY")
        self.option = int(input("\t\t⏩ OPTION: "))
        
        if self.option == 1:
            repeat = "Daily"
        elif self.option == 2:
            repeat = "Weekdays"
        elif self.option == 3:
            repeat = "Weekly"
        elif self.option == 4:
            repeat = "Monthly"
        elif self.option == 5:
            repeat = "Yearly"
        
        return repeat
   
    def my_day_functionality(self, value):   
        clear_console()    
        self.header() 
        answer = ""
        
        if value == 1:
            print("\n\n\t\t➕ Add Task\n\n")
        elif value == 2:
            unmodified_task_description = self.task_information[self.id_task]['task_description']
            unmodified_due_date = self.task_information[self.id_task]['due_date']
            unmodified_reminder = self.task_information[self.id_task]['reminder']
            unmodified_repeat = self.task_information[self.id_task]['repeat']
            
            print("\n\n\t\t☝ Modify Task\n\n")
        elif value == 3:
            unmodified_task_description = self.list_task_information[self.id_list_task]['task_description']
            unmodified_due_date = self.list_task_information[self.id_list_task]['due_date']
            unmodified_reminder = self.list_task_information[self.id_list_task]['reminder']
            unmodified_repeat = self.list_task_information[self.id_list_task]['repeat']
            
            print("\n\n\t\t☝ Modify Task\n\n")
            
        while True:
            if value == 1:
                task_description = input("\t\tAdd a task: ")
                
                if not task_description:
                    print("\t\tPlease enter a task description.")
                else:
                    break
                
            else: 
                task_description = input("\t\tTask [Enter: default value]: ")
                
                if not task_description:
                    task_description = unmodified_task_description
                    break
                else:
                    break
       
        if value == 1:
            answer = input("\t\tAdd due date? [Yes:y / No:n]: ").lower()
            
            if answer != "y":
                due_date = "none-none-none"
            
        else:
            answer = input("\t\tModify due date? [Yes:y / No:n]: ").lower()
            
            if answer != "y":
                due_date = unmodified_due_date

        if answer == "y":
            due_date = self.due_date_task()
            
            
            
        if value == 1:
            answer = input("\n\n\t\tDo you want a reminder? [Yes:y / No:n]: ").lower()
            
            if answer != "y":
                reminder = "none, none"
                
        else: 
            answer = input("\n\n\t\tModify reminder? [Yes:y / No:n]: ").lower()
            
            if answer != "y":
                reminder = unmodified_reminder
        
        if answer == "y":
            reminder = self.reminder_task()


         
        if value == 1:   
            answer = input("\n\n\t\tDo you want the task to be repeated? [Yes:y / No:n]: ").lower()
            
            if answer != "y":
                repeat = "none"
        else:
            answer = input("\n\n\t\tModify repeated? [Yes:y / No:n]: ").lower()
            
            if answer != "y":
                repeat = unmodified_repeat
        
        if answer == "y":
            repeat = self.repeat_task()
        
        
        
        if value == 1:
            answer = input("\n\n\t\tCreate task? [Yes:y / No:n]: ").lower()
        else :
            answer = input("\n\n\t\tModify task? [Yes:y / No:n]: ").lower()
            
        if answer == "y":
            return task_description, due_date, reminder, repeat, True
        else:
            return task_description, due_date, reminder, repeat, False
