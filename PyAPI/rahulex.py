import requests
import json

# response = requests.get("http://216.10.245.166/Library/GetBook.php",params={'AuthorName':'Rahul Shetty2'},)
# json_res = response.json()
# # print(json_res)
# for book in json_res:
#     if book['isbn'] == 'bnid3473':
#         print(book)
#         break
#
# expt = {'book_name': 'Devops', 'isbn': 'bnid3473', 'aisle': '7538'}
#
# assert book == expt

# response = requests.get('https://fakestoreapi.com/products')
# print(response.json())
# print(response.status_code)

# with open('da.json', 'r') as f:
#     data = json.load(f)
#
# response = requests.post('https://fakestoreapi.com/products', json=data)
# print(response.json())
# print(response.status_code)

# response = requests.get('https://fakestoreapi.com/products/1')
# print(response.json())
# print(response.status_code)

# product = {'title': 'Updated Product', 'price': 39.99}
# response = requests.put('https://fakestoreapi.com/products/1', json=product)
# print(response.json())
# print(response.status_code)

response = requests.delete('https://fakestoreapi.com/products/1')
print(response.json())
print(response.status_code)