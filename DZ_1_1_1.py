print("Приветствую тебя!\n Это программа перевода временных величин, для выхода жми 'q' ")
duration = ''

while duration !='q':
    duration = (input('Введите цифровое значение продолжительности времени в секундах: '))
    try:
        duration = int(duration)
    except ValueError:
        continue
    else:
        hours = duration // 3600
        user_secs = duration % 3600

        minutes = user_secs // 60
        user_secs = user_secs % 60
        secs = user_secs


        days = 0
        while hours >= 24:
            days += 1
            hours = hours - 24

        if not days:
            if hours:
                print(f"{hours:02} ч. - {minutes:02} мин. - {secs:02} сек.")
            else :
                if minutes:
                    print(f"{minutes:02} мин. - {secs:02} сек.")
                else:
                    if secs:
                        print(f"{secs:02} сек.")
        else:
            print((f"{days:02}  д. - {hours:02} ч. -{minutes:02} мин. - {secs:02} сек."))