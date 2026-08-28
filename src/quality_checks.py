"""
Módulo de reglas de calidad de datos para la extracción de texto en Silver.
"""
from typing import Tuple, Dict, Any

def validate_extracted_text(
    text: str, 
    min_length: int = 50, 
    max_non_printable_ratio: float = 0.05
) -> Tuple[bool, str]:
    """
    Valida si el texto extraído cumple con las métricas mínimas de calidad.
    Devuelve (True, 'OK') si pasa, o (False, Razón) si debe desecharse/revisarse.
    """
    if not text or not text.strip():
        return False, "EMPTY_TEXT"
        
    cleaned_text = text.strip()
    
    if len(cleaned_text) < min_length:
        return False, f"TEXT_TOO_SHORT (length: {len(cleaned_text)} < {min_length})"
        
    # Calcular proporción de caracteres no imprimibles o de control
    non_printable = sum(1 for c in cleaned_text if not c.isprintable() and c not in ['\n', '\r', '\t'])
    ratio = non_printable / len(cleaned_text)
    
    if ratio > max_non_printable_ratio:
        return False, f"HIGH_CORRUPTION_RATIO ({ratio:.2f} > {max_non_printable_ratio})"
        
    return True, "PASSED_QUALITY_CHECK"