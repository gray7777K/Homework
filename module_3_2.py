def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if "@" not in recipient or not recipient.endswith((".com",".ru", ".net")) or "@" not in sender or not sender.endswith((".com",".ru", ".net")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
send_email("Ура, товарищи!", 'arbuzgmail.com')
send_email("Ура, товарищи!", 'university.help@gmail.com')
send_email("Ура, товарищи!", 'arbuz@gmail.com')
send_email("Ура, товарищи!", 'arbuz@gmail.com', sender = 'sliva@yandex.ru')
send_email("Ура, товарищи!", 'sliva@yandex.ru', sender = 'sliva@yandex.ru')
send_email("Ура, товарищи!", 'arbuz@gmail.com', sender = 'persik@co.uk')
send_email("Ура, товарищи!", 'arbuz@gmail.com', sender = 'slivayandex.ru')
