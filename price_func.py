

def retrieve_price(item):
    price = item.select('.bui-price-display__value')[0].get_text().split('\n')[1].split()[1]
    return int(price.replace(",", ""))