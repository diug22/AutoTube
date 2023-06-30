import undetected_chromedriver as uc
from undetected_chromedriver import By
from selenium.webdriver.chrome.options import Options
from time import sleep

import os

class Constants:
    def __init__(self) -> None:
        self.UPLOAD_BUTTON = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button'
        self.UPLOAD_VIDEO = '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a'
        self.UPLOAD_VIDEO_FILE = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input'
        self.TITLE_INPUT = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div'
        self.DESCRIPTION_INPUT = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-video-description/div/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div'
        self.NEXT_BUTTON = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]'
        self.NOT_FOR_KIDS = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[2]'
        self.FOR_KIDS = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]'
        self.PRIVATE = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]'
        self.PUBLIC = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]'
        self.DONE_BUTTON = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]'


class Yt_selenium_uploader:
    def __init__(self) -> None:
        self.driver = uc.Chrome()
        self.yt = Constants()

    def login(self, username, password):
        self.driver.get('https://accounts.google.com/ServiceLogin')
        sleep(2)

        self.driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]').click()
        sleep(2)

        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
        sleep(25)
        
    def upload_video(self, file, title, desc):
        try:
            self.driver.get("https://youtube.com")
            sleep(2)
            self.driver.find_element(By.XPATH, self.yt.UPLOAD_BUTTON).click()
            sleep(2)
            self.driver.find_element(By.XPATH, self.yt.UPLOAD_VIDEO).click()
            sleep(5)
            self.driver.find_element(By.XPATH, self.yt.UPLOAD_VIDEO_FILE).send_keys(os.path.abspath(file))
            sleep(5)
            self.driver.find_element(By.XPATH, self.yt.TITLE_INPUT).clear()
            self.driver.find_element(By.XPATH, self.yt.TITLE_INPUT).send_keys(title)
            self.driver.find_element(By.XPATH, self.yt.DESCRIPTION_INPUT).send_keys(desc)
            self.driver.find_element(By.XPATH, self.yt.NEXT_BUTTON).click()
            self.driver.find_element(By.XPATH, self.yt.NOT_FOR_KIDS).click()
            sleep(3)
            self.driver.find_element(By.XPATH, self.yt.NEXT_BUTTON).click()
            self.driver.find_element(By.XPATH, self.yt.NEXT_BUTTON).click()
            self.driver.find_element(By.XPATH, self.yt.NEXT_BUTTON).click()
            sleep(2)
            self.driver.find_element(By.XPATH, self.yt.PRIVATE).click()
            
            self.driver.find_element(By.XPATH, self.yt.DONE_BUTTON).click()
            sleep(5)
            return True
        except:
            return False
        
        



