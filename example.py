from nuxai import NUX
from pydantic import BaseModel

nux = NUX("")


class ResponseFormat(BaseModel):
    city: str
    neighborhood: str
    weather: float


response_format = ResponseFormat(
    city="New York", neighborhood="Manhattan", weather=72.5
)

# text = nux.parse(file_urls=["https://www.weather.com/"])

output = nux.generate.openai.chat(
    model="gpt-3.5-turbo",
    response_format=response_format,
    context=f"Given this context, answer X. | context",
)


print(output)
