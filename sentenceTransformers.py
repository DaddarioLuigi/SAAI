# Esempio con SentenceTransformers
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

keywords = ["vomito", "diarrea", "patologie intestinali", "prurito", "rossore cutaneo", "ulcere", "dermopigmentazioni della pelle", "obesità", "sovrappeso", "ostoartrite", "ulcere", "insufficienza renale", "infiammazione"]

# Calcola gli embedding
user_embedding = model.encode(["Credo ci sia un problema con il peso del mio cane!"])
keyword_embeddings = model.encode(keywords)

# Calcola la similarità del coseno
similarities = cosine_similarity(user_embedding, keyword_embeddings)[0]

# Associa ogni keyword al suo punteggio di similarità
keyword_similarities = dict(zip(keywords, similarities))

print(keyword_similarities)


# Trova la keyword più simile
most_similar_keyword = max(keyword_similarities, key=keyword_similarities.get)

print(most_similar_keyword)