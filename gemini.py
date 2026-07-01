from google import genai

client = genai.Client(api_key="AQ.Ab8RN6K6VoDLcZPRLCq8fOkU7GAyLo2GGIgS6ICV5WqrkEY-kw")  

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me a fun fact about RC fighter jets"
)
print(response.text)