import random
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.wjx.cn/m/68711134.aspx')
# 空格要用.代替
answers = driver.find_elements_by_css_selector('.field.ui-field-contain')
i = 1
for answer in answers:
    try:
        # driver.execute_script("arguments[0].scrollIntoView();", answer)
        # ans_sin = answer.find_elements_by_css_selector('.ui-radio') #筛选所有单选
        if i==1 or i==2:
            driver.execute_script("arguments[0].scrollIntoView();", answer)
            ans_sin = answer.find_elements_by_css_selector('.ui-radio') #筛选所有单选
            hit_sin = random.choice(ans_sin[:-1])
            hit_sin.click()
            i = i + 1
        elif i==7:
            driver.execute_script("arguments[0].scrollIntoView();", answer)
            ans_sin = answer.find_elements_by_css_selector('.ui-radio') #筛选所有单选
            ans_sin[0].click()
            print(i)
            i = i + 1
        elif i==5 or i==6 or i==11 or i==14:
            ans_mul = answer.find_elements_by_css_selector('.ui-checkbox')
            ans_mul[1].click()
            ans_mul[2].click()
            i=i+1
        elif i==17:
            answer.find_element_by_css_selector('textarea').send_keys('无')

        else:
            driver.execute_script("arguments[0].scrollIntoView();", answer)
            ans_sin = answer.find_elements_by_css_selector('.ui-radio') #筛选所有单选
            hit_sin = random.choice(ans_sin)
            hit_sin.click()
            i = i + 1

    except Exception as e:
        print(e)

# submit_button = driver.find_element_by_css_selector('.button.blue')
# submit_button.click()
