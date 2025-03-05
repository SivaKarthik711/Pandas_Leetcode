import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
   not_order_customer = customers[~customers['id'].isin(orders['customerId'])]
   return not_order_customer[['name']].rename(columns={'name':'Customers'})