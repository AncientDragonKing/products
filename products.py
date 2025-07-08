products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': # quit
		break
	price = input("請輸入商品價格:")
	products.append([name, price]) # products[0][0] = products清單中第一個 index 中的第一個 index
print(products)
for p in products:
	print(p[0], "的價格是", p[1])
with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')