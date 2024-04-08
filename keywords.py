from transformers import AutoModel, AutoTokenizer
import torch
from scipy.spatial.distance import cosine

# Carica il tokenizer e il modello
model_name = "bert-base-multilingual-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Funzione per calcolare l'embedding di una frase
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze()

# Lista delle tue keyword (anche frasi composte da più parole)
keywords = ["vomito", "diarrea", "patologie intestinali", "prurito", "rossore cutaneo", "ulcere", "dermopigmentazioni della pelle", "obesità", "sovrappeso", "ostoartrite", "ulcere", "insufficienza renale", "infiammazione"]

# Frase fornita dall'utente
user_text = "Il mio cane sta vomitando"

# Calcola gli embedding per la frase e per ciascuna keyword
user_embedding = get_embedding(user_text)
keyword_embeddings = {keyword: get_embedding(keyword) for keyword in keywords}

# Calcola la similarità del coseno tra la frase dell'utente e ogni keyword
similarities = {keyword: 1 - cosine(user_embedding.detach().numpy(), emb.detach().numpy()) for keyword, emb in keyword_embeddings.items()}

print(similarities)

# Trova la keyword più simile
most_similar_keyword = max(similarities, key=similarities.get)

print(f"La keyword più simile a '{user_text}' è: '{most_similar_keyword}' con una similarità del coseno di {similarities[most_similar_keyword]:.4f}")
