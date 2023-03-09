import whatsapp_api

api = whatsapp_api.api

def login():
    api.login()


def open_chat(contact: str):
    api.search_contact(contact)
    api.click_contact(contact)


def send_message_to(contact: str, message: str):
    open_chat(contact)
    api.send_message(message)
    api.get_messages()


def main():
    login()
    open_chat("test")
    api.get_messages()


main()