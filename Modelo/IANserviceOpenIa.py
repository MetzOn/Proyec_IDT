from openai import OpenAI
from decouple import config
import openai
import json

class OpenIaInspector:
    
    def __init__(self,dataframe):
        self.dataframe=dataframe
        self.API_KEY=config('SECRET_KEY')
        
    def get_gpt_response(self):
        client = OpenAI(api_key=self.API_KEY)
        try:
            response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role":"system", 
                    "content":"""
                        Se te proprocionará una lista cuyos valores será diccionarios de python, aquí encontrás información
                        como: (id del empleado), (nombre del empleado), (apellido del empleado), (dni  del empleado), (cantidad de asistencias) y (procentaje de asistencias).
                        En base a esta información quiero que realices una apreciación y resumen de la data proporcionada. Esto representa data de una semana de trabajo de 5 días de lunes a viernes
                        También quiero que realices un resumen de cómo va todo y qué cosas se podrían mejorar, si algunos empleados baja del 80% quiero tambien realices una apreciación de ellos 
                    """
                },
                {
                    "role":"user",
                    "content":json.dumps(self.dataframe)
                }
            ]
            )
            return response.choices[0].message.content
        except openai.OpenAIError  as e:
            #Handle API error here, e.g. retry or log
            print(f"OpenAI API returned an API Error: {e}")
            return None
         