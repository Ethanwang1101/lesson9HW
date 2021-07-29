print('歡迎使用此系統')
i = 0
x = 0
y = 0
shop = {'A001小熊軟糖':'20元'
        ,'A002冰棒':'25元'
        ,'A004王子麵':'10元'
        ,'A006汽水':'30元'}
while i < 1:

    num = str(input('現在要做什麼?'))
    print('1,要查貨')
    print('2,要離開')
    
    if num =='1':
        print(shop)
        for k,v in shop.items():
            print(k,v)
        
        s = str(input('請輸入貨號?'))
        if s == 'A001':
            print(shop['A001小熊軟糖'])
        elif s == 'A002':
            print(shop['A002冰棒'])
        elif s == 'A004':
            print(shop['A004王子麵'])
        elif s == 'A006':
            print(shop['A006汽水'])
        else:
            print('yes or no')
            z = str(input('確定要輸入新商品?'))
            if z == 'yes':
                x = str(input('新商品的貨號和商品名字?'))
                y = str(input('商品價格?'))
                shop[x] = y
            elif z == 'no':
                print('ok')
    elif num =='2':
        print('yes or no')
        a = str(input('確定退出'))
        if a == 'yes':
            print('感謝使用此系統')
            i = i + 1
        elif a == 'no':
            print('ok')