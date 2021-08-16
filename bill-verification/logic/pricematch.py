import pandas as pd

from util.constant import CAPACITY_CHARGE, HOEP, DISTRIBUTION_CHARGE, TRANSMISSION_NETWORK_CHARGE, \
    TRANSMISSION_CONNECTION_CHARGE, POWER_FACTOR, ADJUSTMENT_FACTOR, \
    METERING_FACTOR, WHOLE_MARKET_SERVICE_CHARGE, CUSTOMER_CHARGE, TRANSFORMER_ALLOWANCE, \
    ADMIN_CHARGE, TAX, GA, PDF

from logic.energy import Statistics
from util.scanned_file import scanned_file

class PriceMatch:
    '''
    validate the details of electricity bill based on OEB approved rates.
    '''

    def __init__(self, df: pd.DataFrame, start, end, pdf, percent): 
        self.bill_ins = Statistics(df, start, end, pdf)
        self.scanned_file = scanned_file()
        self.original_file = self.bill_ins.get_data()
        self.percent = percent
        

    def telorance(self, original_file) -> float:
        return self.percent * original_file
    
    def price_difference(self, original_file, scanned_file):
        return scanned_file - original_file
    
    def bill_ver(self):
            not_match = set()
            for item in self.scanned_file:
                original_file = self.original_file[item]
                scanned_file = self.scanned_file[item]

                if scanned_file >= original_file + self.telorance(original_file):
                    not_match.add(item)
                    print(f"{item} is not valid and the difference is {self.price_difference(original_file, scanned_file)}")

                else:
                    print(f"{item} is valid")
            
            return (f"not valid items : {not_match}")