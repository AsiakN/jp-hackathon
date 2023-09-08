from prompts.momo_charge_prompt import TARRIF_CHARGE,TRANSACTION_CHARGES,TRANSACTION_CHARGES_X
from google.cloud import aiplatform
import requests 
import vertexai
from typing import Optional

from vertexai.language_models import TextGenerationModel

class OpenAIFraudDetection:

    def __init__(self) -> None:
        #OPENAI CONFIGS
        self.url = 'https://api.openai.com/v1/chat/completions'

        # self.api_key = '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'
        self.api_key = ''
        self.temperature = 0

        self.headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {self.api_key}'
        }

        self.model_name = "gpt-3.5-turbo-16k"

        self.prompt = TRANSACTION_CHARGES_X

    def make_api_call(self, transaction_details: dict):
        data = self.build_request(transaction=transaction_details)

        response = requests.post(self.url, json=data, headers=self.headers)
        if response.status_code == 200:
            # Parse and print the response
            result = response.json()
            print(result)
            return result
        else:
        # If the request was not successful, print the error message
            print(f"Error: {response.status_code}\n{response.text}")

    def build_request(self, transaction:dict):

        data = {
        "model": f"{self.model_name}",
        "temperature": self.temperature,
        "messages": [
            {
                "role": "system",
                "content": f"You're a helpful transaction detector. {self.prompt}"
            },
            {
                "role": "user",
                "content": f"{transaction}"
            }
        ]
    }
        return data

class PalmFraudDetection():
    def __init__(self) -> None:
        self.palm_key = ''
        self.model = TextGenerationModel.from_pretrained("text-bison@001")
        self.parameters = {
            "candidate_count": 1,
            "max_output_tokens": 512,
            "temperature": 0.2,
            "top_p": 0.95,
            "top_k": 40
        }
   
        vertexai.init(project="eighth-network-397610", location="us-central1")
    
    def get_palm_response(self):
        response = self.model.predict(
            TARRIF_CHARGE,
            **self.parameters
        )

        return response
