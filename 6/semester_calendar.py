"""Function that returns calendar in html or txt type"""
import calendar

def get_semester_calendar(output_type, year, first_month, last_month):
    """
    HW
    >>> get_semester_calendar("html", 2024, 10, 10)
    '<table border="0" cellpadding="0" cellspacing="0" class="month">\\n<tr><th \
colspan="7" class="month">October 2024</th></tr>\\n<tr><th class="mon">Mon</th><th \
class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th \
class="sat">Sat</th><th class="sun">Sun</th></tr>\\n<tr><td class="noday">&nbsp;</td><td \
class="tue">1</td><td class="wed">2</td><td class="thu">3</td><td class="fri">4</td><td \
class="sat">5</td><td class="sun">6</td></tr>\\n<tr><td class="mon">7</td><td \
class="tue">8</td><td class="wed">9</td><td class="thu">10</td><td class="fri"\
>11</td><td class="sat">12</td><td \
class="sun">13</td></tr>\\n<tr><td class="mon">14</td><td \
class="tue">15</td><td class="wed">16</td><td \
class="thu">17</td><td class="fri">18</td><td class="sat">19</td><td \
class="sun">20</td></tr>\\n<tr><td \
class="mon">21</td><td class="tue">22</td><td class="wed">23</td><td class="thu">24</td><td \
class="fri">25</td><td class="sat">26</td><td \
class="sun">27</td></tr>\\n<tr><td class="mon">28</td><td \
class="tue">29</td><td class="wed">30</td><td class="thu">31</td><td class="noday">&nbsp;</td><td \
class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\\n</table>\\n'
    
    >>> get_semester_calendar("txt", 2024, 8, 9)
    '    August 2024\\nMo Tu We Th Fr Sa Su\\n\
          1  2  3  4\\n 5  6  7  8  9 10 11\\n12 \
13 14 15 16 17 18\\n19 20 21 22 23 24 25\\n26 27 \
28 29 30 31\\n   September 2024\\nMo Tu We Th Fr Sa Su\\n                   \
1\\n 2  3  4  5  6  7  8\\n 9 10 11 12 13 14 15\\n16 17 \
18 19 20 21 22\\n23 24 25 26 27 28 29\\n30\\n'
    
    """
    if not output_type in ("txt", "html")\
    or not (1 <= first_month <= 12)\
    or not (1 <= last_month <= 12)\
    or first_month > last_month:
        return None

    calendar_string = []

    for i in range(first_month, last_month+1):
        if output_type == "txt":
            cal = calendar.TextCalendar()
            calendar_string.append(cal.formatmonth(year, i))
        else:
            cal = calendar.HTMLCalendar()
            calendar_string.append(cal.formatmonth(year, i))

    calendar_string = "".join(calendar_string)
    return calendar_string

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
