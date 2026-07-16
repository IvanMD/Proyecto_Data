import pandas as pd

def load_and_clean_orders(file_path):
    """
    Loads the orders dataset, transforms date columns to datetime objects,
    and filters to keep only delivered orders.
    """
    print("1. Loading raw orders data...")
    orders = pd.read_csv(file_path)
    
    print("2. Cleaning dates and removing canceled orders...")
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
    
    # Keep ONLY orders that were delivered
    clean_orders = orders[orders['order_status'] == 'delivered']
    
    print(f"Done! We retained {clean_orders.shape[0]} actual delivered orders.")
    
    return clean_orders
