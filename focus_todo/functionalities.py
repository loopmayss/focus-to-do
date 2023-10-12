import datetime
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Functionalities:
    def __init__(self, accounts, email):
        self.email = email
        self.accounts = accounts
        self.option = 0
        self.id_task = 0
        self.task_information = {}

    def save_data(self, filename, data):
        with open(filename, 'a') as file:
            file.write(data)
    
    def create_task(self, value):
        task_description, due_date, reminder, repeat =  self.my_day_functionality(value)
        
        self.id_task += 1
        filename = "user_database/tasks_personal_or_student.txt"
        important = 0
        completed = 0
        
        data = f"{self.accounts[self.email]['id']}|{self.id_task}|{task_description}|{due_date}|{reminder}|{repeat}|{important}|{completed}\n"
        self.save_data(filename, data)
        print("\t\tTask created ✅")
        time.sleep(2)
    
    def load_the_last_id(self, user_id):
        try:
            with open("user_database/tasks_personal_or_student.txt", 'r') as file:
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
        
        with open("user_database/tasks_personal_or_student.txt", "r") as file:
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
                        
                        new_description_task, new_due_date, new_reminder, new_repeat = self.my_day_functionality(2)
                        
                        description_task = new_description_task
                        due_date = new_due_date
                        reminder = new_reminder
                        repeat = new_repeat
                        

                    modified_task = f"{user_id}|{task_id}|{description_task}|{due_date}|{reminder}|{repeat}|{important}|{completed}\n"
                    tasks.append(modified_task)
                else:
                    unmodified_task = f"{user_id}|{task_id}|{description_task}|{due_date}|{reminder}|{repeat}|{important}|{completed}\n"
                    tasks.append(unmodified_task)
            
        with open("user_database/tasks_personal_or_student.txt", "w") as file:
            for task in tasks:
                file.write(task)
    
    def load_data_tasks_personal_or_student(self, id_user):
        continue_view_task = "y"
        try:
            while continue_view_task == "y":
                clear_console()
                print("\n\t\t👀 View Tasks\n\n")
                with open("user_database/tasks_personal_or_student.txt", "r") as file:
                    
                    for line in file:
                        tasks = line.rstrip().split("|")
                        
                        if tasks[0] == id_user:
                            task_id, task_description, due_date, reminder, repeat, important, completed = tasks[1:]
                            
                            if completed == "0" :
                                print(f"\t\t{task_id}|  ☐  {task_description} 👈")
                                
                                if important == "0" and completed == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ☆ not Important ")
                                elif important == "1" and completed == "0":
                                    print(f"\t\t📆 {due_date} ▪ ⏰ {reminder} ▪ ⭕ {repeat} ▪ ⭐ Important ")
                            
                            print("\n")   
                    
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
                        
        except   FileNotFoundError:
            print("\t\tThere are no pending tasks 📖")     
               
    def header(self):
        print("\n\t\t📒 Focus TO-DO 📒\n")
        print(f"\t\t👦 {self.accounts[self.email]['name']} {self.accounts[self.email]['lastname']}\n\n")
    
    def get_option(self):
        return self.option

    def features_menu(self):
        while self.option != 5:
            clear_console()
            self.header()
            print("\t\t1. 🚀 MY DAY")
            print("\t\t2. ⭐️ IMPORTANT")
            print("\t\t3. 📑 TASKS")
            print("\t\t4. 📚 NEW LIST")
            print("\t\t5. 🚶 EXIT")
            
            while(True):
                self.option = int(input("\t\t⏩ OPTION: "))
                
                if self.option >= 1 and self.option <= 5:
                    break
                else :
                    print("\t\tInvalid Option :(\n")
            
            if self.option == 1:
                self.option = 0
                self.my_day_menu()
            elif self.option == 5:
                break
   
    def my_day_menu(self):
        while self.option != 3:
            clear_console()
            self.header()
            print("\t\t🚀 MY DAY\n\n")
            print("\t\t1. ➕ Add Task")
            print("\t\t2. 👀 View Tasks")
            print("\t\t3. 🚶 Exit")
            print("\t\t-----------------------\n\n")
            self.option = int(input("\t\t⏩ OPTION: "))
            
            if self.option == 1:
                self.create_task(1)
            elif self.option == 2:
                self.load_data_tasks_personal_or_student(self.accounts[self.email]['id'])
            elif self.option == 3:
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
        else:
            unmodified_task_description = self.task_information[self.id_task]['task_description']
            unmodified_due_date = self.task_information[self.id_task]['due_date']
            unmodified_reminder = self.task_information[self.id_task]['reminder']
            unmodified_repeat = self.task_information[self.id_task]['repeat']
            
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
            answer2 = input("\n\n\t\tModify task? [Yes:y / No:n]: ").lower()
            
        if answer == "y":
            self.load_the_last_id(self.accounts[self.email]['id'])
            return task_description, due_date, reminder, repeat
        
        if answer2 == "y":
            return task_description, due_date, reminder, repeat