from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def get_notified(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = '/home/sujay/python_projects/notice/culogo.png',
        timeout = 10
    )

def get_data(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    while True:


        myHtml = get_data('https://cuexam.net/exam-notice.php')
        soup = BeautifulSoup(myHtml, 'html.parser')
        # print(soup.prettify())
        mynoticeboard = ""
        tbl1= soup.find_all('table')[2]
        for tr in tbl1.find_all('tr'):
            for td in tr.find_all('td'):
                mynoticeboard += td.get_text()


        slicednoticeboard = mynoticeboard[23:1070]
        item_list = slicednoticeboard.split('\n\n\n')
        # print(item_list)
        calcuttauniversity = ['001', '002', '003', '004', '005', '006', '007', '008']
        for item in item_list:
            final=item.split('\n')
            print(final)
            if final[0] in calcuttauniversity:
                nTitle = 'Notice Board University of Calcutta'
                nText = f'{final[2]}:\n\n{final[1]}'
                get_notified(nTitle,nText)
                time.sleep(5)
        time.sleep(43200)


























