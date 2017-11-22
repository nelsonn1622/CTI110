#CTI-110
#NajahN
#Mr. Norris
#oct 2

#ask user for a string
tag = input("enter the tag: ")


#definition of the tag
tagParagraph = "p"
tagHeader = "h1"
tagBold = "b"
tagDivide = "div"


#give definition of tag
if tag == tagParagraph:
    print("This means paragraph")
    print("example: <p>text</p>")
elif tag == tagHeader:
    print("This means header")
    print("example: <h1>This is a heading</h1>")
elif tag == tagBold:
    print("This bolds the text")
    print("example: <b>bolds the text</b>")
elif tag == tagDivide:
    print("This takes a section of the HTML document and define  it")
    print("example: <div> this section of the document</div>")
          


