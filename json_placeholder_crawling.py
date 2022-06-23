import requests

main_url = "https://jsonplaceholder.typicode.com/posts/{id}"

for id in range(1, 11):
    url = main_url.format(id=id)
    res = requests.get(url).json()




    print(res)

