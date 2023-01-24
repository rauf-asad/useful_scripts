import pikepdf

# Open the first PDF document
pdf1 = pikepdf.open("document1.pdf")

# Open the second PDF document
pdf2 = pikepdf.open("document2.pdf")

# Add all the pages from the second PDF to the first PDF
pdf1.pages.extend(pdf2.pages)

# Save the resulting PDF
pdf1.save("merged_document.pdf")

# Close the PDFs
pdf1.close()
pdf2.close()
