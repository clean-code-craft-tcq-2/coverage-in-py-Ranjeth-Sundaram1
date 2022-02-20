import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    def test_Generate_email_content_for_low(self):
        self.assertTrue(typewise_alert.Generate_email_content('TOO_LOW', typewise_alert.email_info['messages']) == 'Hi, the temperature is too low')
    def test_Generate_email_content_for_high(self):
        self.assertTrue(typewise_alert.Generate_email_content('TOO_HIGH', typewise_alert.email_info['messages']) == 'Hi, the temperature is too high')

if __name__ == '__main__':
  unittest.main()
