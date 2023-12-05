import pickle
from pathlib import Path
import datetime
import time

from scrapper import moscow_kamin_scr, flammen_gmbh_scr, schmid_scr, schiedel_scr, belfortkamin_scr, \
    lit_kom_scr, ecokamin_scr, kamin_sklad_scr, easysteam_scr, prometall_scr, pkferrum_scr
from tg_master import send_message, error_message, check_message


def main():
    file_path = Path('dict_stock.pickle')
    if file_path.exists():
        with open('dict_stock.pickle', 'rb') as file:
            dict_stock = pickle.load(file)
    else:
        dict_stock = {}


    try:
        moscow_kamin_list = moscow_kamin_scr()
    except Exception as e:
        error_message('moscow_kamin', e)
    try:
        flammen_gmbh_list = flammen_gmbh_scr()
    except Exception as e:
        error_message('flammen_gmbh', e)
    try:
        schmid_list = schmid_scr()
    except Exception as e:
        error_message('schmid', e)
    try:
        schiedel_list = schiedel_scr()
    except Exception as e:
        error_message('schiedel', e)
    try:
        belfortkamin_list = belfortkamin_scr()
    except Exception as e:
        error_message('belfortkamin', e)
    try:
        lit_kom_list = lit_kom_scr()
    except Exception as e:
        error_message('lit_kom', e)
    try:
        ecokamin_list = ecokamin_scr()
    except Exception as e:
        error_message('ecokamin', e)
    try:
        kamin_sklad_list = kamin_sklad_scr()
    except Exception as e:
        error_message('kamin_sklad', e)
    try:
        easysteam_list = easysteam_scr()
    except Exception as e:
        error_message('easysteam', e)
    try:
        prometall_list = prometall_scr()
    except Exception as e:
        error_message('prometall', e)
    try:
        pkferrum_list = pkferrum_scr()
    except Exception as e:
        error_message('epkferrum', e)


    dict_stock_current = {
        'flammen-gmbh.ru': flammen_gmbh_list, 'schmid.ru': schmid_list, 'moscow.kamin.ru': moscow_kamin_list,
        'schiedel.com.ru': schiedel_list, 'belfortkamin.ru': belfortkamin_list, 'lit_kom_list': lit_kom_list,
        'www.ecokamin.ru': ecokamin_list, 'kamin-sklad.ru': kamin_sklad_list, 'easysteam.ru': easysteam_list,
        'prometall.ru': prometall_list, 'pkferrum.ru': pkferrum_list
    }

    with open('dict_stock.pickle', 'wb') as file:
        pickle.dump(dict_stock_current, file)

    for key in dict_stock_current:
        event_list = dict_stock_current[key]
        for event in event_list:
            if key in dict_stock:
                if event not in dict_stock[key]:
                    send_message(key, event)
                    time.sleep(5)
            else:
                send_message(key, event)
                time.sleep(5)


def wait_until_morning():
    current_time = datetime.datetime.now()
    target_time = datetime.datetime(current_time.year, current_time.month, current_time.day, 9, 0, 0)

    while current_time < target_time:
        current_time = datetime.datetime.now()
        time.sleep(30)


if __name__ == "__main__":
    while True:
        main()
        wait_until_morning()
