import unittest
import pyperclip
from contact import Contact

class TestContact(unittest.TestCase):
    def setUp(self):

        self.new_contact = Contact("james", "Muriuki","0712345678","james@ms.com")

    def tearDown(self):

        '''
            tearDown method that does clean up after each test case has run.
            '''
        Contact.contact_list = []


    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_contact.first_name,"james")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"james@ms.com")

    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_multiple_contact(self):

        '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact(self):

        '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com")
        test_contact.save_contact()

        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_find_contact_by_number(self):

        '''
        test to check if we can find a contact by phone number and display information
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com")
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711223344")

        self.assertEqual(found_contact.email,test_contact.email)

    def test_contact_exist(self):

        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()

        contact_exists = Contact.contact_exist("0711223344")

        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Contact.display_contacts(),Contact.contact_list)



if __name__ == "__main__":
    unittest.main()