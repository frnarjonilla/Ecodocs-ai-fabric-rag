# 🛠️ Documentación Técnica: Capas Bronze, Silver y Gold (Fases 3 a 6)

## 📌 1. Arquitectura del Pipeline de Datos

El pipeline procesa documentación no estructurada aplicando la arquitectura Medallion en **Microsoft Fabric**:

## 📥 2. Fase 3: Ingesta en Capa Bronze
* **Objetivo:** Registrar archivos en bruto y generar metadatos sin alterar el contenido original.
* **Orquestación:** Data Pipeline de Data Factory (`PL_Ingesta_EcoDocs`).
* **Mecanismo de Inserción:** MERGE idempotente en Delta Lake utilizando el hash `MD5(file_name)` como `document_id`.
* **Clasificación por Prefijo:** Detección automática de categoría mediante prefijos de nombre (`hr_`, `legal_`, `security_`, etc.).
* **Estados Iniciales:** `pending` para formatos soportados (`.pdf`, `.txt`, `.md`, `.docx`, `.xlsx`, `.csv`) y `skipped` para formatos no soportados.

---

## 🧹 3. Fases 4 y 5: Extracción, Limpieza y Calidad (Capa Silver)

### Extracción Multi-formato
Soporte modular para extracción de texto con librerías nativas de Python/Spark:
* **PDF:** Extracción vía `pdfplumber` (con fallback automático a `pypdf`).
* **Word (`.docx`):** `python-docx`.
* **Excel / CSV:** `pandas` / `openpyxl` transformando estructuras tabulares en bloques de texto formateado.
* **Texto plano / Markdown:** Lectura nativa UTF-8.

### Normalización de Texto
1. **Limpieza Unicode:** Normalización `NFC` y preservación de diacríticos y caracteres en español.
2. **Filtrado de Ruido:** Eliminación de encabezados/pies de página repetitivos (patrones de paginación y fechas) mediante expresiones regulares (`re`).
3. **Control de Espaciado:** Reemplazo de saltos de línea a mitad de frase y consolidación de múltiples espacios en blanco.

### Matriz de Calidad de Datos (Data Quality Framework)
Cada documento se evalúa sobre un **Quality Score (0 a 100)** aplicando las siguientes reglas de negocio:

| Criterio | Condición | Penalización |
| :--- | :--- | :---: |
| **Puntuación Base** | Estado inicial | **100 pts** |
| **Texto Vacío** | `clean_text` nulo o sin contenido | **-30 pts** |
| **Longitud Insuficiente** | `< 500` caracteres | **-20 pts** |
| **Categoría Ausente** | Categoría no identificada (`unknown`) | **-10 pts** |
| **Sin Ruta Origen** | `source_url` no definido | **-10 pts** |
| **Sin Título** | `document_title` nulo | **-10 pts** |

**Ubicación de estados (`quality_status`):**
* **`valid`** ($\ge 80$ pts): Apto para producción RAG.
* **`warning`** ($50 - 79$ pts): Apto pero con metadatos limitados.
* **`invalid`** ($< 50$ pts): Descartado para la capa Gold.

---

## 🧩 4. Fase 6: Fragmentación (Capa Gold)

* **Objetivo:** Dividir documentos limpios en fragmentos procesables para el motor de búsqueda semántica.
* **Filtrado de Entrada:** Procesa únicamente registros de Silver en estado `valid` o `warning`.
* **Estrategia de Chunking:**
  * **Tamaño objetivo:** ~700 tokens (~2.800 caracteres).
  * **Solapamiento (Overlap):** ~120 tokens (~480 caracteres) para preservar el contexto inter-chunk.
  * **Algoritmo:** Splitter recursivo por jerarquía de delimitadores (`\n\n`, `\n`, `. `, ` `).
* **Estructura de Salida (`gold_document_chunks`):**
  * Metadatos preservados: `document_id`, `chunk_number`, `document_category`, `document_title`, `source_url`, `page_number`.
  * Clave primaria: `chunk_id` (`CHK_<hash_md5>`).

---

## 📊 5. Diccionario de Datos del Lakehouse (`LH_Ecodocs`)

### `bronze_documents`
* `document_id` (STRING) [PK]
* `file_name` (STRING)
* `file_path` (STRING)
* `file_type` (STRING)
* `category` (STRING)
* `file_size` (LONG)
* `ingestion_date` (TIMESTAMP)
* `processing_status` (STRING): `pending`, `processed`, `failed`, `skipped`
* `error_message` (STRING)

### `silver_documents`
* `document_id` (STRING) [PK]
* `file_name` (STRING)
* `document_title` (STRING)
* `document_category` (STRING)
* `language` (STRING)
* `clean_text` (STRING)
* `num_pages` (INT)
* `num_characters` (INT)
* `num_words` (INT)
* `source_url` (STRING)
* `quality_score` (DOUBLE)
* `quality_status` (STRING): `valid`, `warning`, `invalid`
* `extraction_date` (TIMESTAMP)

### `gold_document_chunks`
* `chunk_id` (STRING) [PK]
* `document_id` (STRING) [FK]
* `chunk_number` (INT)
* `chunk_text` (STRING)
* `chunk_size` (INT)
* `document_category` (STRING)
* `document_title` (STRING)
* `source_url` (STRING)
* `page_number` (INT)
* `created_at` (TIMESTAMP)