# Catálogo Documental Inicial - EcoDocs AI

Este documento registra el inventario inicial de fuentes de información utilizadas en el proyecto para validar el pipeline de datos (Medallion) y el asistente de Inteligencia Artificial (RAG).

## 📊 Resumen del Dataset
* **Total de Documentos Registrados:** 8 documentos (3 reales de fuentes públicas y 5 internos/ficticios).
* **Categorías cubiertas:** Legal (legal), Human Resources (hr), Technical (technical), Environmental, Social & Governance (esg), Financial (financial), Security (security), Operations (operations).
* **Formatos:** PDF (documentos externos/formales) y TXT/Markdown (comunicaciones internas).

---

## 🗂️ Inventario de Documentos por Categoría

### 1. Human Resources (hr)
* **Doc ID:** `HR-001`
* **Nombre de Archivo:** `politica_teletrabajo_ecopower.txt`
* **Tipo:** Ficticio (Interno)
* **Descripción:** Regula las condiciones de teletrabajo, jornadas híbridas y uso de VPN para empleados de oficina.
* **Pregunta de Prueba:** ¿Cuántos días a la semana se permite teletrabajar en EcoPower?

### 2. Security & Prevention (security)
* **Doc ID:** `SE-001`
* **Nombre de Archivo:** `manual_seguridad_plantas_solares.txt`
* **Tipo:** Ficticio (Interno)
* **Descripción:** Protocolos de parada de emergencia y uso obligatorio de Equipos de Protección Individual (EPI) en parques fotovoltaicos.
* **Pregunta de Prueba:** ¿Cuáles son los EPI obligatorios para intervenir un inversor solar?

### 3. Operations (operations)
* **Doc ID:** `OP-001`
* **Nombre de Archivo:** `procedimiento_compras_proveedores.txt`
* **Tipo:** Ficticio (Interno)
* **Descripción:** Flujo de aprobación de compras de tecnología y evaluación bajo cumplimiento NIS2.
* **Pregunta de Prueba:** ¿A partir de qué importe se requieren tres presupuestos competitivos para compras de software?

* **Doc ID:** `OP-002`
* **Nombre de Archivo:** `operations_mantenimiento_correctivo.txt`
* **Tipo:** Ficticio (Interno)
* **Descripción:** Protocolo y tiempos de respuesta para acciones correctivas en aerogeneradores e infraestructuras de la red de distribución.
* **Pregunta de Prueba:** ¿Cuál es el tiempo límite establecido para iniciar el mantenimiento correctivo ante una avería crítica en un aerogenerador?

### 4. Environmental, Social & Governance (esg)
* **Doc ID:** `ESG-001`
* **Nombre de Archivo:** `IB_Informe_Sostenibilidad.pdf`
* **Tipo:** Real (Basado en reporte público del sector)
* **Descripción:** Reporte de emisiones de carbono de alcance 1, 2 y 3, e iniciativas de diversidad y reforestación corporativa.
* **Pregunta de Prueba:** ¿Qué reducción de emisiones de alcance 1 se proyecta para el próximo año?

### 5. Legal (legal)
* **Doc ID:** `LE-001`
* **Nombre de Archivo:** `Reglamento 2016-679.pdf`
* **Tipo:** Real (Reglamento General de Protección de Datos - RGPD)
* **Descripción:** Manual normativo sobre el tratamiento de datos de clientes y la libre circulación de estos datos.
* **Pregunta de Prueba:** ¿Cuál es el plazo máximo para notificar una brecha de seguridad de datos según el GDPR?

### 6. Technical (technical)
* **Doc ID:** `TE-001`
* **Nombre de Archivo:** `Guia_Profesional_Tramitacion_autoconsumo_v.6.pdf`
* **Tipo:** Real (Guía del IDAE)
* **Descripción:** Guía profesional que describe los pasos técnicos y administrativos para la tramitación de instalaciones de autoconsumo eléctrico en España.
* **Pregunta de Prueba:** ¿Qué documentación técnica es necesaria para registrar una instalación de autoconsumo colectivo sin excedentes?

### 7. Financial (financial)
* **Doc ID:** `FI-001`
* **Nombre de Archivo:** `financial_presupuesto_anual_2026.txt`
* **Tipo:** Ficticio (Interno)
* **Descripción:** Asignación presupuestaria detallada para las divisiones de I+D y operaciones de parques eólicos de EcoPower para el año fiscal 2026.
* **Pregunta de Prueba:** ¿Qué porcentaje del presupuesto anual de 2026 está asignado a la investigación de nuevas tecnologías fotovoltaicas?

---

## ❓ Banco de Preguntas para Evaluación (Golden Dataset)
Estas preguntas se utilizarán en la **Fase 5** para evaluar de forma cuantitativa la precisión del sistema RAG (comparando la respuesta generada por el LLM contra el documento origen exacto):

| ID Pregunta | Categoría | Pregunta de Evaluación | Documento de Referencia |
| :--- | :---: | :--- | :--- |
| `Q-HR-01` | hr | ¿Cuál es el horario de disponibilidad obligatorio durante el teletrabajo? | `HR-001` |
| `Q-SE-01` | security | ¿Qué debe hacer un técnico inmediatamente si hay una incidencia eléctrica en un panel? | `SE-001` |
| `Q-OP-01` | operations | ¿Qué directiva de ciberseguridad debe validar el departamento legal en contratos de proveedores? | `OP-001` |
| `Q-OP-02` | operations | ¿Cuál es el tiempo límite establecido para iniciar el mantenimiento correctivo ante una avería crítica? | `OP-002` |
| `Q-LE-01` | legal | ¿Quién es el responsable de revisar las cláusulas de confidencialidad en las compras? | `OP-001` |
| `Q-FI-01` | financial | ¿Cuál es la asignación total del presupuesto para el mantenimiento preventivo en 2026? | `FI-001` |
| `Q-TE-01` | technical | ¿Cuáles son los requisitos de registro para autoconsumos colectivos? | `TE-001` |