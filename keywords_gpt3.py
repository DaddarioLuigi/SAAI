import requests

def calcola_similarita_gpt3(testo_utente):
    api_key = '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'
    headers = {'Authorization': f'Bearer {api_key}'}
    
    # La struttura corretta per GPT-3.5 Turbo richiede che 'messages' sia un array
    payload = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {"role": "system", "content": "Quali sono le tre keywords piu semanticamente vicine a questa frase?Rispondi in formato csv e scrivi anche il punteggio di similarita' per ognuna delle 3 top."},
            {"role": "user", "content": f"Frase: '{testo_utente}'. Keywords: 'vomito, diarrea, patologie intestinali, prurito, rossore cutaneo, ulcere, dermopigmentazioni della pelle, obesità, sovrappeso, ostoartrite, ulcere, insufficienza renale, infiammazione'."}
        ]
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', json=payload, headers=headers)
    response_data = response.json()

    try:
        # Assumi che la risposta sia nel primo messaggio e estrai il contenuto
        score = response_data['choices'][0]['message']['content'].strip()
        print(score)
        return float(score.split()[-1])  # Assumi che l'ultimo elemento sia il punteggio
    except (KeyError, IndexError, ValueError) as e:
        print(f"Errore nell'elaborazione della risposta: {e}")
        return None


# Frase fornita dall'utente
user_text = "Ma il mio cane non e' obeso!"

# Calcola la "similarità" per ciascuna keyword
similarities = calcola_similarita_gpt3(user_text)

print(similarities)


