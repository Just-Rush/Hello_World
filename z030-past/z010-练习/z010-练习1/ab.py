def send_messages(show_messages,sent_messages):
    for message in show_messages:
        sent_messages.append(message)
        show_messages.remove(message)
    print(show_messages)
    print(sent_messages)

def send_messages3(show_messages,sent_messages):
    show_m_copy = show_messages[:]
    while show_m_copy:
        sent_message = show_m_copy.pop(0)
        sent_messages.append(sent_message)
        print(sent_message)
    print(sent_messages)
    print(show_messages)