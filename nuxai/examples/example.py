from nuxai import NUX
from pydantic import BaseModel

# init NUX client
nux = NUX("")


# define response format
class UserSchema(BaseModel):
    name: str
    age: int
    email: str


# extract text
text = nux.parse(file_urls=["https://nux-ai.s3.amazonaws.com/parse/parse_text.txt"])

# generate response using extracted text and response format
response = nux.generate(response_format=UserSchema, context=text, prompt="blah")
