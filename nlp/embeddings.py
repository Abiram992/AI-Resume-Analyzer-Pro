from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# LOAD MODEL
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =========================
# SEMANTIC MATCHING
# =========================
def semantic_similarity(
    resume_text,
    job_description
):

    embeddings = model.encode([
        resume_text,
        job_description
    ])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(
        similarity * 100,
        2
    )