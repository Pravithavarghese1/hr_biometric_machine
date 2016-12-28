# hr_biometric_machine
Biometric Machine/Fingerprint Machine Integration with Odoo

INITIAL REQUIREMENTS:

Install  Python ZKLib

      Download from https://pypi.python.org/pypi/zklib/0.1.1
      or 
      sudo easy_install zklib 
      or
      sudo pip install zklib

Install hr_biometric_machine

BIOMETRIC MACHINE CONFIGURATION:

Goto Employees --> Biometric Device Manager --> Attendance Machine

      field_name: name
      input_value: 192.168.0.201

      field_name: port
      input_value: 4370

      field_name: ref_name
      input_value: write your location where biometric device is installed

