from datetime import datetime
from util.constant import PDF

from logic import get_statistics, get_total, get_diff
from property_mimic import Property

sample_start_date = datetime(2019, 11, 1)
sample_end_date = datetime(2019, 12, 1)      


if __name__ == '__main__':
    print(get_diff(Property.objects.get(id=17), sample_start_date, sample_end_date, pdf=PDF))