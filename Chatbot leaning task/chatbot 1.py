
qna = {
    "hi": "HEY",
    "what is your name": "My name is Chatbot",
    "how are you": "I am fine",
    "how old are you": "I AM VIRTUAL MACHINE",
}

while True:
    qs = input()

    if qs == "quit":
        break
    elif qs in qna:
        print(qna[qs])
    else:
        print("I don't have an answer for that question.")
