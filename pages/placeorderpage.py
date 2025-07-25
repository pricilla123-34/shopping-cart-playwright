

class PlaceOrderPage:

    """
    Page object for the place order page.
    """

    def __init__(self, page):

        self.page = page
        self._Fname = page.get_by_placeholder("First Name")
        self._Lname = page.get_by_placeholder("Last Name")
        self._postal_code = page.get_by_placeholder("Postal Code")
        self._continue_button = page.get_by_role("button", name="Continue")
        self._confirm_message = page.get_by_text("Thank you for your order!")
        self._finish_button = page.get_by_role("button", name="Finish")

        
    def enter_shipping_info(self, first_name, last_name, postal_code):
        """
        Enters shipping information into the respective fields.
        """

        self._Fname.fill(first_name)
        self._Lname.fill(last_name)
        self._postal_code.fill(postal_code)

    def click_continue(self):
        """
        Clicks the 'Continue' button to proceed with the order.
        """
    
        self._continue_button.click()


    def click_finish(self):
        """
        Clicks the 'Finish' button to complete the order.
        """
        self._finish_button.click()



    def get_confirmation_message(self):
        """
        Returns the confirmation message displayed after the order is placed.
        """
        return self._confirm_message


