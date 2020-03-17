import time
class Data:
    def __init__(self, zeit):
        self.zeit = zeit

    @classmethod
    def a_1(cls, zeit):
        zeit = zeit.split("-")[::-1]
        zeit[0] = int(zeit[0])
        zeit[1] = int(zeit[1])
        zeit[2] = int(zeit[2])
        Data.a_stat(zeit)
        print("day", zeit[2])
        print("month", zeit[1])
        print("year", zeit[0])
        s = [0, 0, 0, 0, 0, 0]
        zeit = tuple(zeit + s)
        print(f" дата преобразованная в число {time.mktime(zeit)} вот тип даты теперь: {type(time.mktime(zeit))} ")

    @staticmethod
    def a_stat(param):
        if param[0] >= 1970 and param[1] <= 12 and param[2] <= 31:
             return param
        else:
             print(param, "параметры не верны - выхожу")
             exit()



Data.a_1("31-12-1971")
daz = Data("10-12-1971")
daz.a_1("10-12-1977")
daz1 = Data("10-12-2018")
daz1.a_1("10-12-2018")