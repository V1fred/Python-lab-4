from datetime import date

today = date.today()

print("Today: {}.{}.{}".format(today.day, today.month, today.year))

print("Day of the week: ", today.strftime ("%A"))

nextyear = date( today.year + 1, 1, 1 )
tonextyear = nextyear - today
print("Until next year: ", tonextyear.days - 1, "days")

