class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


m = Question('Raman', "True")
print(m.text)
print(m.answer)
