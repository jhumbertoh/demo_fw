import unittest
from datetime import datetime
import HTMLTestRunner
#custom imports
import sys,site
site.addsitedir(sys.path[0]+'\\pages')
from basetest import BaseTest
import cotizador_page as cotizadorpage

class CotizadorTests(BaseTest):

    def test_models_loaded_for_brand(self):
        cotizador = cotizadorpage.CotizadorPage(self.driver)
        brand = "Daewoo"
        cotizador.input_brand(brand)
        assert cotizador.models_loaded(), "Los modelos no se cargaron para la marca> %s" % brand



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
