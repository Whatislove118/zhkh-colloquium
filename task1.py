date1 = list(map(int, "2024-03-15".split("-")))
date2 = list(map(int, "2019-12-31".split("-")))

DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_BEFORE_MONTH = [-1]

# считаем кол-во дней с начала года до месяца
dbm = 0
for dim in DAYS_IN_MONTH[1:]:
    DAYS_BEFORE_MONTH.append(dbm)
    dbm += dim
del dbm, dim

def is_leap(year):
    return year % 4 == 0

def days_before_year(year):
    # Считаем кол-во дней до 1 январяе предыдущего года  (с учетом викосных годов)
    y = year - 1
    return y * 365 + y // 4

def days_in_month(year, month):
    if month == 2 and is_leap(year):
        return 29 # Если февраль и год високосный
    return DAYS_IN_MONTH[month]

def days_before_month(year, month):
    return DAYS_BEFORE_MONTH[month] + (month > 2 and is_leap(year))

def get_days(year, month, day):
    # Берем за начальную точку 1 Января 0001 года
    return days_before_year(year) + days_before_month(year, month) + day

print(abs(get_days(*date2) - get_days(*date1)))