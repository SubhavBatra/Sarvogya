from pdfquery import PDFQuery

def extract_pdf(query):
    pdf = PDFQuery(query)

    pdf.load()

    # pdf.tree.write("Puranjay.xml", pretty_print=True, encoding='utf-8')

    name = pdf.pq('LTTextLineHorizontal:in_bbox("91.112, 784.766, 185.927, 793.385")').text()
    name = name.split(' ')[0:3]
    name = ' '.join(name)

    age = pdf.pq('LTTextLineHorizontal:in_bbox("369.375, 773.439, 404.833, 782.057")').text()
    age = age.split(' ')[0:1]
    age = ' '.join(age)

    gender = pdf.pq('LTTextLineHorizontal:in_bbox("370.36, 762.111, 389.519, 770.73")').text()
    gender = gender.split(' ')[0:1]
    gender = ' '.join(gender)

    hgb = pdf.pq('LTTextLineHorizontal:in_bbox("283.877, 563.789, 305.934, 572.605")').text()
    rbc_count = pdf.pq('LTTextLineHorizontal:in_bbox("283.877, 510.894, 301.032, 519.71")').text()
    tlc = pdf.pq('LTTextLineHorizontal:in_bbox("283.877, 378.658, 301.032, 387.474")').text()
    tpc = pdf.pq('LTTextLineHorizontal:in_bbox("283.877, 161.613, 298.582, 170.429")').text()
    hbA1c = pdf.pq('LTTextLineHorizontal:in_bbox("278.361, 581.322, 290.615, 590.138")').text()
    cholesterol = pdf.pq('LTTextLineHorizontal:in_bbox("272.156, 350.586, 299.114, 359.401")').text()
    glu_fasting = pdf.pq('LTTextLineHorizontal:in_bbox("272.156, 573.146, 294.213, 581.962")').text()
    return [name,age,gender,hgb,rbc_count,tlc,tpc,hbA1c,cholesterol,glu_fasting]

    # print(name)
    # print(age)
    # print(gender)
    # print(hgb)
    # print(rbc_count)
    # print(tlc)
    # print(tpc)
    # print(hbA1c)
    # print(cholesterol)
    # print(glu_fasting)


# query = "Puranjay.pdf"

# extract_pdf(query)