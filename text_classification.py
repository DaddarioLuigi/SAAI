
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import torch

# Carica il tokenizer e il modello preaddestrato per la classificazione
tokenizer = BertTokenizer.from_pretrained('dbmdz/bert-base-italian-xxl-cased')
model = BertForSequenceClassification.from_pretrained('dbmdz/bert-base-italian-xxl-cased')

# Carica un modello NER preaddestrato
# Carica un modello NER preaddestrato (modifica qui con un modello NER multilingue)
ner_model = pipeline("ner", model="bert-base-multilingual-cased", tokenizer=tokenizer)

# Definisci le categorie e le keyword preset (esempi)
categorie_preset = ["Mangimi medicati", "Parafarmacia veterinaria", "Integratori"]

# Funzione di predizione della categoria e delle keyword
def predici_categoria(testo):
    # Prepara l'input per BERT
    inputs = tokenizer(testo, return_tensors="pt", padding=True, truncation=True, max_length=512)
    
    # Ottieni le predizioni del modello di classificazione
    with torch.no_grad():
        outputs = model(**inputs)
    
    print(outputs.logits)

    # Seleziona la categoria con il logit più alto
    categoria_predetta_idx = outputs.logits.argmax().item()
    categoria_predetta = categorie_preset[categoria_predetta_idx]
    
    
    return categoria_predetta

# Esempio di utilizzo
testo_input = "Il mio cane vomita sempre!"
categoria = predici_categoria(testo_input)
print(f"Categoria predetta: {categoria}")
