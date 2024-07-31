import requests

def fetch_data():
    try:
        response = requests.get('http://bff:5000/')
        response.raise_for_status()  
        data = response.text  
        print(data)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    fetch_data()