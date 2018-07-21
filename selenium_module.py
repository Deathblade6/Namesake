# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests,bs4,time
def scrape( url ):
    res=requests.get(url)
    res.raise_for_status
    nostarch = bs4.BeautifulSoup(res.text , "html.parser")
    print (nostarch.prettify())
    a = nostarch.select("b")
    print (a)
    print ("Working?")
def main():
    from selenium import webdriver
    driver = webdriver.Firefox(executable_path=r"C:\Users\Harikrishn\Desktop\Arun's Stuff(TOXIC AF)\geckodriver.exe")
    driver.get("http://results.cusat.ac.in/regforms/regno1.php")
    regno = driver.find_element_by_name("rno")
    regno.clear()
    button = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/input")
    regno.send_keys('12180021')
    button.click()
    scrape(driver.current_url)
    time.sleep(5)
    driver.back()
    regno = driver.find_element_by_name("rno")
    regno.clear()
main()


