def day_counter(hours):
    return hours//24

def add_time(start:str, duration:str, day=""):
    days_of_the_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    start_hour, start_minute = start.split(":")
    start_minute, noon = start_minute.split(" ")
    duration_hour, duration_minute= duration.split(":")
    fun_noon = noon
    before_after = {
        "am": 0,
        "pm": 1,
    }
    noon = before_after.get(noon.lower())
    extra_hour = (int(start_minute)+int(duration_minute))//60
    end_minutes = (int(start_minute)+int(duration_minute))%60
    end_hour = int(duration_hour)+int(start_hour)+extra_hour
    noon += end_hour//12
    noon = noon%2
    end_hour = (int(duration_hour)+int(start_hour)+extra_hour)%12  # hours
    extra_hour = extra_hour%60  # minutes
    if noon == 0:
        noon = "AM"
    else:
        noon = "PM"
    if fun_noon.lower() == 'pm':
        afternoon_addon = 12
    else:
        afternoon_addon = 0
    days_passed = day_counter( int(duration_hour)+int(start_hour)+extra_hour+afternoon_addon)
    if end_hour == 0:
        end_hour = 12
    end_minutes = str(end_minutes)
    if len(end_minutes) == 1:
        end_minutes = '0'+end_minutes
    num_day_week = days_passed
    days_passed = str(days_passed)
    if days_passed  == "0":
        days_passed = ''
    elif days_passed == '1':
        days_passed = '(next day)'
    else:
        days_passed = f"({days_passed} days later)"
    num_day_week = num_day_week%7
    if day!='':
            start_day = days_of_the_week.index(day.lower())
            end_day = (num_day_week + start_day) % 7
            end_day = days_of_the_week[end_day]
            if days_passed == '':
                return f"{end_hour}:{end_minutes} {noon}, {end_day.capitalize()}"
            return f"{end_hour}:{end_minutes} {noon}, {end_day.capitalize()} {days_passed}"
    elif days_passed == '':
        return f"{end_hour}:{end_minutes} {noon}"
    return f"{end_hour}:{end_minutes} {noon} { days_passed}"


