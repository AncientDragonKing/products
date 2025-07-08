products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': # quit
		break
	products.append(name)
print(products)