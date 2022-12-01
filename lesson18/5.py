from time import time, localtime
class Clock:
    @staticmethod
    def say_time():
        timeP = localtime(time())
        print(f"{timeP.tm_hour} : {timeP.tm_min} : {timeP.tm_sec}")
Clock.say_time()