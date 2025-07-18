import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

OUTPUT_DIR = 'output'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'jobs.csv')

# 自动安装 chromedriver
chromedriver_autoinstaller.install()

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    # 如需无头模式可取消注释
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def linkedin_login(driver, username, password):
    driver.get('https://www.linkedin.com/login')
    # 等待页面加载和元素出现
    for _ in range(30):  # 最多等30秒
        try:
            user_input = driver.find_element(By.ID, 'username')
            pass_input = driver.find_element(By.ID, 'password')
            break
        except NoSuchElementException:
            time.sleep(1)
    else:
        raise Exception('登录页面加载超时，未找到输入框')
    time.sleep(1)
    user_input.send_keys(username)
    time.sleep(1)
    pass_input.send_keys(password)
    time.sleep(1)
    pass_input.send_keys(Keys.RETURN)
    time.sleep(8)

def search_jobs(driver, keyword, location):
    search_url = f'https://www.linkedin.com/jobs/search/?keywords={keyword}'
    if location:
        search_url += f'&location={location}'
    driver.get(search_url)
    time.sleep(5)

def parse_job_cards(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_cards = soup.find_all('div', class_='base-card')
    jobs = []
    for card in job_cards:
        title = card.find('h3')
        company = card.find('h4')
        link = card.find('a', class_='base-card__full-link')
        desc = card.find('div', class_='job-search-card__snippet')
        jobs.append({
            '公司': company.get_text(strip=True) if company else '',
            '职务': title.get_text(strip=True) if title else '',
            'JD描述': desc.get_text(strip=True) if desc else '',
            '招聘链接': link['href'] if link else ''
        })
    return jobs

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    keyword = input('请输入职位关键词（如: Data Scientist）：')
    location = input('请输入base（如: Shanghai, 可留空）：')
    username = input('请输入LinkedIn账号（邮箱）：')
    password = input('请输入LinkedIn密码：')
    driver = get_driver()
    try:
        linkedin_login(driver, username, password)
        search_jobs(driver, keyword, location)
        print('正在抓取职位信息...')
        time.sleep(5)
        jobs = parse_job_cards(driver)
        df = pd.DataFrame(jobs)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f'已保存到 {OUTPUT_FILE}')
    finally:
        driver.quit()

if __name__ == '__main__':
    main() 