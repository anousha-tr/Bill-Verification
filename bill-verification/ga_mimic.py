import datetime

gas = {
    datetime.date(2020, 1, 1): 1107.8,
    datetime.date(2020, 2, 1): 1136.5,
    datetime.date(2020, 3, 1): 1168.4,
    datetime.date(2020, 4, 1): 1282.7,
    datetime.date(2020, 5, 1): 1293.6,
    datetime.date(2020, 6, 1): 1282.2,
    datetime.date(2020, 7, 1): 1217.7,
    datetime.date(2019, 1, 1): 956.2,
    datetime.date(2019, 2, 1): 908.1,
    datetime.date(2019, 3, 1): 857.6,
    datetime.date(2019, 4, 1): 1118.7,
    datetime.date(2019, 5, 1): 1133.3,
    datetime.date(2019, 6, 1): 1261.3,
    datetime.date(2019, 7, 1): 1149.6,
    datetime.date(2019, 8, 1): 1327.7,
    datetime.date(2019, 9, 1): 1082.9,
    datetime.date(2019, 10, 1): 1209.6,
    datetime.date(2019, 11, 1): 979.0,
    datetime.date(2019, 12, 1): 1000.2,
    datetime.date(2020, 8, 1): 1115.5
}


class FakeManager:
    @staticmethod
    def get(date):
        return GA(date, gas[date])


class GA:
    objects = FakeManager()

    def __init__(self, date, val):
        self.date = date
        self.ga_value = val

