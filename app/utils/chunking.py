from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_text_splitter(
    chunk_size: int = 1000,
    chunk_overlap: int = 150
):
    """
    Returns optimized recursive splitter for semantic continuity.
    """

    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )


def chunk_documents(documents):
    splitter = get_text_splitter()
    return splitter.split_documents(documents)
