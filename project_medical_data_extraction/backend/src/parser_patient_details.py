import re
from backend.src.parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            "patient_name": self.get_field("patient_name"),
            "phone_number": self.get_field("phone_number"),
            "medical_problems": self.get_field("medical_problems"),
            "hepatitis_b_vaccination": self.get_field("hepatitis_b_vaccination")
        }


    def get_field(self, field):
        pattern_dic = {
            "patient_name": r"Date\n*(.*)\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b",
            "phone_number": r"(.*)Weight",
            "medical_problems": r"Medical.Problems.*\n*(.*)",
            "hepatitis_b_vaccination": r"vaccination\?\n*.*(Yes|No)"
        }

        pattern = pattern_dic.get(field)
        if pattern:
            matches = re.findall(pattern, self.text)
            if len(matches) > 0:
                return matches[0].strip()







if __name__ == "__main__":
    document_text='''
17/12/2020

Patient Medical Record

Patient Information Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight’
9264 Ash Dr 95
New York City, 10005 .
United States Height:
190
In Casc of Emergency
7 ee
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone

Genera! Medical History

a

a

a ea A CE i a

Chicken Pox (Varicella): Measies:

IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?
No

List any Medical Problems (asthma, seizures, headaches}:

Migraine

CO
aa

.

‘Name of Insurance Company:

Random Insuarance Company - 4789 Bollinger Rd
Jersey City, New Jersey, 07030

a Policy Number:
ra 1520731 3 Expiry Date:

. 30 December 2020
Do you have medical insurance?

Yes:

Medical Insurance Details

List any allergies:

Peanuts

List any medication taken regularly:
Triptans'''

    pp= PatientDetailsParser(document_text)
    print(pp.parse())