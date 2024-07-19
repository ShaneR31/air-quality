import requests
import pandas as pd
import config  # Import the configuration file

api_key = config.API_KEY  # Access the API key from the config file
url = "https://api.purpleair.com/v1/sensors"

headers = {
    "X-API-Key": api_key
}

# Define the parameters for your API request
params = {
    "fields": "sensor_index,name,latitude,longitude,pm2.5_cf_1"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

# Extract relevant data
sensors = data.get("data", [])

# Convert to DataFrame
df = pd.DataFrame(sensors, columns=["sensor_index", "name", "latitude", "longitude", "pm2.5_cf_1"])

# Save to CSV
df.to_csv("purpleair_data.csv", index=False)