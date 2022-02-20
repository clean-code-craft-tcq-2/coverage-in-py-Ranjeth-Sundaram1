email_info = { 'recepient' : 'a.b@c.com',
               'messages'  : {'TOO_LOW' : 'Hi, the temperature is too low',
                              'TOO_HIGH' : 'Hi, the temperature is too high'
                            }
                }

def DefineCoolingtype_limits(coolingType):    
    coolingtype_limits = { 'PASSIVE_COOLING' : {"lowerLimit" : 0, "upperLimit" : 35},
                          'HI_ACTIVE_COOLING' : {"lowerLimit" : 0, "upperLimit" : 45},
                          'MED_ACTIVE_COOLING' : {"lowerLimit" : 0, "upperLimit" : 40}
    }
    if coolingType in coolingtype_limits.keys():
        return(coolingtype_limits[coolingType])
    else:
        return({"lowerLimit" : 'NA', "upperLimit" : 'NA'})

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
    limits  = DefineCoolingtype_limits(coolingType)
    if 'NA' not in limits.values():
        return infer_breach(temperatureInC, limits['lowerLimit'], limits['upperLimit'])
    else: 
        return "Invalid cooling type"

def IsbatteryCharValid(batteryChar):
    batteryChar_types = ['PASSIVE_COOLING', 'HI_ACTIVE_COOLING', 'MED_ACTIVE_COOLING']
    if batteryChar in batteryChar_types:
        return True
    return False

def check_and_alert(alertTarget, batteryChar, temperatureInC):
    breachType =  classify_temperature_breach(batteryChar, temperatureInC) if IsbatteryCharValid(batteryChar) else False
    alert_status, breachType = alertTarget(breachType),  breachType if breachType else False, 'Invalid Param'
    return((alert_status, breachType))

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')

def Generate_email_content(breachtype, email_messages):
    return email_messages[breachtype]

def send_to_email(breachType):
    mail_content = Generate_email_content(breachType, email_info['messages'])
    sent_email = f"To: {email_info['recepient']} : {mail_content}"
    print(sent_email)
    return(sent_email)
