import pandas as pd 

asking_prices = pd.Series([15000, 22000, 18000, 30000, 25000])  
fair_prices = pd.Series([16000, 20000, 18500, 28000, 26000])    

good_deals = asking_prices < fair_prices
good_deal_indices = [i for i in range(len(good_deals)) if good_deals[i]==True]
                        #OR
# good_deal_indices = good_deals[good_deals].index.tolist()

print("Asking Prices:\n", asking_prices)
print("\nFair Prices:\n", fair_prices)
print("Indices of good deals:", good_deal_indices)