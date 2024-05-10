import pandas as pd

order_items = pd.read_csv('S_Data\order_items.csv')
print(order_items.head())
order_items['prod_demand'] = order_items['product_id'].map(order_items['product_id'].value_counts())

print(order_items.sort_values('product_id').head())
