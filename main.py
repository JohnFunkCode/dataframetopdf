########
# main

import pandas as pd
import numpy as np

x=5
y=3
z=x/y

from Reporting import PDFReportClass as pdf
p=pdf.PDFReport()
pdf.PDFReport.set_title("Hello World")
pdf.PDFReport.set_pageInfo("PlatypusTable2 example")
pdf.PDFReport.set_sourcefile("RegistrantExport_EM0393 Liz 10-19-2016 Clean.csv")

# doc = SimpleDocTemplate("simple_table.pdf", pagesize=landscape(letter))
# docElements = []

#Title = "Hello World"
#pageinfo = "PlatypusTable2 example"
#now = datetime.datetime.now()
#timestamp = now.strftime("%Y-%m-%d %H:%M")


#PAGE_HEIGHT = defaultPageSize[1];
#PAGE_WIDTH = defaultPageSize[0]
#styles = getSampleStyleSheet()

# my data frame
index = ['a', 'b', 'c', 'd']
columns = ['one', 'two', 'three', 'four']
df = pd.DataFrame(np.random.randn(4, 4), index=index, columns=columns)
data = [df.columns[:, ].values.astype(str).tolist()] + df.values.tolist()

# docElements.extend(put_dataframe_on_pdfpage(data, doc, "1", "9:00am", "Boys & Girls Kata", "10-13", "Blue/Blue Green"))
#p.put_dataframe_on_pdfpage(data, "1", "9:00am", "Boys & Girls Kata", "10-13", "Blue/Blue Green")
p.put_dataframe_on_pdfpage(data,"1","9:00am","Boys Kata","10","blue and green")

index = ['a', 'b', 'c', 'd', 'e']
columns = ['one', 'two', 'three', 'four', 'five']
df2 = pd.DataFrame(np.random.randn(5, 5), index=index, columns=columns)
data = [df2.columns[:, ].values.astype(str).tolist()] + df2.values.tolist()

p.put_dataframe_on_pdfpage(data, "1", "9:00am", "Boys & Girls Kata", "10-13", "Blue/Blue Green")

p.write_pdfpage()