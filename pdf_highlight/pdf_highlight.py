import fitz     
# opening the pdf file  
my_pdf = fitz.open("sample.pdf")      
# input text to be highlighted  
my_text = "demonstration"    
# iterating through pages for highlighting the input phrase  
for n_page in my_pdf:  
    matchWords = n_page.search_for(my_text)      
    for word in matchWords:  
        my_highlight = n_page.add_highlight_annot(word)  
        my_highlight.update()     
# saving the pdf file as highlighted.pdf  
my_pdf.save("highlighted_text.pdf")  