import pickle
from pathlib import Path
import time

from scrapper import moscow_kamin_scr, flammen_gmbh_scr, schmid_scr, schiedel_scr, belfortkamin_scr, \
    lit_kom_scr, ecokamin_scr, kamin_sklad_scr, easysteam_scr, prometall_scr, pkferrum_scr
from tg_master import send_message


def main():
    file_path = Path('dict_stock.pickle')
    if file_path.exists():
        with open('dict_stock.pickle', 'rb') as file:
            dict_stock = pickle.load(file)
    else:
        dict_stock = {}

    moscow_kamin_list, flammen_gmbh_list, schmid_list = moscow_kamin_scr(), flammen_gmbh_scr(), schmid_scr()
    schiedel_list, belfortkamin_list = schiedel_scr(), belfortkamin_scr()
    lit_kom_list, ecokamin_list, kamin_sklad_list = lit_kom_scr(), ecokamin_scr(), kamin_sklad_scr()
    easysteam_list, prometall_list, pkferrum_list = easysteam_scr(), prometall_scr(), pkferrum_scr()

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


if __name__ == "__main__":
    main()
    time.sleep(86400)

