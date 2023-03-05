from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()

class Tests:
    def test_radio_button_example(self):
        driver.get("https://courses.letskodeit.com/practice")
        wait = WebDriverWait(driver, 10)
        bmw_radiobutton = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="bmwradio"]')))
        benz_radiobutton = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="benzradio"]')))
        honda_radiobutton = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="hondaradio"]')))
        assert not benz_radiobutton.is_selected()
        assert not bmw_radiobutton.is_selected()
        assert not honda_radiobutton.is_selected()
        bmw_radiobutton.click()
        assert bmw_radiobutton.is_selected()
        assert not benz_radiobutton.is_selected()
        assert not honda_radiobutton.is_selected()
        benz_radiobutton.click()
        assert benz_radiobutton.is_selected()
        assert not bmw_radiobutton.is_selected()
        assert not honda_radiobutton.is_selected()
        honda_radiobutton.click()
        assert honda_radiobutton.is_selected()
        assert not bmw_radiobutton.is_selected()
        assert not benz_radiobutton.is_selected()
    def test_checkbox_example(self):
        driver.get("https://courses.letskodeit.com/practice")
        wait = WebDriverWait(driver, 10)
        bmw_checkbox = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="bmwcheck"]')))
        benz_checkbox = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="benzcheck"]')))
        honda_checkbox = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="hondacheck"]')))
        assert not bmw_checkbox.is_selected()
        assert not benz_checkbox.is_selected()
        assert not honda_checkbox.is_selected()
        bmw_checkbox.click()
        assert bmw_checkbox.is_selected()
        assert not benz_checkbox.is_selected()
        assert not honda_checkbox.is_selected()
        benz_checkbox.click()
        assert bmw_checkbox.is_selected()
        assert benz_checkbox.is_selected()
        assert not honda_checkbox.is_selected()
        honda_checkbox.click()
        assert bmw_checkbox.is_selected()
        assert benz_checkbox.is_selected()
        assert honda_checkbox.is_selected()
        bmw_checkbox.click()
        assert not bmw_checkbox.is_selected()
        assert benz_checkbox.is_selected()
        assert honda_checkbox.is_selected()
        benz_checkbox.click()
        assert not bmw_checkbox.is_selected()
        assert not benz_checkbox.is_selected()
        assert honda_checkbox.is_selected()
        honda_checkbox.click()
        assert not bmw_checkbox.is_selected()
        assert not benz_checkbox.is_selected()
        assert not honda_checkbox.is_selected()
    def test_mouse_hover(self):
        driver.get("https://courses.letskodeit.com/practice")
        wait =  WebDriverWait(driver, 10)
        mouse_hover = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="mousehover"]')))
        driver.execute_script("arguments[0].scrollIntoView();", mouse_hover)
        honda_radiobutton = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="hondaradio"]')))

        actions=ActionChains(driver)
        actions.move_to_element(mouse_hover).perform()

        reload_hover = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="mouse hover content"] > a:nth-child(2)')))
        reload_hover.click()
        honda_radiobutton = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="hondaradio"]')))
        assert not honda_radiobutton.is_selected()

        driver.quit()
        