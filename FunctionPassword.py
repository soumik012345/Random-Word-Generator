import time
import pyautogui as pag
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from configparser import ConfigParser
import datetime
from urllib.request import Request, urlopen
import random
from configparser import ConfigParser
from configparser import SafeConfigParser
import pyscreeze
from PIL import Image
import cv2



class Password:
    def __init__(self):
        pass

# This Function is used to Read Data From Configuration File file
    def readConfiguration(self):
        configParser = ConfigParser(interpolation=None)
        configParser.read('G:/Huawei_Automations/Config/iMaster-NCE-Credentials.ini')
        self.f_username = configParser.get('NCE', 'Username')
        self.f_password = configParser.get('NCE', 'Password')
        self.f_url = configParser.get('NCE', 'Url')
        self.f_path = configParser.get('NCE', 'OSPFDataDir')

# This function is used to load and install chrome driver and click on Advance button and Ip before login page
    def chromeconfig(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        self.driver.get(self.f_url)
        self.driver.maximize_window()
        time.sleep(2)
        advance = self.driver.find_element_by_xpath('//*[@id="details-button"]')
        advance.click()
        time.sleep(1)
        ip = self.driver.find_element_by_xpath('//*[@id="proceed-link"]')
        ip.click()
        time.sleep(2)

# This Function is used to get username and password from readtextfile() function and complete login & after login click agree button
    def login(self):
        username = self.driver.find_element_by_xpath('//*[@id="username"]')
        username.send_keys(self.f_username)
        time.sleep(2)
        pin = self.driver.find_element_by_xpath('//*[@id="value"]')
        pin.send_keys(self.f_password)

        btn = self.driver.find_element_by_xpath('//*[@id="submitDataverify"]')
        btn.click()

        time.sleep(5)
        agree =self.driver.find_element_by_xpath('//*[@id="login_warn_confirm"]')
        agree.click()
        time.sleep(2)

        print("Login Completed")

    def passwordChangeStep(self):

        #self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/div').click()
        time.sleep(5)
        pag.press('tab')
        pag.press('tab')
        pag.press('enter')
        time.sleep(2)
        pag.press('tab')
        pag.press('enter')
        time.sleep(5)

        # For old Password
        time.sleep(2)
        pag.press('tab')
        pag.press('tab')
        pag.press('tab')
        pag.press('tab')
        pag.press('tab')
        pag.press('tab')
        pag.press('tab')
        pag.press('tab')
        pag.press('tab')
        pag.press('tab')
        pag.press('tab')
        pag.press('tab')
        time.sleep(5)
        #pag.typewrite(self.f_password, interval=0.25)
        time.sleep(2)
        pag.press('tab')
        pag.press('tab')
        time.sleep(2)

    def randompasswordgenerator(self):

        # # Create Current Date
        # now = datetime.datetime.now()
        # currentTimeDate = now.strftime("%Y%m%d")
        #
        # # Create Random Word
        # url = "https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
        # req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        # web_byte = urlopen(req).read()
        # webpage = web_byte.decode('utf-8')
        # first5 = webpage[:500].split("\n")
        # random.shuffle(first5)
        # for i in range(len(first5)):
        #     word = (first5[5])
        #     break
        # print("New Generated Password", word)
        #
        # self.new_password = word + "#" + currentTimeDate
        #
        # print(self.new_password)
        #
        # # Write new generated possword on new password and confrim password input box
        # time.sleep(2)
        # pag.typewrite(self.new_password)
        pag.press('tab')
        time.sleep(2)
        # pag.typewrite(self.new_password)


    def openExistigTxtFile(self):
        a = 'Fahim'
        import configparser
        config = configparser.ConfigParser()
        config.read('G:/RAT-Automation-src/iMaster-NCE-Credentials.ini')
        config.set('NCE', 'Password', a)



        with open("G:/RAT-Automation-src/iMaster-NCE-Credentials.ini", "w") as configfile:
            config.write(configfile)
        parser = SafeConfigParser()



    def clickapply(self):
        pag.press('tab')
        pag.press('enter')
        #self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/table/tbody/tr/td/div/div/table/tr[5]/td[2]/button').click()




    def logout(self):
        #time.sleep(10)

        logouticon = pag.locateOnScreen(
            "G:\\RAT-Automation-src\\PasswordChange\\images\\rsz_1logout.png",
            grayscale=True, confidence=.9)
        while logouticon == None:

            logouticon = pag.locateOnScreen(
                "G:\\RAT-Automation-src\\OSPFParameterSettings\\images\\rsz_1logout.png",
                grayscale=True, confidence=.9)
            if (logouticon != None):
                pag.click(pag.center(logouticon))
                break;
            time.sleep(3)
        pag.click(pag.center(logouticon))
        pag.press('enter')
        pag.press('enter')
        pag.press('tab')
        pag.press('enter')


    def exitapp(self):
        self.driver.quit()




