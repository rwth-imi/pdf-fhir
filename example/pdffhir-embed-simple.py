from pypdf import PdfReader, PdfWriter

reader = PdfReader("RD_john_muller-original.pdf")
writer = PdfWriter()

writer.append_pages_from_reader(reader);

with open("fhir-bundle.xml", "rt") as file:
  writer.add_attachment("fhir-bundle.xml", file.read())

with open("RD_john_muller-fhir.pdf", "wb") as file:
  writer.write(file)


