import os

# Definir los documentos simulados de EcoPower
documentos_ficticios = {
    "politica_teletrabajo_ecopower.txt": {
        "categoria": "hr",
        "contenido": """EcoPower Solutions S.L. - Política Interna de Teletrabajo.
        Puestos compatibles podrán realizar hasta dos días de teletrabajo por semana.
        Se requiere aprobación previa del responsable directo. El horario de disponibilidad obligatorio
        es de 09:00 a 14:00 y de 15:00 a 18:00. Los empleados deben conectarse mediante la VPN corporativa
        y garantizar la seguridad de la información confidencial según los estándares de la compañía."""
    },
    "manual_seguridad_plantas_solares.txt": {
        "categoria": "security",
        "contenido": """EcoPower Solutions S.L. - Manual de Prevención de Riesgos en Plantas Solares.
        Ante una incidencia eléctrica en un inversor o paneles fotovoltaicos, el técnico debe:
        1. Detener inmediatamente la intervención.
        2. Asegurar la zona delimitando el perímetro.
        3. Utilizar de forma obligatoria los Equipos de Protección Individual (EPI): guantes dieléctricos, calzado de seguridad clase E y casco.
        4. Comunicar la incidencia al responsable de mantenimiento y registrar el evento en el sistema operativo."""
    },
    "procedimiento_compras_proveedores.txt": {
        "categoria": "operations",
        "contenido": """EcoPower Solutions S.L. - Procedimiento de Contratación y Compras.
        Cualquier contratación de proveedores tecnológicos que superen los 15.000 euros anuales requerirá
        la presentación de al menos tres presupuestos competitivos. El departamento legal debe revisar y validar
        las cláusulas de confidencialidad y cumplimiento de la normativa NIS2 antes de firmar el contrato definitivo."""
    }
}

# Crear carpeta local temporal si no existe para revisar los archivos
os.makedirs("data_samples", exist_ok=True)

for nombre_archivo, info in documentos_ficticios.items():
    ruta = os.path.join("data_samples", nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(info["contenido"])
    print(f"Documento creado: {ruta} (Categoría: {info['categoria']})")