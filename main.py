from db_config.populate_db import populate
from product_category.process_data import data_for_clustering, tokenize
from timeseries.forecast import predict_sales
from product_category.recommandation_system import recommend


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # populate()
    # tokenize()
    # print(predict_sales())
    print(recommend())

