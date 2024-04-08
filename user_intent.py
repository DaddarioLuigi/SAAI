from transformers import pipeline

# Carica una pipeline NER pre-addestrata
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", tokenizer="dbmdz/bert-large-cased-finetuned-conll03-english")

# Testo da analizzare
text = "Vorrei capire quali siano i problemi del mio gatto, vomita sempre"

# Esegui la pipeline NER sul tuo testo
ner_results = ner_pipeline(text)

# Stampa le entità riconosciute e le loro categorie
for entity in ner_results:
    print(f"Entità: {entity['word']}, Categoria: {entity['entity']}")
