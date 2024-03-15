class Generate:
    def __init__(self):
        self.openai = self.OpenAI()

    class OpenAI:
        def chat(self, **kwargs):
            response_format = kwargs.get("response_format", None).dict()
            if response_format:
                # Ensure response_format is a dictionary
                assert isinstance(
                    response_format, dict
                ), "response_format must be a dictionary"
                # Now you can use response_format in your method
                # For example, you can print it:
                print(response_format)
