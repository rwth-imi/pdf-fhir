import sys
from pypdf import PdfReader

reader = PdfReader("RD_john_muller-fhir.pdf")

# loop through attachments to find & extract HL7 FHIR bundle files
if "fhir-bundle.xml" in reader.attachments.keys():
    with open("extracted_fhir-bundle.json","wb") as file:
      a = reader.attachments["fhir-bundle.xml"]
      file.write(a[0])
