from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import locators as lc
options = Options()
class Test_Sauce:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    def teardown_method(self):   
         self.driver.quit() 
    def test_login_empty(self):
        self.waitDriver((By.XPATH,lc.userNameXpath))
        userName= self.driver.find_element(By.XPATH,lc.userNameXpath)
        self.waitDriver((By.XPATH,lc.passwordXpath))
        password = self.driver.find_element(By.XPATH,lc.passwordXpath)

        if userName.text == "" and password.text == "":
            loginButton = self.driver.find_element(By.XPATH,lc.loginButtonXpath)
            loginButton.click()
            self.waitDriver((By.XPATH,lc.errorAreaXpath))
            errorArea = self.driver.find_element(By.XPATH,lc.errorAreaXpath)

        assert errorArea.text == "Epic sadface: Username is required"  ,"text should be 'Epic sadface: Username is required'"
    def test_userNameArea(self):
        self.waitDriver((By.XPATH,lc.userNameXpath))
        userName= self.driver.find_element(By.XPATH,lc.userNameXpath)
        userName.send_keys("standard_user")
        userName.send_keys(Keys.ENTER)
        self.waitDriver((By.XPATH,lc.passwordXpath))
        password = self.driver.find_element(By.XPATH,lc.passwordXpath)
        time.sleep(5)
        
        if  password.text == "":
            loginButton = self.driver.find_element(By.XPATH,lc.loginButtonXpath)
            loginButton.click()
            self.waitDriver((By.XPATH,lc.erorAreaDenemeXpath))
            errorAreaDeneme = self.driver.find_element(By.XPATH,lc.erorAreaDenemeXpath)
            errorAreaDeneme.text
        assert errorAreaDeneme.text == "Epic sadface: Password is required"

    def test_success(self):
        self.waitDriver((By.XPATH,lc.userNameXpath))
        userName= self.driver.find_element(By.XPATH,lc.userNameXpath)
        userName.send_keys("standard_user")
        self.waitDriver((By.XPATH,lc.passwordXpath))
        password = self.driver.find_element(By.XPATH,lc.passwordXpath)
        password.send_keys("secret_sauce")
        souceProducts = len(self.driver.find_elements(By.XPATH,lc.souceProductsXpath))
        souceProductsPrice = self.driver.find_elements(By.XPATH,lc.souceProductsPriceXpath)
        priceArray = []
        for i in souceProductsPrice:
            priceText =i.text
            priceArray.append(priceText)
        assert souceProducts == len(priceArray)    

    def waitDriver(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator)) 
