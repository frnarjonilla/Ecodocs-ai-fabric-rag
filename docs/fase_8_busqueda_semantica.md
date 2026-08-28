# 🔍 Documentación Técnica: Fase 8 - Búsqueda Semántica (Retrieval)

## 📌 1. Objetivo
Implementar el motor de recuperación de información semántica (Retrieval) para evaluar preguntas en lenguaje natural frente a los vectores almacenados en la Capa Gold y devolver los $k$ fragmentos más relevantes junto con sus metadatos de trazabilidad.

---

## 🛠️ 2. Especificación del Motor de Búsqueda
* **Inferencia de la Pregunta:** Transformación de la consulta a vector mediante `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (384 dimensiones).
* **Métrica de Similitud:** Similitud Coseno calculada mediante producto escalar vectorizado con `numpy` en memoria distribuida.
* **Filtros Adicionales:** Capacidad opcional de filtrado por categoría documental (`document_category`).

---

## 🧪 3. Resultados de las Pruebas de Validación

| Tipo de Prueba | Consulta | Top 1 Score | Top 2 Score | Top 3 Score | Estado |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Prueba 1** | *¿Qué dice la empresa sobre teletrabajo?* | **0.53** | **0.47** | **0.46** | Validado |
| **Prueba 2** | *¿Tiempos de respuesta para averías en aerogeneradores?* | **0.56** | **0.55** | **0.49** | Validado |
| **Prueba 3** | *Procedimiento de compras (Filtro: Operations)* | **0.30** | **0.19** | -- | Validado |

---

## 📂 4. Entregables
* **Notebook:** `05_semantic_search`
* **Función Core:** `search_documents(question: str, top_k: int = 5, category_filter: str = None)`