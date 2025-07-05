import re
from backend.src.parser_generic import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            "patient_name": self.get_field("patient_name"),
            "patient_address": self.get_field("patient_address"),
            "medicines": self.get_field("medicines"),
            "directions": self.get_field("directions"),
            "refill": self.get_field("refill")
        }

    def get_field(self, field_name):
        pattern_dict = {
            "patient_name": {"pattern": r"Name:(.*)Date:", "flags": 0},
            "patient_address": {"pattern": r"Address:(.*)\n", "flags": 0},
            "medicines": {"pattern": r"Address[^\n]*(.*)Directions", "flags": re.DOTALL},
            "directions": {"pattern": r"Directions:(.*)Refill", "flags": re.DOTALL},
            "refill": {"pattern":  r"Refill:(.*)times", "flags": 0}
        }
        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object["pattern"], self.text, flags=pattern_object["flags"])
            if len(matches) > 0:
                return matches[0].strip()



if __name__ == "__main__":
    document_text = '''
Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC



Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mig every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''
    pp = PrescriptionParser(document_text)
    print(pp.parse())
