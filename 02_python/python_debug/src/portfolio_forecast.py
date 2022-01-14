import numpy as np

def load_hpi(hpi_file):
    hpi_dict = {}
    with open(hpi_file,'r') as f_hpi:
        f_hpi.readline()
        for line in f_hpi:
            str_tok = line.split(sep=',')
            zipcode = np.int(str_tok[0].strip() or 0)
            period = np.int(str_tok[1].strip() or 0)
            hpi_index = np.float64(str_tok[2].strip() or 0)
            if zipcode not in hpi_dict:
                hpi_dict[zipcode] = {}
            hpi_dict[zipcode][period] = hpi_index
    return hpi_dict
"""
A program to compute a weighted sum of forecasted price of a property portfolio in 5 years time
"""
if __name__ == '__main__':
    hpi_file = '../metadata/hpi.csv'
    portfolio_file = '../metadata/rmbs_portfolio.csv'
    hpi_dict = load_hpi(hpi_file)
    forecast_time = 60
    current_total = 0
    forecasted_total = 0
    with open(portfolio_file,'r') as f_portfolio:
        f_portfolio.readline()
        for line in f_portfolio:
            str_tok = line.split(sep=',')
            current_price = np.int(str_tok[0].strip() or 0)
            zipcode = np.int(str_tok[1].strip() or 0)
            own_pct = np.float64(str_tok[2].strip() or 0)
            current_total = current_total + (current_price * own_pct / 100)
            forecasted_price = current_price * hpi_dict[zipcode][60] / hpi_dict[zipcode][0]
            forecasted_total = forecasted_total + (forecasted_price * own_pct / 100)
    print('Current value of portfolio: ' + str(round(current_total,2)))
    print('Forecasted value of portfolio: ' + str(round(forecasted_total,3)))
    print('Growth of portfolio: ' + str(round(forecasted_total/current_total,2)))



