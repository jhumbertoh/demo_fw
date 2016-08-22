from basepage import BasePage


class CotizadorPage(BasePage):

    def input_brand(self, brand):
        element = self.driver.find_element_by_id("Marca")
        element.send_keys(brand)

    def models_loaded(self):
        element = self.driver.find_element_by_id("Modelo")
        return (element.text == ":: Seleccione ::")
