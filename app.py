from flask import Flask,jsonify
import requests

app=Flask(__name__)


@app.route('/docks_available',methods=['GET'])
def total_docks():
    try:
        url = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"

        response = requests.get(url)
        data = response.json()

        stations = data['data']['stations']
        total_docks_available = sum(station['num_docks_available'] for station in stations)

        return jsonify({"Total_docks_available" : total_docks_available})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error" : str(e)}), 500
    except KeyError :
        return jsonify({'error': 'Invalid response format'}), 500
 




@app.route('/bikes_available',methods=['GET'])
def total_bikes():
    try:
        url = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"

        response = requests.get(url)
        data = response.json()

        stations = data['data']['stations']
        total_bikes_available = sum(station['num_bikes_available'] for station in stations)
        

        return jsonify({"Total_bike_available" : total_bikes_available})
    

    except requests.exceptions.RequestException as e:
        return jsonify({"error" : str(e)}), 500
    
    except KeyError :
        return jsonify({'error': 'Invalid response format'}), 500
    


@app.route('/station_active',methods=['GET'])
def total_station():
    try:
        url = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"

        response = requests.get(url)
        data = response.json()

        stations = data['data']['stations']
        stations_available=0
        for x in stations:
            if x['station_status'] == 'active':
                stations_available+=1
        return jsonify ({"Total_Station_available" : stations_available})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error" : str(e)}), 500
    
    except KeyError :
        return jsonify({'error': 'Invalid response format'}), 500


@app.route('/reserved_bike',methods=['GET'])
def reserved():
    try:
        url = "https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json"
        response = requests.get(url)
        data = response.json()

        bikes = data['data']['bikes']
        total_reserved_bikes = sum(bike['is_reserved'] for bike in bikes)

        return jsonify ({"Total_bike_reserved " : total_reserved_bikes})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error" : str(e)}), 500
    
    except KeyError :
        return jsonify({'error': 'Invalid response format'}), 500






if __name__ == "__main__":
    app.run(debug=True)