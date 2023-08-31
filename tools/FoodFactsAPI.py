import requests

# Replace with the actual API endpoint and parameters
API_ENDPOINT = 'https://public.opendatasoft.com/api/records/1.0/search/'
PARAMS = {'dataset': 'your-dataset', 'q': 'your-query'}

def get_open_data_records():
    response = requests.get(API_ENDPOINT, params=PARAMS)
    data = response.json()
    return data['records']

# Example usage
records = get_open_data_records()
for record in records:
    print("Record:", record['fields'])