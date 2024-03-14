class Generate:
    def __init__(self):
        self.openai = self.OpenAI()

    class OpenAI:
        def chat(self, **kwargs):
            return self._send_post("/generate/openai/chat", kwargs)
