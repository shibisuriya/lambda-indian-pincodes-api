import requests
import json

def lambda_handler(event, context):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.postalpincode.in',
        'Referer': 'http://www.postalpincode.in/Search-By-PIN-Code',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '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',
        '__VIEWSTATEGENERATOR': 'ECAD39C8',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': 'W62NxJoKlL8dc2YnCQqBz+04nFan74fKnKBxDZoX4t00IERSXb/GJxTDjPy9TOYi/S0AvhdNo24Ra5MMz0/XpY8Lmn5cxHqYiuRQteDoTfNORPqw+mpxGDHZiXJxEVharrOdh/g0HYogM29nkMRrAyEGRLovpfKxY0hUSLpohK8=',
        'ctl00$ContentPlaceHolder1$txtPINCode': '600097',
        'ctl00$ContentPlaceHolder1$btnSearch': 'Submit',
    }

    response = requests.post('http://www.postalpincode.in/Search-By-PIN-Code', headers=headers, data=data, verify=False)

    return {
        status: 200,
        body: json.dump(response.text)
    }
