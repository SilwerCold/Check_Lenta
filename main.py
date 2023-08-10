import json
import requests
import time
from random import randrange


def get_data(start, end):
    cookies = {
        '.ASPXANONYMOUS': 'VSm-acQeMaDK9WmeuyUUyI3voWoTBYwV2Z-hn60Ed7s_nBAWUofdEjU-jRYfyyxmPTGEmAaejnQRFl3Z6-vz0FyCVvgoHzUW1kFksQD5SwcPzXx-rxAC_cPXFqyh1szLiM5_6Q2',
        'ASP.NET_SessionId': '5quw10c31yus1o3fgrvqfgrd',
        'CustomerId': '7264eb21f7bd48dbbf35e26390054751',
        'ShouldSetDeliveryOptions': 'True',
        'DontShowCookieNotification': 'true',
        'cookiesession1': '678B286A9914BDFHJLNPRTVXZCEFEE0D',
        '_ym_d': '1657614856',
        '_ym_uid': '1657614856390607995',
        '_tm_lt_sid': '1657614855327.995706',
        'KFP_DID': 'bc06afe8-c62b-ddec-b28f-9c0377f75dfb',
        'AddressTooltipInfo': 'Lenta.MainSite.Abstractions.Entities.Ecom.AddressTooltip',
        '_gcl_au': '1.1.1239530581.1659341664',
        '_ym_isad': '1',
        'tmr_lvid': 'c6200a8e43616efa5c0817f257e70e4f',
        'tmr_lvidTS': '1659341664137',
        '_ga': 'GA1.2.1838342026.1659341664',
        '_gid': 'GA1.2.678805602.1659341664',
        '_tt_enable_cookie': '1',
        '_ttp': '10354ee4-a7e5-4826-a8c6-5445ae3c8839',
        'flocktory-uuid': '765b22b4-9096-4a44-b9a2-defa216f23d9-8',
        'oxxfgh': 'c108cbf2-e4fc-4800-a201-9b0f4ce4ee10#2#5184000000#5000#1800000#44965',
        '.AspNet.ApplicationCookie': 'qhTUpr2T1jfOaqwfnRiRlevfxGps4rzca9XDLQzmi3BsvNyRAPMrrxJsf_mQXTwDweS6C4vgmloI15viJWIapUL0vso2TYwzlWXvRb2DbeYB0NFdMOj_OwMiUt3_hP72xJZRyYDa12YWoFsHux9rRU6M2Y5v0OfFXH_giHI5ixDGZuSaJriTqAuS06aqAiJGNdQdCCtrAVvIyLOwvZMmhxFmOg7pF2pX_JKRU7ppHxi8tmBuhwE4gdywvybis95MHWqeqxlrfA0-dad3g549eq7nfHIZ02t9RblUUIsh2Sxs13fhBrH27OIvzNwJ6rNDrK45a_M9ZtqiKH3I511ZHU6_puhoURNkDx0nj4HE5TaZpEzo5i5QHpK6uBjEo2TfJmaTVW3OGNcxCeokvX-3Am46pT9i9dnLdhXWLncuIO5BdAbO3gwI78BK2uF8fj9dRs7mZUDCXkgzuhfF6Z0TRf27J5XNS1JdoIYtM3mMxiKlXL_EFQotOfQzsp0jlV1zc1a5xTA9hMpTMsEqtdRQaWYob4KXWLIHSP7b8iWYQAJ0R08tzp5HfOKOENz6hxi90OCGnYzdZQaJ-CfIEys0CDIGEdCykbgS99jnoAdYWdDjdVEEuSHOAiyaQlLWXzn8_uWJpE0z6pU0bsJML7a24hR6WJtXhnRI7aGSy3FpBLUtPht9gCJOtrQQjEdhj4dT33d0f1DggTxl2pQnExJy9nQZg07fltJEWrKHbsGitLhkKRok4q8d6TGMT3Hlo9cKSgLpwER73sMapdJ4CkGdrNRJH3gT8fB__SvKaQ1yjl-PYECEFvom4yIOwlE5bDJx3b2oqJiNj3SnNC4dtyEBMIzmGDIiKao9nFAxGF0xQxe8uqg2WjgSSmDoMOGWFEZPrNlA2g',
        '_ym_visorc': 'b',
        '_dc_gtm_UA-327775-35': '1',
        '_gat_UA-327775-1': '1',
        'tmr_detect': '1%7C1659354352149',
        'tmr_reqNum': '57',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '.ASPXANONYMOUS=VSm-acQeMaDK9WmeuyUUyI3voWoTBYwV2Z-hn60Ed7s_nBAWUofdEjU-jRYfyyxmPTGEmAaejnQRFl3Z6-vz0FyCVvgoHzUW1kFksQD5SwcPzXx-rxAC_cPXFqyh1szLiM5_6Q2; ASP.NET_SessionId=5quw10c31yus1o3fgrvqfgrd; CustomerId=7264eb21f7bd48dbbf35e26390054751; ShouldSetDeliveryOptions=True; DontShowCookieNotification=true; cookiesession1=678B286A9914BDFHJLNPRTVXZCEFEE0D; _ym_d=1657614856; _ym_uid=1657614856390607995; _tm_lt_sid=1657614855327.995706; KFP_DID=bc06afe8-c62b-ddec-b28f-9c0377f75dfb; AddressTooltipInfo=Lenta.MainSite.Abstractions.Entities.Ecom.AddressTooltip; _gcl_au=1.1.1239530581.1659341664; _ym_isad=1; tmr_lvid=c6200a8e43616efa5c0817f257e70e4f; tmr_lvidTS=1659341664137; _ga=GA1.2.1838342026.1659341664; _gid=GA1.2.678805602.1659341664; _tt_enable_cookie=1; _ttp=10354ee4-a7e5-4826-a8c6-5445ae3c8839; flocktory-uuid=765b22b4-9096-4a44-b9a2-defa216f23d9-8; oxxfgh=c108cbf2-e4fc-4800-a201-9b0f4ce4ee10#2#5184000000#5000#1800000#44965; .AspNet.ApplicationCookie=qhTUpr2T1jfOaqwfnRiRlevfxGps4rzca9XDLQzmi3BsvNyRAPMrrxJsf_mQXTwDweS6C4vgmloI15viJWIapUL0vso2TYwzlWXvRb2DbeYB0NFdMOj_OwMiUt3_hP72xJZRyYDa12YWoFsHux9rRU6M2Y5v0OfFXH_giHI5ixDGZuSaJriTqAuS06aqAiJGNdQdCCtrAVvIyLOwvZMmhxFmOg7pF2pX_JKRU7ppHxi8tmBuhwE4gdywvybis95MHWqeqxlrfA0-dad3g549eq7nfHIZ02t9RblUUIsh2Sxs13fhBrH27OIvzNwJ6rNDrK45a_M9ZtqiKH3I511ZHU6_puhoURNkDx0nj4HE5TaZpEzo5i5QHpK6uBjEo2TfJmaTVW3OGNcxCeokvX-3Am46pT9i9dnLdhXWLncuIO5BdAbO3gwI78BK2uF8fj9dRs7mZUDCXkgzuhfF6Z0TRf27J5XNS1JdoIYtM3mMxiKlXL_EFQotOfQzsp0jlV1zc1a5xTA9hMpTMsEqtdRQaWYob4KXWLIHSP7b8iWYQAJ0R08tzp5HfOKOENz6hxi90OCGnYzdZQaJ-CfIEys0CDIGEdCykbgS99jnoAdYWdDjdVEEuSHOAiyaQlLWXzn8_uWJpE0z6pU0bsJML7a24hR6WJtXhnRI7aGSy3FpBLUtPht9gCJOtrQQjEdhj4dT33d0f1DggTxl2pQnExJy9nQZg07fltJEWrKHbsGitLhkKRok4q8d6TGMT3Hlo9cKSgLpwER73sMapdJ4CkGdrNRJH3gT8fB__SvKaQ1yjl-PYECEFvom4yIOwlE5bDJx3b2oqJiNj3SnNC4dtyEBMIzmGDIiKao9nFAxGF0xQxe8uqg2WjgSSmDoMOGWFEZPrNlA2g; _ym_visorc=b; _dc_gtm_UA-327775-35=1; _gat_UA-327775-1=1; tmr_detect=1%7C1659354352149; tmr_reqNum=57',
        'Referer': 'https://lenta.com/lk/profile/bonus-history/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64',
        'sec-ch-ua': '"Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'startDate': f'{start}T00:00:00.000+04:00',
        'endDate': f'{end}T00:00:00.000+04:00',
        'operationType': 'All',
        'offset': '0',
        'limit': '10',
    }
    response = requests.get('https://lenta.com/api/v1/me/receipt/history', params=params, cookies=cookies,
                            headers=headers).json()

    ids = []
    for item in response.get('items'):
        ids.append(item['id'])

    with open('1_id.json', 'w') as file:
        json.dump(ids, file, indent=4, ensure_ascii=False)

    result = []
    for item in ids:
        response_detail = requests.get(f'https://lenta.com/api/v1/me/receipt/details?id={item}', cookies=cookies,
                                       headers=headers).json()
        products = []
        date = response_detail.get('purchaseDate')
        price = response_detail.get('totalSale').get('value')
        for items in response_detail.get('products'):
            product = items.get('sku').get('title') + '  ' + str(items.get('price').get('value'))
            products.append(product)
        result.append(
            {
                'date': date,
                'total': price,
                'items': products
            }
        )
        time.sleep(randrange(2, 5))

    with open('2_result.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def main():
    start = str(input("Input start as 'YEAR-MN-DY: "))
    end = str(input("Input end as 'YEAR-MN-DY: "))
    get_data(start, end)


if __name__ == '__main__':
    main()
