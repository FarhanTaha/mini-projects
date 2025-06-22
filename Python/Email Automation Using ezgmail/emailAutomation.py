# Email Automation Using Python

import ezgmail , os 

# Making sure the current working directory is set to where our .py file is located
os.chdir(r'E:\Programming\pythonWorkSpace\Python_Bootcamp_HDNB\10B1-C7')
ezgmail.init() # 🌐 Authorize your Gmail account in browser


# Sending First email
ezgmail.send('farhanmubasshirtahaltd@gmail.com', 
             'Test Email', 
             'This is a test email sent using ezgmail library.\nFirst Automation Test')

# Sending Second email
ezgmail.send(
    'farhanmubasshirtahaltd@gmail.com',
    'Hello Automation World',
    'Second Automation Test',
    ['SolvedCode.png']  # or 'SolvedCode.py' or full path if needed
)

# Sending Third email with CC and BCC
ezgmail.send('mubasshirtaha.business@gmail.com' , 
             'CC and BCC Test', 
             'Third Automation Test',
             cc='farhanmubasshirtahaltd@gmail.com',
             bcc= 'farhanmubasshirtaha816@gmail.com')

