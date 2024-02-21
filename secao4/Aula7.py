import calendar 
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print(locale.getlocale())

print(calendar.calendar(2024))
