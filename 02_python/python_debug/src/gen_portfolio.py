import numpy
import random
import numpy as np

def load_hpi(hpi_file):
    hpi_dict = {}
    with open(hpi_file,'r') as f_hpi:
        f_hpi.readline()
        for line in f_hpi:
            str_tok = line.split(sep=',')
            zipcode = int(str_tok[0].strip() or 0)
            period = int(str_tok[1].strip() or 0)
            hpi_index = float(str_tok[2].strip() or 0)
            if zipcode not in hpi_dict:
                hpi_dict[zipcode] = {}
            hpi_dict[zipcode][period] = hpi_index
    return hpi_dict

"""
A program to sum the area of all the triangles in 10000_triangle_area_calc.csv
"""
if __name__ == '__main__':
    portfolio_file = '../metadata/rmbs_portfolio.csv'
    hpi_file = '../metadata/hpi.csv'
    portfolio_value = 0
    hpi_dict = load_hpi(hpi_file)
    zipcode_list = list(hpi_dict.keys())
    with open(portfolio_file,'w') as p_file:
        p_file.write('current_house_price,zipcode,ownership_pct\n')
        for i in range(1,10000):
            house_price = random.randint(100000,1000000)
            zipcode_index = random.randint(0, len(zipcode_list)-1)
            zipcode = zipcode_list[zipcode_index]
            ownership = round(np.random.uniform(0.1, 0.001),3)
            p_file.write(str(house_price)+','+str(zipcode)+','+str(ownership)+'\n')
            portfolio_value = portfolio_value + (house_price * ownership/100)

    print('Value of portfolio created: ' + str(portfolio_value))


