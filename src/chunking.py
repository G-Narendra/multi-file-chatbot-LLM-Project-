import re

def chunk_text(text, chunk_size=500, overlap=50):
    """
    Split text into overlapping chunks of specified size.

    Args:
        text (str): Full document text.
        chunk_size (int): Number of characters per chunk.
        overlap (int): Number of overlapping characters between chunks.

    Returns:
        List[str]: List of text chunks.
    """
    if not isinstance(text, str):
        return []

    text = re.sub(r'\s+', ' ', text).strip()

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks
