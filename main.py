class FINDNEWNOTICE:
    def __init__(self):
        self.page_url = "https://sinseo.sen.ms.kr/186943/subMenu.do"
        self.time_interval = 5
        self.target_text = "역사"
        self.alarm_sound = "alarm sound.mp3"

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)


    def main(self):
        checked = 0
        while True:
            checked += 1
            if self.checkNewNotice():
                print(f"찾으시는 공지가 업로드되었어요! ({checked})")
                playsound2.playsound(self.alarm_sound)
                webbrowser.open(self.page_url)
            else:
                print(f"아직 업로드 되지 않았어요! ({checked})")
            time.sleep(self.time_interval)


    def checkNewNotice(self):
        self.driver.get(self.page_url)
        self.driver.implicitly_wait(10)

        text_len = len(self.driver.find_element(By.CSS_SELECTOR, "#board_area > table > tbody").text.split("\n"))
        table = []
        for i in range(1, text_len + 1):
            table_temp = []
            for j in range(1, 6):
                table_temp.append(self.driver.find_element(By.CSS_SELECTOR,
                                                      "#board_area > table > tbody > tr:nth-child({}) > td:nth-child({})".format(
                                                          i, j)).text)
            table.append(table_temp)

        for i in range(len(table)):
            table[i][1] = table[i][1].replace(",", "")
            table[i][1] = table[i][1].strip()

        if self.target_text in table[0][1]:
            return True
        else:
            return False


if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import webbrowser
    import playsound2

    findnewnotice = FINDNEWNOTICE()
