from SPARQLWrapper import SPARQLWrapper, JSON

def sparql_query(title, query, repo_id="iot_repo"):
    print("\n" + "="*80)
    print(f"🔍 {title}")
    print("="*80)

    endpoint = f"http://localhost:7200/repositories/{repo_id}"
    
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    
    for result in results["results"]["bindings"]:
        print(result)

# CONSULTA 1: Obtener 5 observaciones

query_all = """
PREFIX sosa: <http://www.w3.org/ns/sosa/>

SELECT ?obs ?time ?value
WHERE {
    ?obs a sosa:Observation ;
         sosa:resultTime ?time ;
         sosa:hasResult ?r .
    ?r sosa:hasSimpleResult ?value .
}
LIMIT 5
"""

sparql_query("Consulta 1: Cinco observaciones del dataset", query_all)


# CONSULTA 2: Humedad mínima
query_min_humidity = """
PREFIX : <http://example.org/iot/> 
PREFIX sosa: <http://www.w3.org/ns/sosa/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT (MIN(xsd:float(?value)) AS ?minHumidity)
WHERE {
    ?obs sosa:observedProperty :Humidity ;
         sosa:hasResult ?r .
    ?r sosa:hasSimpleResult ?value .
}
"""

sparql_query("Consulta 2: Humedad mínima registrada", query_min_humidity)

# CONSULTA 3: Temperatura promedio

query_avg_temp = """
PREFIX : <http://example.org/iot/>
PREFIX sosa: <http://www.w3.org/ns/sosa/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT (AVG(xsd:float(?value)) AS ?avgTemp)
WHERE {
    ?obs sosa:observedProperty :Temperature ;
         sosa:hasResult ?r .
    ?r sosa:hasSimpleResult ?value .
}
"""

sparql_query("Consulta 3: Temperatura promedio semanal", query_avg_temp)


# CONSULTA 4: Temperatura máxima
query_max_temp = """
PREFIX : <http://example.org/iot/>
PREFIX sosa: <http://www.w3.org/ns/sosa/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT (MAX(xsd:float(?value)) AS ?maxTemp)
WHERE {
    ?obs sosa:observedProperty :Temperature ;
         sosa:hasResult ?r .
    ?r sosa:hasSimpleResult ?value .
}
"""

sparql_query("Consulta 4: Temperatura máxima registrada", query_max_temp)



# CONSULTA 5: Observaciones por rango de fechas
query_date_range = """
PREFIX : <http://example.org/iot/>
PREFIX sosa: <http://www.w3.org/ns/sosa/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?obs ?time ?value
WHERE {
    ?obs a sosa:Observation ;
         sosa:resultTime ?time ;
         sosa:hasResult ?r .
    ?r sosa:hasSimpleResult ?value .

    FILTER (
        ?time >= "2025-10-02T00:00:00"^^xsd:dateTime &&
        ?time <= "2025-10-03T00:00:00"^^xsd:dateTime
    )
}
ORDER BY ?time
LIMIT 20
"""

sparql_query("Consulta 5: Observaciones del 2 al 3 de octubre del 2025", query_date_range)
