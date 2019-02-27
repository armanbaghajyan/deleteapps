from okta_app_info import List_Okta_Apps

action = int(input("""
Please choose action.
   1. List duplicatate 
   2. Delete duplicate applications  
   3. Delete application with keyword
   4. Delete single application by name
Your Input: """))

def get_confirmation():
    confirm = input("Do you want to delete this apps?(Yes/No): ").lower()
    if confirm == 'yes' or confirm == 'y':
        confirm = True
    elif confirm == 'no' or confirm == 'n':
        print('Deleteing applications canceled.')
        confirm = False
    else:
        print('Please input Yes or No')
        confirm = False
    return confirm

def list_duplicate():
    duplicate = List_Okta_Apps.apps_to_deactivate()
    for item in duplicate:
        print(item['label'])

def list_by_pattern(pattern):
    applications = List_Okta_Apps.get_app_dict()
    for item in applications:
        if pattern in item['label']:
            print(item['label'])

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
                list_duplicate()
                confirm = get_confirmation()
                if confirm:
                    print("Deleting applications")
                    del_duplicate()
                else:
                    pass
        elif (action == 3):
                pattern = input("Input Delete pattern: ")
                list_by_pattern(pattern)
                confirm = get_confirmation()
                if confirm:
                    print("Deleting applications")
                    del_by_pattern(pattern)
                else:
                    pass
        elif (action == 4):
                label = input("Input application name to delete: ")
                list_by_pattern(label)
                confirm = get_confirmation()
                if confirm:
                    print("Deleting applications")
                    del_single_application(label)
                else:
                    pass
except TypeError:
        print("Nothing to delete")
except Exception as err:
        print(err)