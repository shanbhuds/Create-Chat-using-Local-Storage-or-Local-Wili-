import requests
from requests.auth import HTTPBasicAuth
def gate_data_confluance(url="http local host address"):
    # Define the URL
    # url = "  your local path"

    # Define your username and password
    username = 'Admin'
    password = 'your password '

    # Make the GET request with authentication
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(response)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Print the data or process it as needed
        print(len(data['results']))
        l=[]
        for i in data['results'][1:]:
            l.append(i['body']['storage']['value'])
            print(i['body']['storage']['value'])
        return l
    #         print(i)
    #         print(i['body']['storage']['value'])
    else:
        return f"Failed to retrieve data: {response.status_code}"
