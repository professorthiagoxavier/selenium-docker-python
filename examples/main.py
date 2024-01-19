from typing import Literal
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 
import pymsteams

class InfologistixCrawler():
  
    def __init__(self, url: str, headless: bool=True) -> None:
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1280,720")
        options.add_argument("--disable-dev-shm-usage")
        if headless:
            options.add_argument("--headless")
        self.__driver = Chrome(options=options)
        self.__driver.get(url)
        self.close()

    def close(self) -> None:
        self.__driver.close()



def sendMSTeams(webhook : str, message : str, title : str) -> Literal[True]:
    channel = pymsteams.connectorcard(webhook)
    channel.title(title)
    channel.text(message)
    return channel.send()


if __name__ == "__main__":
    services = InfologistixCrawler(url="https://infologistix.de")
    #print(services)
    # make a html table 
    #message = services.to_html()
    print('fim')
    # comment out if you have a webhook.
    #sendMSTeams("webhook", message=message, title=title)