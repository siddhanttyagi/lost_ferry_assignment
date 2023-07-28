from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    term = data.get('title', '')  # Default to empty string if not provided
    media = data.get('content', '')  # Default to empty string if not provided
    entity = data.get('entity', '')  # Default to empty string if not provided

    apiurl = 'https://itunes.apple.com/search'
    
    # Prepare the query parameters, excluding empty parameters
    params = {
        key: value for key, value in {
            'term': term,
            'media': media,
            'entity': entity,
        }.items() if value
    }

    # Make a GET request to the iTunes API
    response = requests.get(apiurl, params=params)

    if response.status_code == 200:
        # Successful response
        result_data = response.json()
        print(result_data)
        return {'data': result_data}
    else:
        # Error occurred while fetching data
        error_message = f"Error: {response.status_code} - {response.text}"
        return jsonify({'data': [], 'error': error_message}), response.status_code





if __name__ == '__main__':
    app.run()
