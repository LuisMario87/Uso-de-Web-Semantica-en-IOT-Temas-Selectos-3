import csv
from datetime import datetime, timedelta
import random

def simulate_classroom_data():
    # Parámetros de simulación
    start_date = datetime(2025, 10, 1, 0, 0, 0)   # puedes ajustar la fecha de inicio
    end_date = start_date + timedelta(days=7)
    interval = timedelta(minutes=10)
    
    data = []
    
    current_time = start_date
    while current_time < end_date:
        
        # Temperatura simulada (°C)
        # Más caliente al mediodía, más fresco en la madrugada
        base_temp = 22  
        
        # Variación por hora
        hour_variation = (current_time.hour - 12) ** 2
        temp = base_temp + random.uniform(-2, 2) - (hour_variation * 0.05)

        # Entre 18 y 29°C en condiciones normales
        temp = max(18, min(temp, 29))
        
        # Humedad simulada (%)
        humidity = random.uniform(40, 65)
        
        data.append({
            "timestamp": current_time.isoformat(),
            "temperature": round(temp, 2),
            "humidity": round(humidity, 2)
        })
        
        current_time += interval
        
    return data

def save_to_csv(data, filename="sensor_week_data.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature", "humidity"])
        
        for entry in data:
            writer.writerow([entry["timestamp"], entry["temperature"], entry["humidity"]])

# Ejecutar simulación
dataset = simulate_classroom_data()
save_to_csv(dataset)

print(f"Dataset generado con {len(dataset)} mediciones.")
print("Ejemplo de los primeros 5 registros:")
for row in dataset[:5]:
    print(row)
