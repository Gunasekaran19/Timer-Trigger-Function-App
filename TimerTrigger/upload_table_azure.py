import uuid
import random
from azure.data.tables import TableClient
from azure.core.exceptions import ResourceExistsError

def upload_weather_data(weather_data):
    connection_string = 'use_your_connection_string'

# Create a TableClient
    table_client = TableClient.from_connection_string(connection_string, "wheatherdata")
    
    # Define the entity properties
    partition_key = str(uuid.uuid4())
    row_key = str(random.randint(1, 100000))
    weather = f"{weather_data['weather'][0]['description']}"
    temperature =f"{weather_data['main']['temp']}°C"
    humidity = f"{weather_data['main']['humidity']}%"
    speed =f"{weather_data['wind']['speed']} m/s"
    
    # Create the entity
    entity = {
        "PartitionKey": partition_key,
        "RowKey": row_key,
        "Weather": weather,
        "Temperature": temperature,
        "Humidity": humidity,
        "Speed": speed,
    }
    
    try:
        # Insert the entity into the table
        table_client.create_entity(entity)
        print("Entity successfully uploaded to Azure Storage Table.")
    except ResourceExistsError:
        print("Entity with the same PartitionKey and RowKey already exists in the table.")
    except Exception as e:
        print(f"Error uploading entity to Azure Storage Table: {e}")
    