Proyecto IoT con Web Semántica usando SSN/SOSA y GraphDB

Este proyecto implementa un sistema IoT semántico basado en sensores simulados, utilizando tecnologías de la Web Semántica como RDF, la ontología SSN/SOSA y consultas SPARQL ejecutadas desde Python hacia un triplestore GraphDB.

El objetivo es demostrar cómo la representación semántica de datos IoT permite mejorar la interoperabilidad, el análisis avanzado y la integración entre dispositivos y sistemas inteligentes.

Descripción del Proyecto

Este proyecto simula un entorno IoT en un salón de clases mediante dos sensores:

Sensor de temperatura

Sensor de humedad

Los datos se generan cada 10 minutos durante una semana completa, resultando en más de 2000 observaciones.

Posteriormente:

Los datos se convierten a RDF utilizando la ontología SOSA/SSN.

Se cargan en un triplestore GraphDB desde Python.

Se ejecutan consultas SPARQL para analizar tendencias, máximos, mínimos y rangos temporales.

🔧 Tecnologías Utilizadas
Lenguaje

Python 3.10+

Librerías

pandas

rdflib

SPARQLWrapper

Web Semántica

RDF (Resource Description Framework)

Ontología SOSA/SSN (W3C)

SPARQL (para consultas semánticas)

Infraestructura

GraphDB Free Edition

Flujo del Proyecto
1. Simulación de datos (IoT)

El script genera un dataset realista de temperatura y humedad.

Archivo:
src/simulacion/SimulacionDeDatos.py

Salida:
data/sensor_week_data.csv

2. Conversión a RDF usando SSN/SOSA

El archivo CSV se transforma a triples RDF en formato Turtle.

Archivo:
src/rdf/datasetARDF.py

Salida:
data/sensor_data.ttl

Ontología usada:
http://www.w3.org/ns/sosa/

3. Cargar datos en GraphDB

Los datos RDF se cargan vía HTTP desde Python.

Archivo:
src/graphdb/repositorioGraphDB.py

Config inicial (opcional):
src/rdf/repo-config.ttl

4. Consultas SPARQL desde Python

Se ejecutan consultas avanzadas sobre el repositorio:

5 observaciones

Humedad mínima

Temperatura promedio

Temperatura máxima

Rangos temporales

Archivo:
src/graphdb/consultasSPARQLGRAPHDB.py

Resultados Destacados

Temperatura máxima: 23.95 °C

Temperatura promedio semanal: 20.03 °C

Humedad mínima: 40.02 %

El análisis por intervalos permitió observar tendencias y estabilidad en el ambiente.

Cómo Ejecutar el Proyecto
1. Instalar dependencias
pip install -r requirements.txt

2. Iniciar GraphDB

Ejecuta GraphDB localmente

Accede a: http://localhost:7200

Crea un repositorio llamado: iot_repo

3. Generar dataset IoT
python src/simulacion/SimulacionDeDatos.py

4. Convertir el dataset a RDF
python src/rdf/datasetARDF.py

5. Cargar el archivo RDF en GraphDB
python src/graphdb/repositorioGraphDB.py

6. Ejecutar consultas SPARQL
python src/graphdb/consultasSPARQLGRAPHDB.py


Los resultados se imprimirán en la terminal con encabezados claros para distinguir cada consulta.

Consultas SPARQL Incluidas

Obtener 5 observaciones
Temperatura máxima
Temperatura promedio
Humedad mínima
Observaciones por intervalo de fechas


Conclusión

El proyecto demuestra que la Web Semántica y las ontologías como SSN/SOSA permiten:

Estandarizar datos IoT

Realizar consultas avanzadas

Integrar información heterogénea

Analizar tendencias ambientales de manera precisa

La combinación GraphDB + RDF + Python resulta poderosa para construir sistemas IoT semánticamente enriquecidos.

Referencias

W3C SSN/SOSA Ontology — https://www.w3.org/TR/vocab-ssn/

SPARQL 1.1 Query Language — https://www.w3.org/TR/sparql11-query/

RDF 1.1 Concepts — https://www.w3.org/TR/rdf11-concepts/

GraphDB Documentation — https://graphdb.ontotext.com/
