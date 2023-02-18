from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from seleniumwire import webdriver
import schedule
import random,time,os,requests
from time import sleep
cwd = os.getcwd()
opts = Options()

#opts.add_argument('--headless=chrome')
opts.headless = False
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
opts.add_extension(f"{cwd}\\metamaskExtension.crx")

def date():
    date = f"[{time.strftime('%d-%m-%y %X')}]"
    return date

def xpath_long(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all) 

def xpath_el(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    element_all.click()

def xpath_fast(el):
    element_all = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all) 

def xpath_type(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(word)
     
def xpath_type_fast(el,word):
    return wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(word)
     
def signConfirm():
    print("[*] Signing")
    time.sleep(3)

    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[2])

    browser.get('chrome-extension://{}/popup.html'.format("nkbihfbeogaeaoehlefnkodbefgpgknn"))
    time.sleep(5)
    browser.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(3)
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]'))).click()
    time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    # time.sleep(3)
    print('[*] Sign confirmed')
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(3)


def connectToWebsite():
    time.sleep(3)

    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])

    browser.get('chrome-extension://{}/popup.html'.format("nkbihfbeogaeaoehlefnkodbefgpgknn"))
    time.sleep(5)
    browser.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(3)
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]'))).click()
    time.sleep(1)
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]'))).click()
    time.sleep(3)
    print('[*] Site connected to metamask')
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(3)
    
def metamaskSetup(recoveryPhrase, password):
    browser.switch_to.window(browser.window_handles[0])

    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Get Started"]'))).click()
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Import wallet"]'))).click()
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//button[text()="No Thanks"]'))).click()

    inputs = wait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH, '//input')))
    inputs[0].send_keys(recoveryPhrase)
    inputs[1].send_keys(password)
    inputs[2].send_keys(password)
    wait(browser,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.first-time-flow__terms'))).click()
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Import"]'))).click()

    time.sleep(5)

    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//button[text()="All Done"]'))).click()
    time.sleep(2)

    # closing the message popup after all done metamask screen
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="popover-content"]/div/div/section/header/div/button'))).click()
    time.sleep(5)
    print("[*] Wallet has been imported successfully")
    

def run_ace_fountain():
    global browser
    address_file = "list_akun.txt"
    get_add = open(f"{cwd}/{address_file}","r")
    get_add = get_add.read()
    get_add = get_add.split("\n")
   
    for urutan in get_add:
        parts = urutan.split(";")

        # Memisahkan bagian "parts[1]" berdasarkan ":"
        subparts = parts[1].split(":")

        # Menyimpan hasil ke dalam variabel yang sesuai
        pharse = parts[0]
        host = subparts[0]
        port = subparts[1]
        user = subparts[2]
        password = subparts[3]

        proxy_options = {
            'proxy': {
                'http': f'http://{user}:{password}@{host}:{port}',
                'https': f'https://{user}:{password}@{host}:{port}'
            },
            "backend": "default",
            'mitm_http2': False 
            }
        browser = webdriver.Chrome(options=opts,desired_capabilities=dc,seleniumwire_options=proxy_options)
        metamaskSetup(pharse,"123Pass##okSa")
        browser.get('https://ace.fusionist.io/')
        xpath_long('//button[text()="Connect Wallet"]')
        xpath_long("//button[text()='MetaMask']")
        connectToWebsite()
        try:
            signConfirm()
        except:
            pass
        browser.get('https://ace.fusionist.io/account/endurance')
        sleep(5)
        xpath_el("//p[contains(text(),'Fountain'])]/parent::div//button")
        sleep(5)
        browser.quit()

def run_ace_pump():
    global browser
    address_file = "list_akun.txt"
    get_add = open(f"{cwd}/{address_file}","r")
    get_add = get_add.read()
    get_add = get_add.split("\n")
   
    for urutan in get_add:
        parts = urutan.split(";")

# Memisahkan bagian "parts[1]" berdasarkan ":"
        subparts = parts[1].split(":")

        # Menyimpan hasil ke dalam variabel yang sesuai
        pharse = parts[0]
        host = subparts[0]
        port = subparts[1]
        user = subparts[2]
        password = subparts[3]

        proxy_options = {
            'proxy': {
                'http': f'http://{user}:{password}@{host}:{port}',
                'https': f'https://{user}:{password}@{host}:{port}'
            },
            "backend": "default",
            'mitm_http2': False 
            }
        browser = webdriver.Chrome(options=opts,desired_capabilities=dc,seleniumwire_options=proxy_options)
        metamaskSetup(pharse,"123Pass##okSa")
        browser.get('https://ace.fusionist.io/')
        xpath_long('//button[text()="Connect Wallet"]')
        xpath_long("//button[text()='MetaMask']")
        connectToWebsite()
        try:
            signConfirm()
        except:
            pass
        browser.get('https://ace.fusionist.io/account/endurance')
        sleep(5)
        xpath_el("//p[text()='Ace Pump']/parent::div//button")
        sleep(5)
        try:
            signConfirm()
        except:
            pass
        browser.quit()

 
if __name__ == '__main__':
    global inp
    
    inp = input("[*] 1. Pump\n[*] 2. Fountain\n[*] Choose (1/2): ")
    if inp == "1":
        run_ace_pump()
    else:
        run_ace_fountain()
# Jalankan fungsi run_ace_fountain() setiap 24 jam sekali

# schedule.every(24).hours.do(run_ace_fountain)

# # Jalankan fungsi run_ace_pump() setiap 12 jam sekali
# schedule.every(12).hours.do(run_ace_pump)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
    
