import sys
from pypdf import PdfReader

# output usage if incorrectly used
if len(sys.argv) < 2 or sys.argv[1] == '--help':
  print("Usage: pdfhir-extract.py PDFFILE")
  sys.exit(2)

pdfinput = sys.argv[1]
reader = PdfReader(pdfinput)

extracted = False

# loop through attachments to find & extract HL7 FHIR bundle files
for attachment in reader.attachment_list:
  if attachment.name == "fhir-bundle.json" or attachment.name == "fhir-bundle.xml":
    extracted = True
    with open(f"{pdfinput}_{attachment.name}","wb") as file:
      file.write(attachment.content)

# exit with error code 1 if no FHIR attachmemts were found
if extracted != True:
  print("No embedded file fhir-bundle.json/xml found.", file=sys.stderr)
  sys.exit(1)  
