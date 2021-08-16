import pandas as pd

from util.constant import CAPACITY_CHARGE, HOEP, DISTRIBUTION_CHARGE, TRANSMISSION_NETWORK_CHARGE, \
    TRANSMISSION_CONNECTION_CHARGE, POWER_FACTOR, ADJUSTMENT_FACTOR, \
    METERING_FACTOR, WHOLE_MARKET_SERVICE_CHARGE, CUSTOMER_CHARGE, TRANSFORMER_ALLOWANCE, \
    ADMIN_CHARGE, TAX, GA, PDF
from util.util import scrape_total_ga, get_month, get_year, find_sum, find_max, adjust_constant


class Statistics:
    """
    statistics information for last of finished month
    """

    def __init__(self, df: pd.DataFrame, start, end, pdf):
        self.month = get_month(df)[0]  # error handle
        self.year = get_year(df)[0] # error handle
        self.val_sum = find_sum(df)
        self.val_max = find_max(df).max()
        self.adjust_constant = adjust_constant(start, end)
        self.hoep = scrape_total_ga(self.year, self.month)
        self.pdf = pdf
        self.start = start
        self.end = end
    
    def __kWh_used(self):
        return self.val_sum.sum()
    
    def __adjusted_val_detail(self, factor=ADJUSTMENT_FACTOR):
        return self.val_sum * factor[str(self.year)][0]

    def __adjusted_val(self) -> float:
        return self.__adjusted_val_detail().sum() 
    

    def __adjusted_max(self, factor=METERING_FACTOR) -> float:
        return self.val_max * factor[str(self.year)][0] * adjust_constant(self.start, self.end)

    def __get_hoep_detail(self) -> float:
        return self.__adjusted_val_detail() * HOEP[self.year][self.month]

    def __get_hoep(self) -> float:
        return self.__get_hoep_detail().sum() 

    def __get_adj_kVA(self, factor=POWER_FACTOR):
        return self.__adjusted_max() / factor[self.year][self.month]

    def __get_dist_charge(self, dist_charge=DISTRIBUTION_CHARGE) -> float:
        return self.__get_adj_kVA() * dist_charge[str(self.year)][0] *  adjust_constant(self.start, self.end) 


    def __get_transformer_allowance_charge(self, transformer_allowance=TRANSFORMER_ALLOWANCE):
        return self.__get_adj_kVA() * transformer_allowance[str(self.year)][0]  

    def __get_net_charge(self, net_charge=TRANSMISSION_NETWORK_CHARGE):
        return self.__adjusted_max() * net_charge[str(self.year)][0] 

    def __get_conn_charge(self, conn_charge=TRANSMISSION_CONNECTION_CHARGE):
        return self.__adjusted_max()  * conn_charge[str(self.year)][0]   
    
    def __get_whole_market_charge_detail(self, market_charge=WHOLE_MARKET_SERVICE_CHARGE):
        return self.__adjusted_val_detail() * market_charge[str(self.year)][0]

    def __get_whole_market_charge(self) -> float:
        return self.__get_whole_market_charge_detail().sum() 
    
    def __get_capacity_recovery(self, capacity_charge=CAPACITY_CHARGE) -> float:
        return self.__adjusted_val() * capacity_charge[str(self.year)][0]

    def __get_global_adjustment(self):
        return scrape_total_ga(self.year, self.month) * self.pdf[self.year][self.month] * 1000000

    def __get_customer_charge(self, customer_charge=CUSTOMER_CHARGE) -> float:
        return customer_charge[str(self.year)][0] * adjust_constant(self.start, self.end) 
    
    def __get_admin_charge(self, admin_charge=ADMIN_CHARGE) -> float:
        return admin_charge[str(self.year)][0] * adjust_constant(self.start, self.end) 

    def bill(self) -> float:
        return self.__get_hoep() + self.__get_dist_charge() + \
               self.__get_net_charge() + self.__get_conn_charge() + self.__get_global_adjustment() + \
               self.__get_whole_market_charge() + self.__get_customer_charge() - \
               self.__get_transformer_allowance_charge() + self.__get_admin_charge() + \
               self.__get_capacity_recovery()


    def get_data(self) -> dict:

        """create dictionary of statistics \n
        sample:
            {'energy_charge': 0.01413,
            'ga': 185967.18600000002,
            'peak': 8.8283, 'demand': 191.76,
            'power_factor': 0.95,
            'transmission_charge': 4.4341}

        :return: dict or None
        """
        return {
            'kWh used': self.__kWh_used(),
            'adjusted kWh': self.__adjusted_val(),
            'energy_charge': self.__get_hoep(),
            'capacity recovery': self.__get_capacity_recovery(),
            'peak': self.val_max,
            'adjusted peak': self.__adjusted_max(),
            'adjusted kVA': self.__get_adj_kVA(),
            'connecting charge': self.__get_conn_charge(),
            'network charge': self.__get_net_charge(), 
            'wholesales charge': self.__get_whole_market_charge(),
            'dist_charge' : self.__get_dist_charge(),
            'transformer allowance': self.__get_transformer_allowance_charge(),
            'global adjustment': self.__get_global_adjustment(),
            'admin charge': self.__get_admin_charge(),
            'customer charge': self.__get_customer_charge(),
            'Total Bill': self.bill() * TAX
         
        }
    
    def get_total_bill(self) -> float:
        return self.bill() * TAX

    def get_final_bill(self) -> float:
        """
        it calculates simulated bill with enregy rebate
        :return: float or None
        """
        return self.get_total_bill() 