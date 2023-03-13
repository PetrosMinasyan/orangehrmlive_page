import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('get_driver')
class TestsHRM:
    def test_login(self):
        input_name = 'Admin'
        input_password = 'admin123'
        self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[name = "username"]').send_keys(input_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(input_password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

        self.get_wait.wait_for_element(By.XPATH, "//*[text() = 'My Info']").click()
        first_name = self.get_wait.wait_for_element(By.CSS_SELECTOR, "input[name='firstName']")

        first_name.send_keys(Keys.CONTROL + 'a')
        first_name.send_keys(Keys.BACK_SPACE)
        first_name.send_keys("Clark")

        first_name.click()
        first_name.send_keys(Keys.CONTROL + 'a')
        first_name.send_keys(Keys.BACK_SPACE)
        first_name.send_keys("Steven")
        name = "Steven"
        self.get_wait.wait_for_element(By.CSS_SELECTOR, "input[name='firstName']")
        attribute_value = first_name.get_attribute("value")
        assert attribute_value == name

        # change the second name
        second_name = self.driver.find_element(By.CSS_SELECTOR, 'input[name="middleName"]')
        self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[name="middleName"]')
        second_name.send_keys(Keys.CONTROL + 'a')
        second_name.send_keys(Keys.BACK_SPACE)
        second_name.send_keys("Green")
        surname = "Green"
        surname_value = second_name.get_attribute("value")
        assert surname_value == surname

        # change the middle name
        middle_name = self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]')
        self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[name="lastName"]')
        middle_name.send_keys(Keys.CONTROL + 'a')
        middle_name.send_keys(Keys.BACK_SPACE)
        middle_name.send_keys("Quora")
        mid_name = "Quora"
        middle_name_value = middle_name.get_attribute("value")
        assert middle_name_value == mid_name

        # change the Nickname fild
        self.get_wait.wait_for_element(By.XPATH, '(//*[@class="oxd-input oxd-input--active"])[2]')
        nickname_button = self.driver.find_element(By.XPATH, '(//*[@class="oxd-input oxd-input--active"])[2]')
        nickname_button.send_keys(Keys.CONTROL + 'a')
        nickname_button.send_keys(Keys.BACK_SPACE)
        nickname_button.send_keys("Alex")
        nickname_fild = nickname_button.get_attribute("value")
        assert nickname_fild == "Alex"

        # chang the ID fild
        self.get_wait.wait_for_element(By.XPATH, '(//*[@class="oxd-input oxd-input--active"])[2]')
        employ_Id_button = self.driver.find_element(By.XPATH, '(//*[@class="oxd-input oxd-input--active"])[2]')
        employ_Id_button.send_keys(Keys.CONTROL + 'a')
        employ_Id_button.send_keys(Keys.BACK_SPACE)
        employ_Id_button.send_keys("2002")
        id_fild = employ_Id_button.get_attribute("value")
        assert id_fild == "2002"

        # chang other ID fild
        self.get_wait.wait_for_element(By.XPATH, '(//*[@class="oxd-input oxd-input--active"])[4]')
        other_ID_button = self.driver.find_element(By.XPATH, '(//*[@class="oxd-input oxd-input--active"])[4]')
        other_ID_button.send_keys(Keys.CONTROL + 'a')
        other_ID_button.send_keys(Keys.BACK_SPACE)
        other_ID_button.send_keys("1001")
        other_ID = other_ID_button.get_attribute("value")
        assert other_ID == "1001"

        self.get_wait.wait_for_element(By.XPATH, '(//*[@class="oxd-input oxd-input--active"])[4]')
        license_number = self.driver.find_element(By.XPATH, '(//*[@class="oxd-input oxd-input--active"])[4]')
        license_number.send_keys(Keys.CONTROL + 'a')
        license_number.send_keys(Keys.BACK_SPACE)
        license_number.send_keys("1122")
        driver_license_number = license_number.get_attribute("value")
        assert driver_license_number == "1122"

        # work with calendar
        self.get_wait.wait_for_element(By.CSS_SELECTOR, 'i[class="oxd-icon bi-calendar oxd-date-input-icon"]')
        self.driver.execute_script("window.scrollBy(0, -500);")
        calendar_button = self.driver.find_elements(By.CSS_SELECTOR,
                                                    'i[class="oxd-icon bi-calendar oxd-date-input-icon"]')
        calendar_button[0].click()
        drop_down_button = self.driver.find_elements(By.CSS_SELECTOR,
                                                     'i[class="oxd-icon bi-caret-down-fill oxd-icon-button__icon"]')
        drop_down_button[1].click()
        click_2018 = self.driver.find_element(By.XPATH, '//li[contains(text(), "2018")]')
        click_2018.click()
        self.get_wait.wait_for_element(By.XPATH, '//li[contains(text(), "2018")]')
        self.driver.execute_script("window.scrollBy(0, 300);")
        today_calendar = self.driver.find_element(By.CSS_SELECTOR, 'div[class="oxd-date-input-link --today"]')
        today_calendar.click()

        # chang the SIN Number fild
        self.get_wait.wait_for_element(By.XPATH, '(//*[@class="oxd-input oxd-input--active"])[6]')
        sin_number = self.driver.find_element(By.XPATH, '(//*[@class="oxd-input oxd-input--active"])[6]')
        sin_number.send_keys(Keys.CONTROL + 'a')
        sin_number.send_keys(Keys.BACK_SPACE)
        sin_number.send_keys("19-20-99-20")
        sin_number_fild = sin_number.get_attribute("value")
        assert sin_number_fild == "19-20-99-20"

        self.get_wait.wait_for_element(By.XPATH,
                                       '(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[1]')
        nationality_drop_down = self.driver.find_element(By.XPATH,
                                                         '(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[1]')
        self.get_wait.wait_for_element(By.XPATH, '(//div[@clear="false"])[1]')
        self.driver.find_element(By.XPATH, '(//div[@clear="false"])[1]')
        nationality_drop_down.click()
        button_drop_down = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="option"]')
        button_drop_down[2].click()


        drop_down_marital_status = self.driver.find_element(By.XPATH,
                                                            '(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[2]')
        drop_down_marital_status.click()
        self.get_wait.wait_for_element(By.XPATH, '(//div[@role="option"])[2]')
        click_single = self.driver.find_element(By.XPATH, '(//div[@role="option"])[2]')
        click_single.click()
        # marital_status_fild = click_single.get_attribute("value")

        open_calendar = self.driver.find_element(By.XPATH,
                                                 '(//i[@class="oxd-icon bi-calendar oxd-date-input-icon"])[2]')
        open_calendar.click()
        self.get_wait.wait_for_element(By.CSS_SELECTOR, 'div[class="oxd-date-input-link --today"]')
        todays_day = self.driver.find_element(By.CSS_SELECTOR, 'div[class="oxd-date-input-link --today"]')
        todays_day.click()
        assert todays_day.is_displayed()

        click_male = self.driver.find_element(By.XPATH,
                                              '(//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"])[1]')
        click_male.click()
        assert click_male.is_enabled()

        # Military Service fild
        self.get_wait.wait_for_element(By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[10]')
        military_service_fild = self.driver.find_element(By.XPATH,
                                                         '(//input[@class="oxd-input oxd-input--active"])[10]')
        military_service_fild.send_keys(Keys.CONTROL + 'a')
        military_service_fild.send_keys(Keys.BACK_SPACE)
        military_service_fild.send_keys("Yes")
        check_service = military_service_fild.get_attribute("value")
        assert check_service == "Yes"

        # Smoker button
        self.get_wait.wait_for_element(By.CSS_SELECTOR,
                                       'span[class="oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input"]')
        click_smoker = self.driver.find_element(By.CSS_SELECTOR,
                                            'span[class="oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input"]')
        click_smoker.click()
        assert click_smoker.is_enabled()

        save_button = self.driver.find_element(By.XPATH, '(//*[@type="submit"])[1]')
        save_button.click()

        # make sure the page is saved
        successful_update = self.driver.find_element(By.CSS_SELECTOR,
                                                     'div[class="oxd-toast-container oxd-toast-container--bottom"]')
        self.get_wait.wait_for_element(By.CSS_SELECTOR, 'div[class="oxd-toast-container oxd-toast-container--bottom"]')
        assert successful_update.is_displayed()
