import requests
from pydantic import BaseModel

import json


class Generate:
    def __init__(self, api_url, headers):
        self.api_url = api_url
        self.headers = headers
        self.openai = self.OpenAI(api_url, headers)

    class OpenAI:
        def __init__(self, api_url, headers):
            self.api_url = f"{api_url}/generate/"
            self.headers = headers

        def _construct_request_format(self, model, context, response_format):
            # Default payload structure
            payload = {
                "model": {"provider": "gpt", "model": model},
                "context": context,
                "messages": [{"role": "user", "content": ""}],
            }

            # If response_format is provided and is a Pydantic model, add it to the payload
            if response_format is not None:
                if not isinstance(response_format, BaseModel):
                    raise ValueError("response_format must be a Pydantic model")
                json_schema = response_format.model_json_schema()
                payload["response_format"] = json_schema

            return payload

        def chat(self, **kwargs):
            model = kwargs.get("model", None)
            response_format = kwargs.get("response_format", None)
            context = kwargs.get("context", None)

            payload = self._construct_request_format(model, context, response_format)

            response = requests.post(
                self.api_url, headers=self.headers, data=json.dumps(payload)
            )

            if response.status_code == 200:
                return response.json()  # Or handle the response as needed
            else:
                raise Exception(
                    f"Failed to send request: {response.status_code} - {response.text}"
                )
