import datetime

__id__ = 1
__author__ = "Alexei Molchalin"
__date__ = datetime.date(2018, 12, 20)
__name__ = "<Собери число>"

class Task:
    c = int(input())

    sum1 = c//100 + c%100//10
    sum2 = c%100//10 + c%10

    if (sum1 < sum2):
        print(str(sum1)+str(sum2))
    else:
        print(str(sum2)+str(sum1))