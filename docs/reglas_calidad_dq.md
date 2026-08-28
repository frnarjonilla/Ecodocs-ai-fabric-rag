# 🛡️ Marcos de Calidad de Datos (Data Quality Framework) - EcoDocs AI

Este documento define la metodología, reglas de negocio y criterios de evaluación aplicados en la **Capa Silver** para la limpieza de texto y cálculo del **Quality Score ($QS$)**.

---

## 1. Pipeline de Limpieza y Normalización

Antes de evaluar la calidad del texto, cada documento atraviesa el pipeline `02_clean_normalize_text`:
1. **Normalización Unicode:** Conversión a norma NFC, estandarización de comillas, guiones y eliminación de caracteres nulos (`\x00`).
2. **Filtrado de Ruido:** Eliminación de patrones de cabecera y pie de página mediante expresiones regulares (ej. paginaciones tipo "Página X de Y", fechas estáticas).
3. **Estandarización de Espaciado:** 
   * Sustitución de saltos de línea rotos a mitad de frase por espacios.
   * Reducción de múltiples saltos de línea a un máximo de 2 (separación de párrafos).
   * Reducción de espacios horizontales continuos a 1 solo espacio.
4. **Detección de Idioma:** Identificación del código ISO 639-1 (`es`, `en`, etc.) mediante `langdetect`.

---

## 2. Algoritmo de Cálculo del Quality Score ($QS$)

El **Quality Score** se calcula sobre una escala de **0 a 100 puntos**. Todos los documentos inician con 100 puntos y sufren penalizaciones acumulativas si incumplen los siguientes criterios:

| Regla / Criterio | Condición de Infracción | Penalización | Justificación Técnica |
| :--- | :--- | :---: | :--- |
| `DQ_ERR_01` | **Sin Texto Extraíble** (`clean_text` vacío o nulo) | **-30 ptos** | El documento no aporta información utilizable para los modelos de LLM/RAG. |
| `DQ_ERR_02` | **Longitud Insuficiente** (`num_characters` < 500) | **-20 ptos** | Contenido demasiado escaso para generar fragmentos semánticos (chunks) de calidad. |
| `DQ_ERR_03` | **Sin Categoría Asignada** (`category` nula o 'unknown') | **-10 ptos** | Dificulta el filtrado por metadatos en búsquedas semánticas vectoriales. |
| `DQ_ERR_04` | **Falta Trazabilidad de Origen** (`source_url` nula) | **-10 ptos** | Impide al usuario final/LLM verificar la fuente original del documento. |
| `DQ_ERR_05` | **Metadato de Título Incompleto** (`title` nulo) | **-10 ptos** | Incompleto para la generación de citas en las respuestas del RAG. |

---

## 3. Clasificación de Estados (`quality_status`)

Según el resultado final del $QS$, el sistema asigna uno de los siguientes tres estados:

* **`valid` ($80 \le QS \le 100$):** Documento con alta calidad de texto y metadatos completos. Apto para ingestión inmediata en la Capa Gold (Vector Search).
* **`warning` ($50 \le QS < 80$):** Documento procesable pero con deficiencias de longitud o metadatos faltantes. Pasa a la Capa Gold marcando la advertencia.
* **`invalid` ($QS < 50$):** Documento rechazado debido a texto corrupto o nulo. Se descarta para el RAG y se genera una alerta para revisión/remediación.