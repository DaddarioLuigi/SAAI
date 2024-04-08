from sentence_transformers import SentenceTransformer, util

# Carica il modello pre-addestrato
model = SentenceTransformer('all-MiniLM-L6-v2')

# Elenco delle keywords o frasi rappresentative per ogni prodotto/servizio
# Lista delle tue keyword
keywords = ["vomito", "diarrea", "patologie intestinali", "prurito", "rossore cutaneo", "ulcere", "dermopigmentazioni della pelle", "obesità", "sovrappeso", "ostoartrite", "ulcere", "insufficienza renale", "infiammazione"]

# Frase inserita dall'utente
user_input = "Il mio cane ha problemi gastrointestinali, sono giorni che non mangia ma che dorme e basta"

# Calcola le embeddings per le keywords e per la frase dell'utente
keywords_embeddings = model.encode(keywords)
user_input_embedding = model.encode(user_input)

# Calcola la similarità semantica
similarities = util.cos_sim(user_input_embedding, keywords_embeddings)

# Stampa i punteggi di similarità
for keyword, similarity in zip(keywords, similarities[0]):
    print(f"Similarità con '{keyword}': {similarity.item():.4f}")
