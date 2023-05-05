import pandas as pd

df = pd.read_csv("..\data\ordersList.csv",encoding="cp949",header = 0)
print(df.pivot_table(index="상품명",columns="거래처명", values="금액", \
    fill_value=0, margins=True, aggfunc="sum"))
