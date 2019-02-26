from okta_app_info import List_Okta_Apps

action = int(input("""
Please choose action.
   1. List duplicatate 
   2. Delet duplicate applications  
   3. Delete application with keyword
   4. Delete single application by name
Your Input: """))

def list_duplicate():
    duplicate = List_Okta_Apps.apps_to_deactivate()
    print(duplicate)

def del_duplicate():
    duplicate = List_Okta_Apps.apps_to_deactivate()
    for item in duplicate:
        List_Okta_Apps.deactivate(item)
    List_Okta_Apps.delete_inactive()

def del_by_pattern(pattern):
    applications = List_Okta_Apps.get_app_dict()
    for item in applications:
        if pattern in item['label']:
            List_Okta_Apps.deactivate(item)
            List_Okta_Apps.delete(item)

def del_single_application(label):
    List_Okta_Apps.del_by_app_label(label)

try:
        if action not in [1,2,3,4]:
                print("Wrong Choice You need to input 1, 2, 3 or 4")
        elif (action == 1):
                list_duplicate()
        elif (action == 2):
                del_duplicate()
        elif (action == 3):
                pattern = input("Input Delete pattern: ")
                del_by_pattern(pattern)
        elif (action == 4):
                label = input("Input application name to delete: ")
                del_single_application(label)
except TypeError:
        print("Nothing to delete")
except Exception as err:
        print(err)