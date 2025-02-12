from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import qrcode
from art import text2art

X = 10  # 要取前 X 個

class expected_condition(object):

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)   # Finding the referenced element
        if(elements):
            for ele in elements:
                if len(ele.text) <= 0:
                    return False
            return elements


service_obj = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome()#use this in Win11



result = []

url = "https://game8.jp/pokemonsleep/541511"
chrome.get(url)
#chrome.refresh()


delay = 20 # seconds
try:
    WebDriverWait(chrome, delay).until(expected_condition((By.CSS_SELECTOR,"div.c-commentItem__code")))

except TimeoutException:
    print ("Loading took too much time!")



elements = chrome.find_elements(By.CSS_SELECTOR, "p[id^='js-copy-text']")[:X]

# 取得文字內容
codes = [el.text for el in elements]

chrome.quit()

# 印出結果
print(codes)

for code in codes:
    clean_code = "94jfutn"+code.replace("-", "")  # 移除 '-'
    

    qr = qrcode.QRCode()
    qr.add_data(clean_code)
    qr.make()
    # 以更漂亮的方式顯示 QR Code
    qr.print_ascii(invert=True)#寶可夢睡好像只吃白底黑圖的 QR code
    print(code)
    
    


