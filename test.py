import pyupbit

access = "xeLxoW97x6uregZWv8v61CZdZh0IPO7pEFsQe0kG"          # 본인 값으로 변경
secret = "3UA2lXU4kWlGtFSRhacNR7cS7Cmb34oGHg6Cr1qL"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

krw = upbit.get_balance("KRW")
upbit.buy_market_order("KRW-XRP", krw*0.9995)
