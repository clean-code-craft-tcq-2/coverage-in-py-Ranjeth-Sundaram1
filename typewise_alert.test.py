import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    def test_Generate_email_content_for_low(self):
        self.assertTrue(typewise_alert.Generate_email_content('TOO_LOW', typewise_alert.email_info['messages']) == 'Hi, the temperature is too low')
    def test_Generate_email_content_for_high(self):
        self.assertTrue(typewise_alert.Generate_email_content('TOO_HIGH', typewise_alert.email_info['messages']) == 'Hi, the temperature is too high')
    def test_DefineCoolingtype_limits_for_PASSIVE_COOLING(self):
        self.assertTrue(typewise_alert.DefineCoolingtype_limits('PASSIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 35})
    def test_DefineCoolingtype_limits_for_HI_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.DefineCoolingtype_limits('HI_ACTIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 45})
    def test_DefineCoolingtype_limits_for_MED_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.DefineCoolingtype_limits('MED_ACTIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 40})
    def test_DefineCoolingtype_limits_for_Wrong_key(self):
        self.assertTrue(typewise_alert.DefineCoolingtype_limits('WRONG_KEY') == {"lowerLimit" : 'NA', "upperLimit" : 'NA'})

if __name__ == '__main__':
  unittest.main()
