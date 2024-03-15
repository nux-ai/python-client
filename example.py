from nuxai import NUX
from pydantic import BaseModel

nux = NUX("sk-2ent6rDGgbJkjvnKhP91oMvC1r8EwOwltwBOdSEpScGdVlMMe67-s2jFHVKTzJ512lg")


class ResponseFormat(BaseModel):
    city: str
    neighborhood: str
    weather: float


text = nux.parse(
    ["https://nux-sandbox.s3.us-east-2.amazonaws.com/marketing/ethan-resume.pdf"]
)

output = nux.generate.openai.chat(
    model="gpt-3.5-turbo",
    response_format=ResponseFormat,
    context=f"Given this context, answer X. | context",
)

print(output)
