def send_email(massage, recipient, sender = "university.help@gmail.com"):
    if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
send_email('message', 'university.help@gmail.com', '@.com')
send_email('message', 'university.help@gmail.com')
send_email('message', 'universi@.com')
send_email('message', 'universi@.co')
send_email('message', 'universi.com')
