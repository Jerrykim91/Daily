# 2019.12.17 <ver_1>
# **<문제>**   
# 커피값을 입력받아서 1500원이상이면 거스럼돈을 줘라     
# 내용은 "거스름돈(받은금액-1500)은 XX원 입니다."

# base ------------------------------
coffee_price =int(input('커피값을 주세요'))
if coffee_price >= 1500 :
    tmp = '잔돈은 %d원 입니다.'% (coffee_price - 1500)
    print(tmp)
    pass

# ----------------------------------

# 2019.12.18 <ver_2>
# base 튜닝-------------------------
coffee_price = int(input('커피값을 주세요'))
if coffee_price > 1500 :
    tmp = '잔돈은 %d원 입니다.'% (coffee_price - 1500)
    print(tmp)
elif coffee_price < 1500: 
    tmp = '금액이 부족합니다. %d원 더 주세요.'% (1500 - coffee_price)
    print(tmp)  
elif coffee_price == 1500:     
    tmp = '\n%d원 받았습니다.\n감사합니다.'% (coffee_price)
    print(tmp)
else :
    print('감사합니다.')
    pass
# ----------------------------------
coffee_price = int(input('커피값을 주세요'))
if coffee_price > 1500:
    print('잔돈은 %d원 입니다.'% (coffee_price - 1500))
elif coffee_price == 1500:
    print('\n%d원 받았습니다.\n감사합니다.'% (coffee_price))
else:
    print('감사합니다.')
# ----------------------------------
