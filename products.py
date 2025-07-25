import os # operating system 作業系統模組
def read_file(filename):
	products = []
	with open(filename, "r", encoding = 'utf-8') as f:
		for line in f:
			if "商品, 價格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name, price])
	return products
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q': # quit
			break
		price = input("請輸入商品價格:")
		price = int(price) # int = interger 整數
		products.append([name, price]) # products[0][0] = products清單中第一個 index 中的第一個 index
	print(products)
	return products
def print_products(products):
	for p in products:
		print(p[0], "的價格是", p[1])
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: # 使用utf-8(最好用的，有支援全語言)來編碼
		f.write("商品, 價格\n") # 寫入和讀取時會出現編碼(encoding)問題
		for p in products:
			f.write(str(p[0]) + ',' + str(p[1]) + '\n')
# 但如果要用excel打開就會有錯誤，因為excel的編碼不是用utf-8，所以要去[ 資料 -> 取得外部資料 -> 從文字檔]
# c記得delimiter(分隔號)要使用comma
# add header 增加欄位名稱
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # path 路徑 isfile 檢查檔案在不在 
		print('讀取成功!')
		products = read_file(filename)
	else:
		print('讀取失敗, 檔案不存在...')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)
main()