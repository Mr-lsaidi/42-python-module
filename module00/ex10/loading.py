import sys
import time


def convert_from_ms(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    seconds = seconds + milliseconds/1000

    result = ""
    if days != 0:
        result += str(days)+"d"
    if hours != 0:
        result += " "+str(hours)+"h"
    if minutes != 0:
        result += " "+str(minutes)+"m"
    if seconds != 0:
        result += " "+str(round(seconds, 2))+"s"
    return result


def ft_progress(range):
    size = 60
    count = len(range)
    total_estimation = 0
    for i in range:
        total_estimation += (i + 3) % 5

    def show(j, estimation):
        x = int(size*j/count)
        progres = int((j * 100 / count))
        es = convert_from_ms(estimation)
        print("ETA: {} [ {}%] [{}>{}] {}/{} elapsed time {}"
              .format(convert_from_ms(total_estimation), progres, u"="*x,
                      " "*(size-x), j, count, es), end='\r',
              file=sys.stdout, flush=True)

    curr_estimation = 0
    for i in range:
        yield i
        curr_estimation += (i + 3) % 5
        time.sleep(0.01)
        show(i + 1, curr_estimation)
    print("", flush=True, file=sys.stdout)


