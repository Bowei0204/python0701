import requests
from requests import Response,ConnectionError,Timeout,TooManyRedirects,HTTPError
from pprint import pprint

def connect() -> Response | str:
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1000'

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

def main():
    response:Response | str = connect()
    if isinstance(response,Response):
        print("連線成功")

        data:list[dict] = response.json()
    
        district:str = input("請輸入新北市行政區: ")
        district += "區"

        district_stations = []
        for station in data:
            if station['sarea'] == district:
                district_stations.append(station)


        if district_stations:
            pprint(district_stations)
        else:
            print(f"沒有找到 {district} 行政區的站點資訊。請再重新執行一次")

    else:
        print(response)


if __name__ == '__main__':
    main()