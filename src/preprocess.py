import re

# Terms that must survive cleaning verbatim (case-insensitive match first,
# stored lowercase so comparison works after text.lower()).
IMPORTANT_TERMS: frozenset[str] = frozenset({
    "c++", "c#", "node.js", "react.js", ".net", "asp.net",
    "machine learning", "deep learning", "nlp",
    "sql", "python", "java", "aws",
    "excel", "powerbi", "power bi", "tableau",
    "active directory", "windows server", "project management",
    "data analysis", "technical support", "troubleshooting"
})

STOPWORDS: frozenset[str] = frozenset({
    "the", "and", "is", "in", "to", "of", "for", "on", "with",
    "a", "an", "by", "this", "that", "from", "at", "as", "it",
    "are", "was", "were", "be", "been", "has", "have", "had",
    "its", "or", "but", "not", "so", "if", "do", "no", "up",
})

# Minimum token length kept (unless it is an important term).
MIN_TOKEN_LEN = 2


def _protect_important_terms(text: str) -> tuple[str, dict[str, str]]:
    """
    Replace multi-word important terms with placeholder tokens so they are
    not broken apart during tokenisation.  Returns the modified text and a
    mapping from placeholder → original term.
    """
    placeholders: dict[str, str] = {}
    for i, term in enumerate(sorted(IMPORTANT_TERMS, key=len, reverse=True)):
        if " " in term and term in text:
            key = f"__TERM{i}__"
            placeholders[key] = term
            text = text.replace(term, key)
    return text, placeholders


def clean_text(text: str) -> str:
    """
    Normalise raw resume / job-description text for downstream NLP steps.

    Pipeline
    --------
    1. Lowercase.
    2. Protect multi-word important terms with placeholders.
    3. Strip repeated separators (===, ---, etc.).
    4. Collapse line-breaks and punctuation to spaces.
    5. Collapse whitespace.
    6. Tokenise; remove stopwords and very short tokens.
    7. Restore important-term placeholders.
    """
    if not isinstance(text, str):
        raise TypeError(f"clean_text expects str, got {type(text).__name__}")

    text = text.lower()
    text, placeholders = _protect_important_terms(text)

    # Remove separator lines (==, --, __, ...)
    text = re.sub(r'[=\-_]{2,}', ' ', text)
    # Collapse newlines
    text = re.sub(r'\n+', ' ', text)
    # Keep alphanumeric, +, #, dot (for version numbers), and spaces
    text = re.sub(r'[^a-z0-9+#.\s]', ' ', text)
    # Collapse multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()

    tokens = []
    for word in text.split():
        if word in placeholders:
            tokens.append(placeholders[word])  # restore "machine learning" etc.
        elif word in IMPORTANT_TERMS:
            tokens.append(word)
        elif word not in STOPWORDS and len(word) > MIN_TOKEN_LEN:
            tokens.append(word)

    return " ".join(tokens)
