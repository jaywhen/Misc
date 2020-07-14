import time
import random
from selenium import webdriver

def myStar():
    #driver = webdriver.Chrome()
    driver.get('https://www.wjx.cn/m/69692400.aspx')
    answers = driver.find_elements_by_css_selector('.field.ui-field-contain')
    i = 1
    for answer in answers:
        try:
            if i==1:
                driver.execute_script("arguments[0].scrollIntoView();", answer)
                ans_sin = answer.find_elements_by_css_selector('.ui-radio') #筛选所有单选
                ans_sin[0].click()
                i=i+1


            elif i==5:
                driver.execute_script("arguments[0].scrollIntoView();", answer)
                ans_sin = answer.find_elements_by_css_selector('.ui-radio') #筛选所有单选
                ans_sin[0].click() #选参加过
                print(i)
                i = i + 1

            elif i==6:
                driver.execute_script("arguments[0].scrollIntoView();", answer)
                ans_sin = answer.find_elements_by_css_selector('.ui-radio') #筛选所有单选
                ans_sin[3].click() #选参加过
                print(i)
                i = i + 1

            elif i==11:
                driver.execute_script("arguments[0].scrollIntoView();", answer)
                ans_sin = answer.find_elements_by_css_selector('.ui-radio') #筛选所有单选
                ans_sin[2].click() #选参加过
                print(i)
                i = i + 1

            elif i == 13:
                driver.execute_script("arguments[0].scrollIntoView();", answer)
                ans_mul = answer.find_elements_by_css_selector('.ui-checkbox')
                ans_mul[0].click()
                #ans_mul[2].click()
                ans_mul[3].click()
                #ans_mul[5].click()
                #ans_mul[7].click()

            elif i == 14: #所有多选
                driver.execute_script("arguments[0].scrollIntoView();", answer)
                ans_mul = answer.find_elements_by_css_selector('.ui-checkbox')
                ans_mul[0].click()
                ans_mul[4].click()
                i=i+1

            elif i == 15: #所有多选
                driver.execute_script("arguments[0].scrollIntoView();", answer)
                ans_mul = answer.find_elements_by_css_selector('.ui-checkbox')
                ans_mul[0].click()
                ans_mul[3].click()
                i=i+1

            elif i == 16:
                driver.execute_script("arguments[0].scrollIntoView();", answer)
                ans_mul = answer.find_elements_by_css_selector('.ui-checkbox')
                ans_mul[0].click()
                ans_mul[2].click()

            elif i == 17:
                answer.find_element_by_css_selector('textarea').send_keys('无')

            else:
                driver.execute_script("arguments[0].scrollIntoView();", answer)
                ans_sin = answer.find_elements_by_css_selector('.ui-radio') #筛选所有单选
                hit_sin = random.choice(ans_sin)
                hit_sin.click()
                i = i + 1

        except Exception as e:
            print(e)
    submit_button = driver.find_element_by_css_selector('.button.blue')
    submit_button.click()

    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    #run 200 times
    for index in range(1,55):
        driver = webdriver.Chrome()
        myStar()



