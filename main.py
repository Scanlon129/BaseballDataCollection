# Imports----------------------------------------------------------------------
import os
# Local Dependencies-----------------------------------------------------------
from top_25_hitters_request import request_top_hitters
from skunkpack import datestrings
from skunkpack import logger

# Definitions------------------------------------------------------------------
data_path = '__data/Top_25_Hitters/'

# Functions--------------------------------------------------------------------
def save_to_csv(df):
    time_executed = f'{datestrings.todays_date}_{datestrings.right_now_24}'
    file_name = f'top25_hitters_week_to_date_{time_executed.replace(':','')}.csv'
    try:
        df.to_csv(data_path+file_name, index=False)
        logger.log.debug(f'{file_name} saved to data folder')
    except:
        logger.log.error(f'AN ERROR OCCURED WHEN LOGGING TOP 25 HITTERS')

def save_to_excel(df):
    time_executed = f'{datestrings.todays_date}_{datestrings.right_now_24}'
    file_name = f'top25_hitters_week_to_date_{time_executed.replace(':','')}.xlsx'
    try:
        df.to_excel(data_path+file_name, index=False)
        logger.log.debug(f'{file_name} saved to data folder')
    except:
        logger.log.error(f'AN ERROR OCCURED WHEN LOGGING TOP 25 HITTERS')
'''
#attempt at messing with pymysql via pandas
try:
    df.to_sql()
    logger.log.debug(f'{file_name} saved to data folder')
except:
    logger.log.error('AN ERROR OCCURED WHEN LOGGING TOP 25 HITTERS TODAY')
'''
# Main-------------------------------------------------------------------------
if __name__ == '__main__':
    df = request_top_hitters()
    save_to_excel(df)
