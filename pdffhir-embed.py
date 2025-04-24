import sys
import os
from pypdf import PdfReader, PdfWriter

if len(sys.argv) != 3 or (len(sys.argv)==2 and sys.argv[1] == '--help'):
  print("Usage: pdfhir-embed.py PDFFILE FHIRBUNDLE")

infile = sys.argv[1]
fhirfile = sys.argv[2]

reader = PdfReader(infile)
writer = PdfWriter()

writer.append_pages_from_reader(reader);

with open(fhirfile, "rt") as file:
  writer.add_attachment("fhir-bundle"+os.path.splitext(fhirfile)[1], file.read())

with open("fhir+"+infile, "wb") as file:
  writer.write(file)


