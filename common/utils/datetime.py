import datetime
import time
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class DateTimeUtils:
    @classmethod
    def get_now_date(cls):
        return timezone.localtime()

    @classmethod
    def is_contain_today(cls, left_date, right_date):
        if left_date <= timezone.localtime() < right_date:
            return True
        else:
            return False

    @classmethod
    def print_date(cls, date, format="%Y-%m-%d"):
        if date is not None:
            return date.astimezone().strftime(format)
        return "-"

    @classmethod
    def print_now(cls, date_format):
        now = timezone.localtime()
        return now.strftime(date_format)

    @classmethod
    def get_exam_time(cls, minutes, date=None):
        if date is None:
            now = datetime.datetime.now()
            result = now + relativedelta(minutes=minutes) + relativedelta(seconds=20)
        else:
            result = date + relativedelta(minutes=minutes) + relativedelta(seconds=20)
        return result

    @classmethod
    def get_after_minutes(cls, minutes, date=None):
        if date is None:
            now = datetime.datetime.now()
            result = now + relativedelta(minutes=minutes)
        else:
            result = date + relativedelta(minutes=minutes)
        return result

    @classmethod
    def get_after_hours(cls, hours, date=None):
        if date is None:
            now = datetime.datetime.now()
            result = now + relativedelta(hours=hours)
        else:
            result = date + relativedelta(hours=hours)
        return timezone.make_aware(result)

    @classmethod
    def get_after_days(cls, days, date=None):
        if date is None:
            now = datetime.datetime.now()
            result = now + relativedelta(days=days)
        else:
            result = date + relativedelta(days=days)
        return timezone.make_aware(result)

    @classmethod
    def get_after_days_timezone(cls, days, timezone_date=None):
        if timezone_date is None:
            now = timezone.localtime()
            result = now + relativedelta(days=days)
        else:
            result = timezone_date + relativedelta(days=days)
        return result

    @classmethod
    def date_string_to_korea_datetime_type_start(cls, string, format="%Y-%m-%d"):
        standard = datetime.datetime.strptime(string, format)
        result = datetime.datetime.combine(standard.date(), standard.time().min)
        result = timezone.make_aware(result)
        return result

    @classmethod
    def date_string_to_korea_datetime_type_end(cls, string, format="%Y-%m-%d"):
        standard = datetime.datetime.strptime(string, format)
        result = datetime.datetime.combine(standard.date(), standard.time().max)
        result = timezone.make_aware(result)
        return result

    @classmethod
    def date_string_to_korea_datetime_type_next_day(cls, string, format="%Y-%m-%d"):
        result = datetime.datetime.strptime(string, format)
        result = result + datetime.timedelta(days=1)
        result = timezone.make_aware(result)
        return result

    @classmethod
    def datetime_string_to_korea_datetime(cls, string):
        result = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M")
        result = timezone.make_aware(result)
        return result

    @classmethod
    def datetime_string_to_korea_datetime_type_next_time(cls, string):
        result = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M")
        result = result + datetime.timedelta(hours=1)
        result = timezone.make_aware(result)
        return result

    @classmethod
    def datetime_to_korea_datetime(cls, date):
        if date is None:
            return date
        result = timezone.localtime(date)
        return result

    @classmethod
    def get_korean_weekday_string(cls, date_string):
        result = datetime.datetime.strptime(date_string, "%Y.%m.%d")
        result = timezone.make_aware(result)
        english = result.strftime("%A")
        return DateTimeUtils.translate_english_weekday_to_korean(english)

    @classmethod
    def translate_english_weekday_to_korean(cls, english):
        if english == "Monday":
            return "월"
        elif english == "Tuesday":
            return "화"
        elif english == "Wednesday":
            return "수"
        elif english == "Thursday":
            return "목"
        elif english == "Friday":
            return "금"
        elif english == "Saturday":
            return "토"
        elif english == "Sunday":
            return "일"
        else:
            return english

    @classmethod
    def get_timedelta_by_datetime(cls, start_string, end_string):
        try:
            start_date = datetime.datetime.strptime(start_string, "%Y-%m-%d %H:%M")
            end_date = datetime.datetime.strptime(end_string, "%Y-%m-%d %H:%M")
            delta = end_date - start_date
            result = delta.days * 24 + delta.seconds / 3600
            return int(result)
        except ValueError:
            return 0

    @classmethod
    def get_next_hour_datetime_string(cls, string):
        result = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M")
        result = result + datetime.timedelta(hours=1)
        return result.strftime("%Y-%m-%d %H:%M")

    @classmethod
    def is_active_datetime(cls, string, format="%Y-%m-%d %H:%M"):
        try:
            if string is None:
                return False
            datetime.datetime.strptime(string, format)
            return True
        except ValueError:
            return False

    @classmethod
    def is_active_date(cls, string, format="%Y-%m-%d"):
        try:
            if string is None:
                return False
            datetime.datetime.strptime(string, format)
            return True
        except ValueError:
            return False

    @classmethod
    def is_active_year_month(cls, string):
        try:
            datetime.datetime.strptime(string, "%Y-%m")
            return True
        except ValueError:
            return False

    @classmethod
    def left_date_string_is_future(cls, left_string, right_string):
        left = datetime.datetime.strptime(left_string, "%Y-%m-%d")
        right = datetime.datetime.strptime(right_string, "%Y-%m-%d")
        return left > right

    @classmethod
    def left_time_string_is_future(cls, left_string, right_string):
        left = datetime.datetime.strptime(left_string, "%Y-%m-%d %H:%M")
        right = datetime.datetime.strptime(right_string, "%Y-%m-%d %H:%M")
        return left > right

    @classmethod
    def get_active_start_datetime_string(cls, start_date):
        result = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        return result.strftime("%Y-%m-%d %H:%M")

    @classmethod
    def get_active_end_datetime_string(cls, end_date):
        result = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        result = result + datetime.timedelta(days=1)
        return result.strftime("%Y-%m-%d %H:%M")

    @classmethod
    def get_active_start_datetime_string_by_monthly_date(cls, start_date):
        result = datetime.datetime.strptime(start_date, "%Y-%m")
        return result.strftime("%Y-%m-%d %H:%M")

    @classmethod
    def get_active_end_datetime_string_by_monthly_date(cls, end_date):
        result = datetime.datetime.strptime(end_date, "%Y-%m")
        result = result + relativedelta(months=1)
        return result.strftime("%Y-%m-%d %H:%M")

    @classmethod
    def get_yesterday_datetime_string(cls, date_string):
        result = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        result = result - datetime.timedelta(days=1)
        return result.strftime("%Y-%m-%d")

    @classmethod
    def change_datetime_format(cls, date_string, format):
        result = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return result.strftime(format)

    @classmethod
    def get_from_today_after_day_string(cls, day_count):
        result = DateTimeUtils.get_from_today_after_day(day_count)
        return result.strftime("%Y-%m-%d")

    @classmethod
    def get_from_now_after_hours(cls, hour_count):
        now = datetime.datetime.now()
        result = now + relativedelta(hours=hour_count)
        return timezone.make_aware(result)

    @classmethod
    def get_from_today_after_day(cls, day_count):
        now = datetime.datetime.now()
        result = now + relativedelta(days=day_count)
        return timezone.make_aware(result)

    @classmethod
    def get_before_3days(cls):
        now = datetime.datetime.now()
        result = now - relativedelta(days=3)
        return timezone.make_aware(result)

    @classmethod
    def get_before_15days_date_string(cls, date_string):
        result = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        result = result - datetime.timedelta(days=15)
        return result.strftime("%Y-%m-%d")

    @classmethod
    def get_after_15days_date_string(cls, date_string):
        result = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        result = result + datetime.timedelta(days=15)
        return result.strftime("%Y-%m-%d")

    @classmethod
    def get_before_1_month_first_day_string(cls, date):
        result = datetime.datetime.strptime(date, "%Y-%m-%d")
        result = result - relativedelta(months=1)
        return result.strftime("%Y-%m-01")

    @classmethod
    def get_before_1_month_string(cls, date):
        result = datetime.datetime.strptime(date, "%Y-%m-%d")
        result = result - relativedelta(months=1)
        return result.strftime("%Y-%m")

    @classmethod
    def get_deposit_date_string(cls, used_date):
        if used_date is None:
            return "-"
        day = DateTimeUtils.print_date(used_date, "%d")
        if int(day) < 11:
            return DateTimeUtils.print_date(used_date, "%Y.%m") + ".10"
        else:
            return DateTimeUtils.get_month_last_date_string(used_date)

    @classmethod
    def get_month_last_date(cls, created_date=timezone.localtime()):
        result = created_date + relativedelta(months=1)
        first_day = result.strftime("%Y.%m") + ".01"
        last_day = datetime.datetime.strptime(
            first_day, "%Y.%m.%d"
        ) - datetime.timedelta(days=1)
        return last_day

    @classmethod
    def get_month_last_date_string(cls, created_date):
        return DateTimeUtils.get_month_last_date(created_date).strftime("%Y.%m.%d")

    @classmethod
    def date_by_adding_business_days(cls, from_date, add_days):
        if from_date is None:
            return None
        business_days_to_add = add_days
        current_date = from_date
        while business_days_to_add > 0:
            current_date += datetime.timedelta(days=1)
            weekday = current_date.weekday()
            if weekday >= 5:  # sunday = 6
                continue
            business_days_to_add -= 1
        result = DateTimeUtils.print_date(current_date)
        return DateTimeUtils.date_string_to_korea_datetime_type_start(result)

    @classmethod
    def get_next_lecture_date(cls, current_date, times, is_first=True):
        rtimes = dict(current_date=current_date, times=[])
        if not is_first:
            rtimes['current_date'] += datetime.timedelta(days=1)
        while True:
            is_matched = False
            for time in times:
                if time['lecture_week'][rtimes['current_date'].weekday()]:
                    is_matched = True
                    item = dict()
                    item['start_time'] = time['start_time']
                    item['end_time'] = time['end_time']
                    rtimes['times'].append(item)
            if is_matched == True:
                break
            else:
                rtimes['current_date'] += datetime.timedelta(days=1)
        return rtimes

    @classmethod
    def print_time_stamp(cls):
        timestamp = time.mktime(datetime.datetime.today().timetuple())
        return str(timestamp)

    @classmethod
    def calculate_diff_seconds(cls, start, end):
        date_diff = end - start
        return date_diff.seconds

    @classmethod
    def get_time_string_to_seconds(cls, time_str):
        """Get Seconds from time."""
        return sum(int(x) * 60 ** i for i, x in enumerate(reversed(str(time_str).split(':'))))
