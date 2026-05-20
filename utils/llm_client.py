

    def get_response(self, prompt):
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ updated model
            messages=[
                {"role": "system", "content": "You are a helpful debugging assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
