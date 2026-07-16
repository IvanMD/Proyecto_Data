import pandas as pd
from src.data_prep import load_and_clean_orders

def test_no_canceled_orders_in_cleaned_data():
    """
    Test that the load_and_clean_orders function successfully 
    removes all non-delivered orders.
    """
    # 1. Run our function
    # Note: Make sure the path to the CSV is correct relative to where you run the test
    df_clean = load_and_clean_orders("olist_orders_dataset.csv")
    
    # 2. Check the unique values in the 'order_status' column
    unique_statuses = df_clean['order_status'].unique()
    
    # 3. Assert (Force a check): The only status allowed is 'delivered'
    assert len(unique_statuses) == 1, "There is more than one status in the cleaned data!"
    assert unique_statuses[0] == 'delivered', "Found non-delivered orders in the cleaned dataset!"
    