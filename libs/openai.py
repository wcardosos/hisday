from openai import OpenAI


client = OpenAI()

def fetch_historical_event(date: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um professor acadêmico de história com doutorado"},
            {
                "role": "user",
                "content": f"Me dê um evento histórico que tenha acontecido na data de {date}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "historical_event",
                "schema": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "description": "Data do evento histórico",
                            "type": "string"
                        },
                        "event": {
                            "description": "Informações do evento histórico",
                            "type": "string"
                        }
                    }
                }
            }
        }
    )

    return completion.choices[0].message.content