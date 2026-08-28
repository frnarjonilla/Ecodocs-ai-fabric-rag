"""
Módulo de chunking y segmentación de texto para la Capa Gold.
"""
from typing import List, Dict, Any

def recursive_text_splitter(
    text: str, 
    chunk_size: int = 500, 
    chunk_overlap: int = 50
) -> List[str]:
    """
    Divide un texto largo en fragmentos más pequeños utilizando separadores prioritarios
    (\\n\\n, \\n, espacio, carácter) para preservar la coherencia semántica.
    """
    if not text or not text.strip():
        return []

    separators = ["\n\n", "\n", ". ", " ", ""]
    
    def _split(text_block: str, seps: List[str]) -> List[str]:
        if len(text_block) <= chunk_size or not seps:
            return [text_block] if text_block.strip() else []
        
        sep = seps[0]
        splits = text_block.split(sep) if sep != "" else list(text_block)
        
        chunks = []
        current_chunk = ""
        
        for s in splits:
            item = s + sep if sep != "" else s
            if len(current_chunk) + len(item) <= chunk_size:
                current_chunk += item
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = item
                
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
            
        # Si un bloque sigue superando el tamaño máximo, recurrir al siguiente separador
        final_chunks = []
        for c in chunks:
            if len(c) > chunk_size and len(seps) > 1:
                final_chunks.extend(_split(c, seps[1:]))
            else:
                final_chunks.append(c)
                
        return final_chunks

    raw_chunks = _split(text, separators)
    
    # Aplicar solapamiento (overlap)
    if chunk_overlap <= 0 or len(raw_chunks) <= 1:
        return raw_chunks
        
    overlapped_chunks = []
    for i, chunk in enumerate(raw_chunks):
        if i == 0:
            overlapped_chunks.append(chunk)
        else:
            prev_tail = raw_chunks[i-1][-chunk_overlap:]
            overlapped_chunks.append(f"{prev_tail} {chunk}".strip())
            
    return overlapped_chunks