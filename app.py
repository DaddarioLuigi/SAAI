from flask import Flask, render_template, request, jsonify, session
import requests
from flask_session import Session  # Potrebbe essere necessario installare flask-session

app = Flask(__name__)
app.secret_key = 'UrBoADfC8NUrBoADfC8NUrBoADfCfds8NUrBoADfC8NUrBoADfC8NUrBoADfC8NUrBoADfC8NUrBoADfC8NUrBoADfC8N'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    user_message = data['message']

    with open("kb.txt", "r") as file:
        contenuto = file.read()

    content = contenuto
    
    if 'conversation' not in session:
        session['conversation'] = []
        session['conversation'].append({"role": "system", "content": content})
    
    # Aggiungi il messaggio dell'utente allo storico
    session['conversation'].append({'role': 'user', 'content': user_message})
    
    # Prepara la payload per l'API, includendo lo storico della conversazione
    payload = {
        'model': 'gpt-3.5-turbo',
        'temperature': 0.1,
        'messages': 
            session['conversation']
        
    }
    
    # Effettua la chiamata API
    api_key = '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'
    headers = {'Authorization': f'Bearer {api_key}'}
   

    response = requests.post('https://api.openai.com/v1/chat/completions', json=payload, headers=headers)
    #print("Status Code:", response.status_code)  # Log status code
    
    #print("Response Body:", response.text)  # Log response body
    #print(session['conversation'])  # Stampa lo storico della conversazione per debug

    if response.status_code == 200:
        response_data = response.json()

        bot_response = response_data['choices'][0]['message']['content'].strip()
        # Aggiungi la risposta dell'assistente allo storico della conversazione
        session['conversation'].append({'role': 'assistant', 'content': bot_response})
        session.modified=True
    else:
        bot_response = "Mi dispiace, al momento non sono disponibile."
    
    return jsonify(bot_response)


if __name__ == '__main__':
    app.run(debug=True)
