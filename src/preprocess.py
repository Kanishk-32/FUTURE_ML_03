import re

IMPORTANT_TERMS = {
    "c++", "c#", "node.js", "react.js", "machine learning",
    "deep learning", "nlp", "sql", "python", "java", "aws",
    "excel", "powerbi", "tableau"
}

STOPWORDS = {
    "the", "and", "is", "in", "to", "of", "for", "on", "with",
    "a", "an", "by", "this", "that", "from", "at", "as", "it",
    "are", "was", "were", "be", "been", "has", "have", "had"
}


def clean_text(text):

    text = text.lower()

    text = re.sub(r'[=\\-]{2,}', ' ', text)

    text = re.sub(r'\n+', ' ', text)

    text = re.sub(r'[^a-z0-9+#.\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text).strip()

    tokens = text.split()

    cleaned_tokens = []

    for word in tokens:
       
        if word in IMPORTANT_TERMS:
            cleaned_tokens.append(word)
            continue

       
        if word not in STOPWORDS and len(word) > 2:
            cleaned_tokens.append(word)

    return " ".join(cleaned_tokens)