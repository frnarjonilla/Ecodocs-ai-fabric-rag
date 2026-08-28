# 📐 Documentación Técnica: Fase 7 - Generación de Embeddings (Capa Gold)

## 📌 1. Objetivo
Transformar los fragmentos de texto limpios de la tabla `gold_document_chunks` en vectores numéricos densos para habilitar búsquedas por similitud semántica en el sistema RAG.

---

## 🛠️ 2. Especificación del Modelo
* **Modelo Utilizado:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
* **Dimensión Vectorial:** 384 dimensiones (`ARRAY<DOUBLE>`).
* **Justificación:** Optimizado para textos multilingües (con especial soporte en español), baja latencia de inferencia y alto rendimiento semántico en arquitecturas RAG ligeras.
* **Normalización:** Embeddings normalizados para permitir cálculo directo de similitud coseno o producto escalar.

---

## 🚀 3. Estrategia de Procesamiento y Buenas Prácticas
1. **Procesamiento por Lotes (Batching):** Ejecución en lotes de `batch_size = 32` para optimizar la memoria RAM y acelerar la codificación.
2. **Mecanismo Anti-recalculo (Caching / Incremental Load):**
   * Lectura previa de los `chunk_id` existentes en `gold_embeddings`.
   * Filtrado automático para vectorizar únicamente los chunks de nueva incorporación.
   * Inserción en modo `append` para preservar los registros vectorizados en ejecuciones previas.
3. **Compatibilidad con PySpark en Microsoft Fabric:**
   * Fijado de versiones compatibles (`transformers<4.41.0`, `sentence-transformers<3.0.0`) para mantener la integración nativa con PyTorch 2.2.1 en el clúster.

---

## 📊 4. Diccionario de Datos (`LH_Ecodocs.gold_embeddings`)

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `chunk_id` | `STRING` | Clave primaria y foránea vinculada a `gold_document_chunks`. |
| `document_id` | `STRING` | Clave foránea al documento origen (`silver_documents`). |
| `embedding` | `ARRAY<DOUBLE>` | Vector denso de 384 números flotantes. |
| `embedding_model` | `STRING` | Nombre del modelo de Hugging Face empleado. |
| `embedding_dimension` | `INT` | Tamaño del vector numérico (384). |
| `created_at` | `TIMESTAMP` | Marca de tiempo exacta de la generación del vector. |