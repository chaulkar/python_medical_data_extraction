from backend.src.parser_patient_details import PatientDetailsParser
import pytest

@pytest.fixture()
def doc1_kathy():
    document_text = '''
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
    return PatientDetailsParser(document_text)

@pytest.fixture()
def doc2_jerry():
    document_text = '''
Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A

7?
v

17/12/2020


_—

Name of Insurance Company:
Random Insuarance Company

Policy Number:
5638746258

Do you have medical insurance?

_ Yes

Medical Insurance Details

List any allergies:
N/A

List any medication taken regularly:

N/A

4218 Smeeler Ridge Dr
Buffalo, New York, 14206
United States

Expiry Date:
31 December 2020
'''
    return PatientDetailsParser(document_text)

def test_get_patient_name(doc1_kathy, doc2_jerry):
    assert doc1_kathy.get_field("patient_name") == "Kathy Crawford"
    assert doc2_jerry.get_field("patient_name") == "Jerry Lucas"

def test_get_phone_number(doc1_kathy, doc2_jerry):
    assert doc1_kathy.get_field("phone_number") == "(737) 988-0851"
    assert doc2_jerry.get_field("phone_number") == "(279) 920-8204"

def test_get_medical_problems(doc1_kathy, doc2_jerry):
    assert doc1_kathy.get_field("medical_problems") == "Migraine"
    assert doc2_jerry.get_field("medical_problems") == "N/A"

def test_get_hepatitis_b_vaccination(doc1_kathy, doc2_jerry):
    assert doc1_kathy.get_field("hepatitis_b_vaccination") == "No"
    assert doc2_jerry.get_field("hepatitis_b_vaccination") == "Yes"
