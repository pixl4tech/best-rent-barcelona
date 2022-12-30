from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import config
import statistics


# Python program to get average of a list
def average(lst):
    if len(lst) == 0:
        return None
    return sum(lst) / len(lst)


def median(lst):
    if len(lst) == 0:
        return None
    return statistics.median(lst)


def minimal(lst):
    if len(lst) == 0:
        return None
    return min(lst)


def maximal(lst):
    if len(lst) == 0:
        return None
    return max(lst)


idealista_districts = config.IDEALISTA_DISTRICT_URI_MAPPING
idealista_flats = config.IDEALISTA_FLAT_TYPES

browser = webdriver.Chrome("/Users/pixl4tech/Downloads/chromedriver")

avg_prices_by_district = {}
for flat_type in idealista_flats:
    avg_prices_by_district[flat_type] = {}
    for district_path in idealista_districts:
        price_list = []
        max_iter = 300
        count = 0
        for i in range(1, max_iter+1):
            browser.get(
                f'https://www.idealista.com/en/alquiler-viviendas/{idealista_districts.get(district_path)}/con-pisos,'
                f'{idealista_flats.get(flat_type)}/pagina-{i}.htm')
            time.sleep(1)
            if i == 1:
                count_elems = browser.find_elements(By.CLASS_NAME, 'breadcrumb-navigation-element-info')
                counts = []
                for e in count_elems:
                    counts.append(int(e.text.split("with")[0].replace(" ", "").replace(",", "")))
                if len(counts) > 0:
                    count = counts[len(counts)-1]
                else:
                    count = 0
            if count > 0:
                elems = browser.find_elements(By.CLASS_NAME, 'item-price')
                for e in elems:
                    price_list.append(int(e.text.replace("€/month", "").replace(",", "")))
                _max_iter = count // 30
                if _max_iter < 1:
                    max_iter = 1
                elif _max_iter < max_iter:
                    max_iter = _max_iter
                if i == max_iter:
                    break
            else:
                break

        avg_prices_by_district[flat_type][district_path] = \
            dict(avg=average(price_list), max=maximal(price_list), median=median(price_list), min=minimal(price_list), prices=price_list)

print(avg_prices_by_district)


