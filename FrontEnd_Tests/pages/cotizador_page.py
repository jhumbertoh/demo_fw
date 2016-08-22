from basepage import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class CotizadorPage(BasePage):

    def input_on_element(self,element_id, value):
        element = self.driver.find_element_by_id(element_id)
        element.send_keys(value)

    def input_brand(self, brand):
        self.input_on_element("Marca",brand)

    def input_model(self,model):
        self.input_on_element("Modelo",model)

    def input_email(self,email):
        self.input_on_element("EmailCotizacion",email)


    def input_telefono(self,email):
        self.input_on_element("TelefonoCotizacion",email)

    def input_quotation(self):
        element = self.driver.find_element_by_id("btnComparar")
        element.click()


    def models_loaded(self):
        element = self.driver.find_element_by_id("Modelo")
        return (element.text == ":: Seleccione ::")

    def error_message_displayed(self):
        js_script = "return document.getElementsByClassName('ui-pnotify-text').length == 1"
        try:
            return WebDriverWait(self.driver, 5).until(lambda driver:
            self.driver.execute_script(js_script))
        except TimeoutException:
            print "El mensaje de error no fue mostrado"
