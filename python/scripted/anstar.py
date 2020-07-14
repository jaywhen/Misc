from selenium import webdriver
import random

driver = webdriver.Chrome()

driver.get('https://www.wjx.cn/jq/49350955.aspx')

answers = driver.find_elements_by_css_selector('.div_question')
for answer in answers:
    try:
        driver.execute_script("arguments[0].scrollIntoView();", answer)
        ans = answer.find_elements_by_css_selector('li')
        if not ans:
            answer.find_element_by_css_selector('textarea').send_keys('没有')
            continue
        a = random.choice(ans[:-1])
        a.click()
    except Exception as e:
        print(e)

submit_button = driver.find_element_by_css_selector('#submit_button')
submit_button.click()
