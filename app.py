from flask import Flask, render_template, request
import requests, binascii

app = Flask(__name__)

w3w_api_key = 'R39N1XC0'

# Function to convert 3 words to coordinates
def words_to_coords(words):
    # Create the API URL
    api_url = f'https://api.what3words.com/v3/convert-to-coordinates?words={words}&key={w3w_api_key}'

    # Make the API request
    response = requests.get(api_url)
    data = response.json()
    altitude_binary=''

    if 'coordinates' in data:
        coordinates = data['coordinates']
        latitude, longitude = coordinates['lng'], coordinates['lat']
    else:
        return None, None, None
    
    for i in range(len(words)):
        if words[i] =='.':
            continue
        if words[i].isupper():
            altitude_binary += '1'
        else:
            altitude_binary += '0'

    # Convert binary to altitude
    altitude = int(altitude_binary[:9], 2) * 3
    return latitude,longitude,altitude    


# Function to convert coordinates to 3 words
def coords_to_words(latitude, longitude, altitude):
    # Create the API URL
    coordinates = f'{latitude},{longitude}'
    api_url = f'https://api.what3words.com/v3/convert-to-3wa?coordinates={coordinates}&key={w3w_api_key}'

    # Make the API request
    response = requests.get(api_url)
    data = response.json()
   # return data['words']

    if 'words' in data:
        words = data['words']
        words= str(words)
        #return words
        
    else:
        return None
    
    # Convert altitude to binary and modify 3 words
    altitude_binary = bin(int(altitude) // 3)[2:].zfill(9)

    # Modify the 3 words based on the binary representation
    i,j=0,0
    while j<(len(altitude_binary)):
        if words[i]=='.':
            i=i+1
            continue
        if altitude_binary[j] == '1':
            words = words[:i] + words[i].upper() + words[i+1:]
        i+=1
        j+=1
    return words 




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/coords_to_words', methods=['POST'])
def coords_to_words_route():
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])
    altitude = int(request.form['altitude'])
    words = coords_to_words(latitude, longitude, altitude)
    return render_template('result.html', words=words)

@app.route('/words_to_coords', methods=['POST'])
def words_to_coords_route():
    words = request.form['words']
    latitude, longitude, altitude = words_to_coords(words)
    return render_template('result.html', latitude=latitude, longitude=longitude, altitude=altitude)

if __name__ == '__main__':
    app.run(debug=True)
