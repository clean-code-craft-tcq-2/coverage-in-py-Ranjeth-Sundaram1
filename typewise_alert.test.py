import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    def test_Generate_email_content_for_low(self):
        self.assertTrue(typewise_alert.Generate_email_content('TOO_LOW', typewise_alert.email_info['messages']) == 'Hi, the temperature is too low')
    def test_Generate_email_content_for_high(self):
        self.assertTrue(typewise_alert.Generate_email_content('TOO_HIGH', typewise_alert.email_info['messages']) == 'Hi, the temperature is too high')
    def test_send_to_email_for_TOO_LOW(self):
        self.assertTrue(typewise_alert.send_to_email('TOO_LOW')== 'To: a.b@c.com : Hi, the temperature is too low')
    def test_send_to_email_for_TOO_HIGH(self):
        self.assertTrue(typewise_alert.send_to_email('TOO_HIGH')== 'To: a.b@c.com : Hi, the temperature is too high')
    def test_send_to_controller_for_TOO_LOW(self):
        self.assertTrue(typewise_alert.send_to_controller('TOO_LOW') == f'{0xfeed}, TOO_LOW')
    def test_send_to_controller_for_TOO_HIGH(self):
        self.assertTrue(typewise_alert.send_to_controller('TOO_HIGH') == f'{0xfeed}, TOO_HIGH')    
    def test_DefineCoolingtype_limits_for_PASSIVE_COOLING(self):
        self.assertTrue(typewise_alert.DefineCoolingtype_limits('PASSIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 35})
    def test_DefineCoolingtype_limits_for_HI_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.DefineCoolingtype_limits('HI_ACTIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 45})
    def test_DefineCoolingtype_limits_for_MED_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.DefineCoolingtype_limits('MED_ACTIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 40})
    def test_DefineCoolingtype_limits_for_WRONG_KEY(self):
        self.assertTrue(typewise_alert.DefineCoolingtype_limits('WRONG_KEY') == {"lowerLimit" : 'NA', "upperLimit" : 'NA'})
    def test_classify_temperature_breach_for_NORMAL(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 38)=='NORMAL')
    def test_classify_temperature_breach_for_TOO_LOW(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -30)=='TOO_LOW')   
    def test_classify_temperature_breach_for_TOO_HIGH(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 50)=='TOO_HIGH')
    def test_classify_temperature_breach_for_WRONG_PARAM(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('WRONG_COOLING', 30)=='Invalid cooling type')
    def test_check_and_alert_for_NORMAL(self):
        self.assertTrue(typewise_alert.check_and_alert(typewise_alert.send_to_controller, 'PASSIVE_COOLING', 30) == "NORMAL")
    def test_check_and_alert_for_TOO_LOW(self):
        self.assertTrue(typewise_alert.check_and_alert(typewise_alert.send_to_email, 'PASSIVE_COOLING', -30) == "TOO_LOW")
    def test_check_and_alert_for_TOO_HIGH(self):
        self.assertTrue(typewise_alert.check_and_alert(typewise_alert.send_to_controller, 'PASSIVE_COOLING', 50) == "TOO_HIGH")
    def test_check_and_alert_for_WRONG_PARAM(self):
        self.assertTrue(typewise_alert.check_and_alert(typewise_alert.send_to_controller, 'WRONG_COOLING', -30) == "Invalid_Param")
        
if __name__ == '__main__':
  unittest.main()
