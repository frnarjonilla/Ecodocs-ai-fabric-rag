"""
Módulo para la generación de embeddings vectoriales densos.
"""
import numpy as np
from typing import List, Union
from sentence_transformers import SentenceTransformer

class EmbeddingManager:
    def __init__(self, model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"):
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name)

    def generate_embeddings(self, texts: Union[str, List[str]], normalize: bool = True) -> np.ndarray:
        """
        Genera vectores de 384 dimensiones para un texto individual o una lista de textos.
        """
        if isinstance(texts, str):
            texts = [texts]
            
        embeddings = self.model.encode(
            texts, 
            normalize_embeddings=normalize, 
            show_progress_bar=False
        )
        return np.array(embeddings, dtype=np.float32)