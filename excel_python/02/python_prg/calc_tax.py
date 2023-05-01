"""
calc_tax 함수는 상품 가격과 소비세율을 인수로 받아
소비세액을 돌려줌
"""
def calc_tax(price,rate):
    tax = price * rate / 100
    #int 함수를 써서 정숫값을 반환
    return int(tax)


a = calc_tax(1249,10)
print(a)
