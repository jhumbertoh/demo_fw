import unittest
from datetime import datetime

#custom imports
import sys,site
from basetest import BaseTest
from pages import cotizador_page as cotizadorpage
from utils import HTMLTestRunner

class CotizadorTests(BaseTest):

    def test_models_loaded_for_brand(self):
        cotizador = cotizadorpage.CotizadorPage(self.driver)
        brand = "Daewoo"
        cotizador.input_brand(brand)
        assert cotizador.models_loaded(), "Los modelos no se cargaron para la marca> %s" % brand

    def test_solicitar_cotizacion_email_invalido(self):
        cotizador = cotizadorpage.CotizadorPage(self.driver)
        brand = "Hyundai"
        model = "Accent 1.4 GL Sedan"
        email = "mail4tests"
        telefono = '997874529'
        cotizador.input_brand(brand)
        cotizador.input_model(model)
        cotizador.input_telefono(telefono)
        cotizador.input_email(email)
        cotizador.input_quotation()
        assert cotizador.error_message_displayed(), "Se esperaba mensaje de error"



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CotizadorTests))
    filename = "reports/CotizadorTestsReport_%s_.html" % datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Cotizador Tests',
                description='Base Report for tests on Cotizador Page'
                )
    runner.run(suite)
