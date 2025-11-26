import csv

def csv_to_rdf_turtle(csv_file, ttl_file):
    prefixes = """
@prefix : <http://example.org/iot/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn: <http://www.w3.org/ns/ssn/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix qudt-unit: <http://qudt.org/vocab/unit/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:sensor1 a sosa:Sensor ;
    sosa:observes :Temperature, :Humidity .

:classroom1 a sosa:FeatureOfInterest ;
    sosa:hasProperty :Temperature, :Humidity .

"""

    obs_counter = 1
    ttl_content = prefixes

    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            timestamp = row["timestamp"]
            temperature = row["temperature"]
            humidity = row["humidity"]

            # ---------- TEMPERATURE OBSERVATION ----------
            obs_id = f"obs{obs_counter:04d}"
            result_id = f"result{obs_counter:04d}"
            
            ttl_content += f"""
:{obs_id} a sosa:Observation ;
    sosa:hasFeatureOfInterest :classroom1 ;
    sosa:observedProperty :Temperature ;
    sosa:madeBySensor :sensor1 ;
    sosa:resultTime "{timestamp}"^^xsd:dateTime ;
    sosa:hasResult :{result_id} .

:{result_id} a sosa:Result ;
    sosa:hasSimpleResult "{temperature}"^^xsd:float ;
    qudt:unit qudt-unit:DegreeCelsius .
"""
            obs_counter += 1

            # ---------- HUMIDITY OBSERVATION ----------
            obs_id = f"obs{obs_counter:04d}"
            result_id = f"result{obs_counter:04d}"
            
            ttl_content += f"""
:{obs_id} a sosa:Observation ;
    sosa:hasFeatureOfInterest :classroom1 ;
    sosa:observedProperty :Humidity ;
    sosa:madeBySensor :sensor1 ;
    sosa:resultTime "{timestamp}"^^xsd:dateTime ;
    sosa:hasResult :{result_id} .

:{result_id} a sosa:Result ;
    sosa:hasSimpleResult "{humidity}"^^xsd:float ;
    qudt:unit qudt-unit:Percent .
"""
            obs_counter += 1

    with open(ttl_file, "w", encoding="utf-8") as out:
        out.write(ttl_content)

    print(f"Archivo Turtle generado: {ttl_file}")
    print(f"Total de observaciones RDF: {obs_counter - 1}")


# Ejecutar conversión
csv_to_rdf_turtle("sensor_week_data.csv", "sensor_data.ttl")
