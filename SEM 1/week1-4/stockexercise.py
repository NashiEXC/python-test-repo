purchasedstockprice = float(input("price purchased"))
currentstockprice = float(input("stock price "))
stockamount = 2000
commissionbroker = 0.03
commissionsale = 0.02

print(f"current stock price {currentstockprice}\ntotal commission {purchasedstockprice * commissionbroker * stockamount + currentstockprice * commissionsale * stockamount}\nprofit {purchasedstockprice * (100+commissionbroker) * stockamount+currentstockprice*(100-commissionsale) * stockamount}")