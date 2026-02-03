import requests

# Example: Fetch data from a public test API
url = "https://www.divyabhaskar.co.in/rashifal/13/today?ref=inbound_RHS"   # fake API for testing

try:
    response = requests.get(url, timeout=10)           # timeout prevents hanging forever

    # Check if request was successful (status 200 = OK)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: Server returned {response.status_code}")
        print(response.text)                           # see error message from server

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")