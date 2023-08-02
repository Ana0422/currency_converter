import requests

url = "https://v6.exchangerate-api.com/v6/3e3b6bf5edfe13d9f21b3b3a/latest/USD"


response = requests.get(url)

# print(response)
data = response.json()
# print(data)

for x in data.keys():
    if x == 'conversion_rates':
        currency_data = data['conversion_rates']
        for d in currency_data.keys():
            if d == 'INR':
                # print('{} : {}'.format(d, currency_data[d]))
                inr = currency_data[d]
                break

user_input = int(input("Enter the Dollars : "))
k = user_input*inr
print("The dollar when converted in Indian Rupees will be equal to: {}".format(k))
