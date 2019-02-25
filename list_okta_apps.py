import requests
import json

okta_domain = "https://vinetidev.okta.com"
okta_token = "007ImE9lyiIlUNnoz3DLG6GUy6WSL3tywbCkO7nDEB"
headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "SSWS {0}".format(okta_token)
        }  


class List_Okta_Apps:
    def __init__(self, okta_domain, token, headers):
        self.okta_domain = okta_domain
        self.okta_token = okta_token
        self.headers = headers 
 
    @classmethod
    def list(cls):
        domain = okta_domain+"/api/v1/apps?limit=9999"
        okta_req = requests.get(domain, headers=headers)
        return okta_req.json()

    def get_app_list():
        okta_app_json = List_Okta_Apps.List()
        okta_app_list = []
        for item in okta_app_json:
            if item['status'] == 'ACTIVE':
                okta_app_list.append(item['label'])
        return okta_app_list
    
    @classmethod
    def get_app_dict(cls):
        okta_app_json = List_Okta_Apps.list()
        okta_app_dict = {}
        okta_app_dict_list = []
        for item in okta_app_json:
            if item['status'] == 'ACTIVE':
                okta_app_dict['label'] = item['label']
                okta_app_dict['deactivate'] = 'https://vinetidev.okta.com/api/v1/apps/{0}/lifecycle/deactivate'.format(item['id'])
                okta_app_dict['delete'] = 'https://vinetidev.okta.com/api/v1/apps/{0}'.format(item['id'])
                okta_app_dict_list.append(okta_app_dict.copy())
        return okta_app_dict_list

    def get_label_list():
        app_info_dict = List_Okta_Apps.get_app_dict()
        app_label_list = []
        for item in app_info_dict:
            app_label_list.append(item['label'])
        return app_label_list

    def apps_to_deactivate():
        applications_dict = List_Okta_Apps.get_app_dict()  
        applications_label_list = []
        deactivate_list = []
        for item in applications_dict:
            applications_label_list.append(item['label'])

        print("Applications count: " + str(len(applications_label_list)))

        applications_label_list = set(applications_label_list)

        for item in applications_label_list:
            for dict_item in applications_dict:
                if dict_item['label'] == item:
                    applications_dict.remove(dict_item)
                    break
        if str(len(applications_dict)) == 0:
            print("No Duplicatie applications found")
        else:
            print(str(len(applications_dict)) + " applications need to be deactivated.")
            return applications_dict

    def deactivate(app):
        deactivate_url = app['deactivate']
        print(app['label'])
        deactivate_req = requests.post(deactivate_url, headers=headers)
        print(deactivate_req.json())
    
    def delete_inactive():
        okta_app_json = List_Okta_Apps.list()
        okta_app_dict = {}
        okta_inactive_app_dict_list = []
        for item in okta_app_json:
            if item['status'] == 'INACTIVE':
                okta_app_dict['label'] = item['label']
                okta_app_dict['deactivate'] = 'https://vinetidev.okta.com/api/v1/apps/{0}/lifecycle/deactivate'.format(item['id'])
                okta_app_dict['delete'] = 'https://vinetidev.okta.com/api/v1/apps/{0}'.format(item['id'])
                okta_inactive_app_dict_list.append(okta_app_dict.copy())

        for item in okta_inactive_app_dict_list:
            delete_url = item['delete']
            print(item['label'])
            delete_req = requests.delete(delete_url, headers=headers)



applications_dict = List_Okta_Apps.apps_to_deactivate()

for item in applications_dict:
   List_Okta_Apps.deactivate(item)

# app_list = List_Okta_Apps.delete_inactive()
