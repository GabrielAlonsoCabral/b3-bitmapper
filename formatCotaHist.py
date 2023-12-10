import os
import time
from sys import exit

import pandas as pd
from dotenv import load_dotenv

from s3 import upload_to_s3

load_dotenv()


print("info: only .txt files are allowed.")
filename = input('filepath(without extension):')
file = open(filename + '.txt', 'r')
arq = file.readlines()
file.close()

def gerar_arquivo(option):
    print('\nWriting dataframe on the new format...')
    time3 = time.time()
    duration2 = round((time3 - time2), 2)
    filename_with_extension='_'+filename+'.csv'


    if option == str(0):
        df_global.to_csv('_' + filename + '.csv')
        bucket_name = os.getenv("AWS_BUCKET_NAME")
        s3_key = os.getenv("AWS_BUCKET_KEY")
        upload_to_s3(filename_with_extension,bucket_name,s3_key+filename_with_extension)
    if option == str(1):
        df_global.to_csv('_' + filename + '.csv')
    elif option == str(2):
        df_global.to_excel('_' + filename + '.xlsx')
    elif option == str(3):
        df_global.to_csv('_' + filename + '.csv')
        df_global.to_excel('_' + filename + '.xlsx')        
    else:
        print('\nClosing script!\n')
        exit()
    print('\nfile writed sucessfully!' + str(duration2) + ' seconds\n')



time1 = time.time()

print('\nLoading file...')
print('\nFormating file...!')

dic = {}

dic['REGISTER_TYPE'] = [int(arq[nlinha][24:26]) for nlinha in range(1, len(arq)-1)]
dic['MARKET_DATE'] = [(arq[nlinha][2:10]) for nlinha in range(1, len(arq)-1)]
dic['BDI_CODE'] = [(arq[nlinha][10:12]) for nlinha in range(1, len(arq)-1)]
dic['STOCKS_LETTER_CODE'] = [(arq[nlinha][12:24]).rstrip() for nlinha in range(1, len(arq)-1)]
dic['MARKET_TYPE'] = [int(arq[nlinha][24:27]) for nlinha in range(1, len(arq)-1)]
dic['COMPANY_NAME_RESUME'] = [(arq[nlinha][27:39]).rstrip() for nlinha in range(1, len(arq)-1)]
dic['STOCK_SPECIFICATION'] = [(arq[nlinha][39:49]).strip('-') for nlinha in range(1, len(arq)-1)]
dic['CURRENCY_REFERENCE'] = [(arq[nlinha][52:56]).rstrip() for nlinha in range(1, len(arq)-1)]
dic['OPENING_VALUE'] = [float(arq[nlinha][56:69])/100 for nlinha in range(1, len(arq)-1)]
dic['MAX_VALUE'] = [float(arq[nlinha][69:82])/100 for nlinha in range(1, len(arq)-1)]
dic['MIN_VALUE'] = [float(arq[nlinha][82:95])/100 for nlinha in range(1, len(arq)-1)]
dic['AVERAGE_VALUE'] = [float(arq[nlinha][95:108])/100 for nlinha in range(1, len(arq)-1)]
dic['LAST_OFFER_VALUE'] = [float(arq[nlinha][108:121])/100 for nlinha in range(1, len(arq)-1)]
dic['BEST_BUY_OFFER'] = [float(arq[nlinha][121:134])/100 for nlinha in range(1, len(arq)-1)]
dic['BEST_SALE_OFFER'] = [float(arq[nlinha][134:147])/100 for nlinha in range(1, len(arq)-1)]
dic['TRADES_COUNT'] = [int(arq[nlinha][147:152]) for nlinha in range(1, len(arq)-1)]
dic['STOCKS_TRADES_TOTAL_COUNT'] = [int(arq[nlinha][152:170]) for nlinha in range(1, len(arq)-1)]
dic['VOLUME'] = [float(arq[nlinha][170:188])/100 for nlinha in range(1, len(arq)-1)]
dic['STOCKS_FACTOR'] = [int(arq[nlinha][210:217]) for nlinha in range(1, len(arq)-1)]
dic['ISIN_CODE'] = [(arq[nlinha][230:242]) for nlinha in range(1, len(arq)-1)]
dic['STOCKS_SHARING_NUMBER'] = [int(arq[nlinha][242:245]) for nlinha in range(1, len(arq)-1)]

df_global = pd.DataFrame(dic)
df_global['MARKET_DATE'] = pd.to_datetime(df_global['MARKET_DATE'])
print(df_global)

time2 = time.time()
duration1 = round((time2 - time1), 2)
print('\nDataframe created sucessfully in ' + str(duration1) + ' seconds')

gerar_arquivo(input('\nUpload csv to bucket(0)\ncsv(1)\nxlsx(2)\ncsv and xlsx(3)\nexit(4)\n'))