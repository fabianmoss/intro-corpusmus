import numpy as np 

"""PSEUDOCODE

for ch in chapters:

    citation_keys = [ cit.key for cit in citedpapers ]

    chapter_sum = []
    for k in citation_keys:
        
        page_sum = p2 - p1 for (p1,p2) in k.pages.split("--") # better with re because sometimes "-" and "--"
        chapter_sum.append(page_sum)

    chapter_sum = sum(chapter_sum)
    
    print(f"{chapter_sum} pages to read in chapter {ch}.")

"""