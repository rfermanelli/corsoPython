class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    def next_second(self):
        self.__seconds += self.__seconds
    def previous_second(self):
        self.__seconds -= self.__seconds
    def get_time(self):
        hh = str(self.__hours)
        mm = str(self.__minutes)
        ss = str(self.__seconds)
        return ':'.join([hh, mm, ss])

def format_time(hours, minutes, seconds):
    pass


hh = int(input('hour (format 00:23): '))
mm = int(input('minute (format 00:59): '))
ss = int(input('second (format 00:59): '))

timer_object = Timer(hh, mm, ss)

timer_object.next_second()
timer_object.next_second()
print(timer_object.get_time())






