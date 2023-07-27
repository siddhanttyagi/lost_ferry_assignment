from flask import Flask, request, jsonify
import requests

app = Flask(__name__)



@app.route('/posts', methods=['POST'])
def create_post():
    try:
        
        data = request.get_json()
        term = data.get('title')
        media= data.get('content')
        entity=data.get('entity')
        apiurl='https://itunes.apple.com/search'
        query_params={
            "term": term,
            "media": media,
            "entity": entity
        }
        response = requests.get(apiurl, params=query_params)
        if response:

            data = response.json()
            list_of_songs=[]
            for sub_dict in data['results']:
                list_of_songs.append(sub_dict['collectionName'])
                print(sub_dict['collectionName'])
            return {"data": list_of_songs}

    except Exception as e:
        # Return an error response if something goes wrong
        return jsonify({"error": str(e)}), 500



    


if __name__ == '__main__':
    app.run()
