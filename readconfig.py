import os
import configparser

config_file = "./.config"

if not os.path.isfile(config_file):
    print("Config file doest exist. Do you want to create .config ?")
    domain = input("Input okta domain name (without 'https://'): ")
    token = input("Input okta token: ")
    with open(config_file, 'w') as config:
        Config = configparser.ConfigParser()
        Config.add_section('okta')
        Config.set('okta', 'domain', domain)
        Config.set('okta', 'token', token)
        Config.write(config)
else:
    Config = configparser.RawConfigParser()
    Config.read(config_file)
    domain = Config.get('okta', 'domain')
    token = Config.get('okta', 'token')

print(domain)
print(token)