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

def GetBreachType(batteryChar, temperatureInC):
    breachType =  classify_temperature_breach(batteryChar, temperatureInC) if IsbatteryCharValid(batteryChar) else False
    return breachType if breachType!=False else 'Invalid_Param'

def check_and_alert(alertTarget, batteryChar, temperatureInC):
    breachType = GetBreachType(batteryChar, temperatureInC)
    alert_status = alertTarget(breachType) if breachType!='Invalid_Param' else False
    return(breachType)

def send_to_controller(breachType):
    header = 0xfeed
    command_to_controller = (f'{header}, {breachType}')
    print(command_to_controller)
    return(command_to_controller)

def Generate_email_content(breachtype, email_messages):
    return email_messages[breachtype]

def send_to_email(breachType):
    mail_content = Generate_email_content(breachType, email_info['messages'])
    sent_email = f"To: {email_info['recepient']} : {mail_content}"
    print(sent_email)
    return(sent_email)
