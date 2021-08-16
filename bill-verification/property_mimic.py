import datetime
import pandas as pd

from datetime import timedelta


class FakeManager:
    @staticmethod
    def get(id):
        return Property()


class Property:
    objects = FakeManager()

    def __init__(self):
        self.df = pd.read_csv('bill-verification/property.csv', parse_dates=['time'])
        self.df = self.df.set_index(['time'], drop=True)

    def get_data(self, start, end):
        return self.df[start:end].resample('H', label = 'right', closed = 'right').mean()

    def get_clean_data(self, start, end):
        ''' clean the selected interval from zeros by replacing the last week values in data set.
            :param date: desired start date and the last date
            :return: clean data set 
        '''
        pd.options.mode.chained_assignment = None
        for ind, val in self.df[start:end].iterrows():
             self.df[start:end].loc[ind]= val.apply(lambda val : self.df.loc[ind+timedelta(weeks=-2)][0] if val == 0 else val)
                                                                
        return self.get_data(start, end)

    


  