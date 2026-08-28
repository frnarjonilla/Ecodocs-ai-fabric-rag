"""
Módulo de cálculo de similitud coseno y recuperación de contexto (Retrieval).
"""
import numpy as np
from typing import List, Dict, Any

def cosine_similarity_search(
    query_vector: np.ndarray, 
    gold_cache: List[Any], 
    normalized_matrix: np.ndarray, 
    top_k: int = 5,
    category_filter: str = None
) -> List[Dict[str, Any]]:
    """
    Calcula la similitud coseno entre el vector de la pregunta y la matriz de embeddings Gold.
    Devuelve los top_k elementos ordenados por score.
    """
    if len(gold_cache) == 0:
        return []

    # Producto punto entre el vector normalizado de la consulta y la matriz normalizada
    scores = np.dot(normalized_matrix, query_vector)
    
    results = []
    for idx, score in enumerate(scores):
        rec = gold_cache[idx]
        
        if category_filter and getattr(rec, 'document_category', '').lower() != category_filter.lower():
            continue
            
        results.append({
            "chunk_id": rec.chunk_id,
            "document_id": rec.document_id,
            "score": float(score),
            "document_title": rec.document_title,
            "document_category": rec.document_category,
            "source_url": rec.source_url,
            "page_number": rec.page_number,
            "chunk_text": rec.chunk_text
        })
        
    results_sorted = sorted(results, key=lambda x: x["score"], reverse=True)[:top_k]
    return results_sorted