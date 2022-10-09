import time
import random
import re

class ChatBotNoob:
    def send_message(self, message):
        print(message)
        time.sleep(1)
        print("Yes! I can hear you.. you said:  {}".format(message))


class ChatBot1:
    def __init__(self, name, weather):
        self.name = name
        self.weather = weather

    def send_message(self, message):
        responses = {"What's your name?": ["My name is {0}".format(self.name),
                                           "They call me {0}".format(self.name),
                                           "I go by {0}".format(self.name)],
                     "What's today's weather?": ["the weather is {0}".format(self.weather),
                                                 "it's {0} today".format(self.weather)],
                     "default": ["default message"]}

        if message in responses:
            return random.choice(responses[message])
        else:
            return random.choice(responses["default"])


chat_bot1 = ChatBot1("Sam", "Rainy")
bot_message1 = chat_bot1.send_message("What's your name?")
print(bot_message1)


class ChatBot2:
    def __init__(self, name, weather):
        self.name = name
        self.weather = weather

    def send_message(self, message):
        responses = {'question': ["I don't know :(", 'you tell me!'],
                     'statement': ['tell me more!',
                                   'why do you think that?',
                                   'how long have you felt this way?',
                                   'I find that extremely interesting',
                                   'can you back that up?',
                                   'oh wow!',
                                   ':)']}

        if message.endswith("?"):
            return random.choice(responses["question"])
        else:
            return random.choice(responses["statement"])


chat_bot2 = ChatBot2("Sam", "rainy")
bot_message2 = chat_bot2.send_message("Did you know that we already visited moon?")
print(bot_message2)


class ChatBot3:
    def __init__(self):
        print("Hey this is Sam..")

    def send_message(self, message):
        rules = {'I want (.*)': ['What would it mean if you got {0}',
                                 'Why do you want {0}',
                                 "What's stopping you from getting {0}"],
                 'do you remember (.*)': ['Did you think I would forget {0}',
                                          "Why haven't you been able to forget {0}",
                                          'What about {0}',
                                          'Yes .. and?'],
                 'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
                 'if (.*)': ["Do you really think it's likely that {0}",
                             'Do you wish that {0}',
                             'What do you think about {0}',
                             'Really--if {0}']}

        for pattern, responses in rules.items():
            match = re.search(pattern,message)
            if match is not None:
                response = random.choice(responses)
                if '{}' in response:
                    phrase = match.group(1)
        return response, phrase

    def replace_pronouns(self, message):

        message = message.lower()
        if 'me' in message:
            # Replace 'me' with 'you'
            return re.sub('me', 'you', message)
        if 'my' in message:
            # Replace 'my' with 'your'
            return re.sub('my', 'your', message)
        if 'your' in message:
            # Replace 'your' with 'my'
            return re.sub('your', 'my', message)
        if 'you' in message:
            # Replace 'you' with 'me'
            return re.sub('you', 'me', message)

        return message

    def respond(self, message):
        response, phrase = ChatBot3.send_message(rules, message)
        if '{0}' in response:
            # Replace the pronouns in the phrase
            phrase = ChatBot3.replace_pronouns(phrase)
            # Include the phrase in the response
            response = ChatBot3.response.format(phrase)
        return response
