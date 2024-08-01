import requests
import pyinputplus as pyip
from requests import Response,ConnectionError,Timeout,TooManyRedirects,HTTPError
from pprint import pprint
def connect() -> Response | str:
    url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'

    try:
        response:Response = requests.get(url)
        response.raise_for_status()

    except ConnectionError:
        return "連線錯誤"
    except TooManyRedirects:
        return "過多轉址"
    except Timeout:
        return "網站無回應"
    except HTTPError:
        return "404"
    except:
        return "不明錯誤"

    else:
        return response
def search(response:Response,answer:str) -> list[dict]:
    data:list[dict] = response.text
    gdp = [gdpPercap for gdpPercap in data if gdpPercap['country'] == answer]
    return gdp
def get_country(response:Response) ->list[str]:
    data:list[dict] = response.text
    countrys:set = set()
    for site in data:
        countrys.add(site['country'])
    return list(countrys)

def main():
    response:Response | str = connect()
    if not isinstance(response,Response):
        print(response)
        return
    
    countrys = get_country(response)
    answer = pyip.inputMenu(countrys,"請輸入國家:\n",numbered= True)
    gdp = search(response,answer)

    if gdp:
        pprint(gdp)
    else:
        print(f"沒有找到 {answer} 該國家資訊。請再重新執行一次")


if __name__ == '__main__':
    main()