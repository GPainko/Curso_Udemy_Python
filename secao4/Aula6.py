import calendar

numero_primeiro_dia, ultimo_dia  = calendar.monthrange(2024,2)
print(calendar.day_name[numero_primeiro_dia])
print(calendar.day_name[calendar.weekday(2024,2,ultimo_dia)])

for week in calendar.monthcalendar(2024,2):
    for day in week:
        if day == 0:
            continue
        print(day)