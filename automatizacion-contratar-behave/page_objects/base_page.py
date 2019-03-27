from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

_DEFAULT_TIMEOUT = 100


class BasePage:
    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.base_url = base_url
        self.timeout = _DEFAULT_TIMEOUT
        self.wait = WebDriverWait(self.driver, _DEFAULT_TIMEOUT)

    def find_element(self, locator):
        """
        Encuentra el elemento definido por locator y ademas lo espera
        :param locator: el locator del elemento a encontrar
        :return: un tipo Element
        """
        self.wait_for_element(locator)
        return self.driver.find_element(*locator.ret_locator)

    def find_elements(self, locator):
        """
        Encuentra los elementos definidos por locator
        :param locator: el locator de los elementos a encontrar
        :return: una lista con Elements encontrados
        """
        return self.driver.find_elements(*locator.ret_locator)

    def find_select(self, locator):
        """
        Encuentra el select definido por locator
        :param locator: el locator del select a encontrar
        :return: un elemento de tipo Select
        """
        return Select(self.driver.find_element(*locator.ret_locator))

    def wait_for_element(self, locator):
        """
        Espera que el elemento este visible y habilitado
        :param locator: el locator del elemento a esperar
        :return: un WebDriverWait del elemento
        """
        self.wait.until(ec.presence_of_element_located(locator.ret_locator))
        return self.wait.until(ec.element_to_be_clickable(locator.ret_locator))

    def wait_for_element_invisibility(self, locator):
        """
        Espera que el elemento definido por locator este invisible
        :param locator: el locator del elemento a esperar que no sea visible
        :return: un WebDriverWait del elemento
        """
        return self.wait.until(ec.invisibility_of_element_located(locator.ret_locator))

    def wait_for_element_visibility(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator.ret_locator), "Tiempo de espera excedido.")

    def wait_until_element_clickable(self, locator, timeout=_DEFAULT_TIMEOUT):
        """
        Waits until an element is clickable.

        :param locator: locator for the element to wait for.
        :param timeout: max seconds to wait for the element to be clickable.
        :return: Element.
        :raises:
        """
        return self.wait.until(ec.element_to_be_clickable(locator.ret_locator))

    @property
    def title(self):
        """
        Devuelve el titulo de la pantalla
        :return: string
        """
        return self.driver.title

    @property
    def url(self):
        """
        Devuelve la url actual de la pantalla
        :return: string
        """
        return self.driver.current_url

    def switch_to_alert_and_accept_it(self):
        """
        Espera que se presente un alert y luego lo acepta, bajo la opcion considerada como aceptar
        :return: un handler para el accept
        """
        return self.wait.until(ec.alert_is_present()).accept()

    def wait_and_switch_to_frame(self, locator):
        """
        Espera la presencia de un frame y cambia el contexto hacia un frame (frame, iframe). Solo espera la presencia
        del frame, no de su contenido (hacer waits adicionales para el contenido)
        :param locator: locator del frame
        :return: handler del frame
        """
        return self.wait.until(ec.frame_to_be_available_and_switch_to_it(locator.ret_locator))

    def switch_to_default_context(self):
        """
        Cambia el contexto al por defecto
        :return: handler del contexto
        """
        return self.driver.switch_to.default_content()

    # def wait_for_any_text(self, locator):
    #     return self.wait.until(lambda driver: self.find_element(locator.ret_locator).get_attribute("value") != "")

    def wait_for_text(self, locator, text):
        """
        Espera el texto definido por text, en el locator descrito. Espera a los de la forma: <TagHtml>Texto</TagHtml>
        en ese ejemplo encontraría "Texto"
        :param locator: el locator del elemento a esperar su texto
        :param text: texto a comparar con el del elemento
        :return: nada xD
        """
        return self.wait.until(ec.text_to_be_present_in_element(locator.ret_locator, text))

    def wait_for_text_in_value(self, locator, text):
        """
        Espera el texto definido por text, en el locator descrito. Espera a los de la forma:
        <TagHtml value="textoValue"></TagHtml> . En ese ejemplo encontraria "textoValue"
        :param locator: locator del elemento a esperar su texto en value
        :param text: texto a comparar con el del elemento
        :return: nada
        """
        return self.wait.until(ec.text_to_be_present_in_element_value(locator.ret_locator, text))

    def wait_for_staleness(self, locator):
        # PROTOTIPO, PUEDE CAMBIAR
        """
        Espera que el elemento definido por locator no este presente en el DOM
        :param locator: locator del elemento
        :return: nada
        """
        return self.wait.until(ec.staleness_of(locator.ret_locator))

    def maximize_window(self):
        """
        Maximize the window.

        """
        self.driver.maximize_window()


class Locator:
    def __init__(self, by, name):
        self._by = by
        self._name = name

    @property
    def ret_locator(self):
        return self._by, self._name
