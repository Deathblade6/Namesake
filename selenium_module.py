# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re,time
from selenium import webdriver
    
def main():
    fp = open("name.txt" , "w+")
    driver = webdriver.Firefox()
    driver.get("http://results.cusat.ac.in/regforms/regno1.php")
    regno = driver.find_element_by_name("rno")
    regno.clear()
    button = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/input")
    for i in range(12180000,12180094):
        name_regex = re.compile(r'<b>\w+ (\w+)?')
        regno.send_keys(str(i))
        button = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/input")
        button.click()
        time.sleep(10)
        name  = name_regex.search(driver.page_source) 
        name_final = name.group().split('>')
        print (name_final[1])
        fp.write(name_final[1])
        driver.back()
        regno = driver.find_element_by_name("rno")
        regno.clear()
        time.sleep(4)
    fp.close()
main()
