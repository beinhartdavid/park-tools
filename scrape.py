
import pdb
from selenium import webdriver


"""
Step 1. 
Scrape the 'base_url', and generate a 2 dimensional list containing the url and category name of every category 
Example lst = [ [Brakes, brakeUrl], []...]

"""

def getCategories():
    base_url = "https://www.parktool.com/category/tools"
    driver = webdriver.Chrome()
    driver.get(base_url)
    product_list = []
    products = driver.find_elements_by_class_name("product-category")
    for p in products:
        name = p.find_element_by_class_name("inline-headline")
        link = p.find_element_by_partial_link_text(name.text[:4])
        product_list.append([name.text,link.get_attribute("href")])
    return product_list
pdb.set_trace()


"""
Step 2.
Iterate through each URL from the list above and gather information on each product 
"""

"""
Step 3. 
Write information from step 2 to an Excel file. 
"""

"""
Step 4. 

Iterate the above steps for all products in all categories
"""