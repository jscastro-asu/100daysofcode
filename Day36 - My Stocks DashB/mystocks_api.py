import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT","datatype":"json","output_size":"compact"}

headers = {
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
	"X-RapidAPI-Key": "106bbad07emsh277341f7d7b0eaep14dfddjsn00a333346b73"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)