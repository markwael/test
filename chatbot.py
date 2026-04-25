import random 
class chatbott:
    def __init__(self,responses):
        self.responses = responses
    # Function to get a response based on user input
    def get_respon(self,user_input):
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        
        return random.choice(self.responses["default"])
    # Chatbot function
    def chatbot(self):
        print("Chatbot: Hi! How can I assist you today?")
        
        while True:
            user_input = input("User: ").lower()
            response = chatbott.get_respon(self.user_input)
            
            print("Chatbot:", response)
            
            if user_input == "goodbye":
                break
# Predefined responses
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
    "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"]
}

chatbott()
