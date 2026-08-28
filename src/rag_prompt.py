"""
Módulo para la construcción de prompts y la invocación del LLM.
"""
from typing import List, Dict, Any
from openai import OpenAI

SYSTEM_PROMPT = """Eres EcoDocs AI, un asistente documental interno de EcoPower Solutions.
Responde únicamente usando el contexto proporcionado.
No inventes información.
Si el contexto no contiene información suficiente, responde:
"No tengo información suficiente en los documentos disponibles."
Incluye siempre las fuentes usadas al final."""

def build_user_prompt(context_blocks: List[str], user_question: str) -> str:
    """
    Ensambla el bloque de contexto recuperado con la pregunta del usuario.
    """
    context_str = "\n\n".join(context_blocks)
    return f"Contexto:\n{context_str}\n\nPregunta:\n{user_question}\n\nRespuesta:"

def generate_rag_response(
    client: OpenAI, 
    model_name: str, 
    user_prompt: str, 
    temperature: float = 0.1
) -> str:
    """
    Llama a la API del LLM utilizando la plantilla de sistema con guardrails.
    """
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error en generación LLM: {str(e)}"