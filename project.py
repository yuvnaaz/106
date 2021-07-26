import numpy as np

def getDataSource(data_path):
    Coffee_in_ml = []
    sleep_in_hours = []
    with open(data_path, encoding = "utf-8") as csv_file:
         csv_reader = csv.DictReader(csv_file)
         for row in csv_reader:
             Coffee_in_ml.append(float(row['Coffee in ml']))
             sleep_in_hours.append(float(row['sleep in hours']))
    return{'x': ice_cream_sales, 'y': cold_drink_sales}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('correlation is ', correlation[0,1])
def setup():
    data_path = 'cups of coffee vs hours of sleep.csv'
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
setup()