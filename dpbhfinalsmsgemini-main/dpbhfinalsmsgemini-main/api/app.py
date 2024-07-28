from flask import Flask, jsonify, request
from flask_cors import CORS
from joblib import load
import csv
from twilio.rest import Client
import warnings
from sklearn.exceptions import InconsistentVersionWarning

# Ignore inconsistent version warnings
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

# Load machine learning models
presence_classifier = load('presence_classifier.joblib')
presence_vect = load('presence_vectorizer.joblib')
category_classifier = load('category_classifier.joblib')
category_vect = load('category_vectorizer.joblib')

# Twilio API credentials
#insert your own api keys and number 
account_sid = ''
auth_token = ''
twilio_phone_number = ''
recipient_phone_number = ''

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        output = []
        data = request.get_json().get('tokens')

        for token in data:
            result = presence_classifier.predict(presence_vect.transform([token]))
            if result == 'Dark':
                cat = category_classifier.predict(category_vect.transform([token]))
                output.append(cat[0])
                send_sms(token)  # Send SMS when dark pattern is detected
            else:
                output.append(result[0])

        dark = [data[i] for i in range(len(output)) if output[i] == 'Dark']

        # Writing to CSV file
        csv_file_name = 'output.csv'
        with open(csv_file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Result'])
            csv_writer.writerows([[item] for item in output])

        # Writing to text file
        text_file_name = 'output.txt'
        with open(text_file_name, 'w') as text_file:
            text_file.write('\n'.join(output))

        print(f'Data written to {csv_file_name} and {text_file_name}')

        message = {'result': output}
        return jsonify(message)

def send_sms(token):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'Dark pattern detected: {token}',
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f'SMS sent: {message.sid}')

if __name__ == '__main__':
    app.run(threaded=True, debug=True)

// use this 

