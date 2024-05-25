import calendar

(SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY) = range(7)


def day_name(d): return calendar.day_name[(d + 6) % 7]
