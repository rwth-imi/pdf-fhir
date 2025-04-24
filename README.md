# pdf-fhir
Integrate structured machine readable medical data into PDF reports by embedding HL7 FHIR resources in PDF files



Embedded content for PDF files are specified 
in section 7.11.4 "Embedded File Streams" of the PDF standard.
See "Document management - Portable document format. Adobe. 2008, 
https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf


# Usage

For a simple example and simple python implementation, see the folder `example`.

The generals python scripts can be used as follows:
```
# Embed FHIR bundle into PDF document
cd example
python ../pdffhir-embed.py RD_john_muller-original.pdf fhir-bundle.xml
```


