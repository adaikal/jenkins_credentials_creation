#!/usr/bin/python
import requests
import uuid

random_uuid = uuid.uuid4()
print random_uuid
url = "http://192.168.54.214:8080/credential-store/domain/_/createCredentials"

payload = '''json={
        "": "0", 
        "credentials": {
            "scope": "GLOBAL", 
            "id": "%s", 
            "username": "adaikal", 
            "password": "xxxyyyzzz", 
            "description": "biz", 
            "$class": "com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl"
        }
    }''' % random_uuid
headers = {
    'content-type': "application/x-www-form-urlencoded",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
