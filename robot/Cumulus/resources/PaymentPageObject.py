from cumulusci.robotframework.pageobjects import DetailPage
from cumulusci.robotframework.pageobjects import pageobject
from BaseObjects import BaseNPSPPage
from NPSP import npsp_lex_locators

@pageobject("Details", "npe01__OppPayment__c")
class PaymentPage(BaseNPSPPage, DetailPage):
    object_name = "npe01__OppPayment__c"
    
    def _is_current_page(self):
        """ Verify we are on the payment details page
            by verifying that the url contains '/view'
        """
        self.selenium.wait_until_location_contains("/lightning/r/npe01__OppPayment__c",message="Current page is not a payment detail view")
        self.selenium.wait_until_page_contains("Check/Reference Number",timeout=60)
    
    
    def verify_payment_allocations(self, **kwargs):
       """To verify allocations, header is related list
          key is value in td element, value is value in th element     
       """
       self.salesforce.load_related_list("Payment Allocations")
       for key, value in kwargs.items():
           locator = npsp_lex_locators['payments']['allocations'].format("Payment Allocations",key)
           ele = self.selenium.get_webelement(locator).text
           assert ele == value, "Expected {} allocation to be {} but found {}".format(key,value,ele)
        