import time
from pynput import keyboard
from pynput.keyboard import Controller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("abubakar")

gender = driver.find_element(By.XPATH,"//*[@id='male']")
gender.click()


driver.find_element(By.XPATH,"//*[@id='thursday']").click()

driver.find_element(By.XPATH,"//*[@id='saturday']").click()

time.sleep(5)

country_element = driver.find_elements(By.XPATH,"//*[@id='country']/option")
for country in country_element:
    if country.text == "Canada":
        print(country.text)


color_element = driver.find_elements(By.XPATH,"//*[@id='colors']/option")
for color in color_element:
    if color.text == "Green" or color.text == "Blue":
        print(color.text)

colors_drop = driver.find_element(By.XPATH,"//*[@id='colors']")
colors = Select(colors_drop)
colors.select_by_value("green")
colors.select_by_value("red")
time.sleep(5)

animal_dropdown = driver.find_element(By.XPATH,"//*[@id='animals']")
animals = Select(animal_dropdown)
animals.select_by_visible_text("Dog")
animals.select_by_visible_text("Cat")
time.sleep(5)

Date_Picker1 = driver.find_element(By.ID,"datepicker")
Date_Picker1.send_keys("03/25/2025")
time.sleep(5)

Data_Picket3_Start_Date = driver.find_element(By.ID,"start-date")
Data_Picket3_Start_Date.send_keys("03/25/2025")
Data_Picket3_End_Date = driver.find_element(By.ID,"end-date")
Data_Picket3_End_Date.send_keys("04/01/2025")


submit_btn = driver.find_element(By.CLASS_NAME,"submit-btn")
submit_btn.click()

msg = driver.find_element(By.XPATH,"//*[@id='result']")

if msg.text == "You selected a range of 7 days.":
    print("True")

time.sleep(5)

#
file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "singleFileInput"))
    )
file_input.send_keys("D:\\data1.xlsx")  # Use correct path

    #Wait and click the submit button
submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='singleFileForm']/button"))
    )
submit_button.click()

time.sleep(5)

rows = driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr")
row_count = len(rows)
print(row_count)

# Iterate through each row and print the data
for row in rows:
    # Find all cells in the current row
    cells = row.find_elements(By.TAG_NAME, "td")

    # Print each cell's text
    print("Row: ", end="")
    for cell in cells:
        print(cell.text)
    print()

Check = driver.find_elements(By.XPATH,"//*[@id='productTable']/tbody/tr/td[4]")
check_total = len(Check)
print(check_total)



