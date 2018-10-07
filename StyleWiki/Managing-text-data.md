
In order to apply text changes and traverse text data, the main iterators used by LibreOffice/OpenOffice are named cursors, in correspondence to the UI cursors in text editing.

For this addon, two kinds of cursors are used:
* [View Cursor](https://github.com/eellak/gsoc2018-librecust/wiki/Managing-text-data#view-cursors), [official wiki](https://wiki.openoffice.org/wiki/Writer/API/View_cursor)
* [Text Cursor](https://github.com/eellak/gsoc2018-librecust/wiki/Managing-text-data#text-cursors)


## View Cursors
A view cursor, in terms of LO/OO API, is used to move across the page layout. This cursor is equivalent to the cursor shown in the UI. For this purpose, only one View cursor is instantiated in scripts, as one cursor is shown to the user while editing a document. We use View cursors to change page properties, while moving across pages, adding manual page breaks and altering page styles. 

View cursor reference in Basic and Python:
### Basic
```vb
    ViewCursor = Doc.CurrentController.getViewCursor()
```
### Python
```python
    Doc = XSCRIPTCONTEXT.getDocument()
    ViewCursor = Doc.CurrentController.getViewCursor()
```
There is a variety of View cursors in LO API, which, mainly because of the abstraction layer of Basic and Python, provides methods accessible through the getViewCursor() method [1]


| Interface     | Description   |
| com.sun.star.text.XTextCursor | The primary text cursor that defines simple movement methods |
| com.sun.star.text.XWordCursor | Provides word-related movement and testing methods |
| com.sun.star.text.XSentenceCursor | Provides sentence-related movement and testing methods |
| com.sun.star.text.XParagraphCursor | Provides paragraph-related movement and testing methods |
| com.sun.star.text.XTextViewCursor | Derived from XTextCursor, this describes a cursor in a text document’s view |

Getting a text cursor requires the acquisition of ViewCursor

`oCursor = ViewCursor.getText().createTextCursorByRange(ViewCursor)`

However, page styles provide specific text ranges for Header and Footer locations, a feature used in Page Numbering Addon:

```python
#Header text
 Num_Position = NumberedPage.HeaderText

#Footer text
Num_Position = NumberedPage.FooterText
```
After getting the required text range, a text cursor for data interaction is acquired:
`NumCursor = Num_Position.Text.createTextCursor()`

## Inserting content
Num_Position object implements the [XText](https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XText.html)  interface, allowing for text content insertion/deletion using specific methods. As far as Page Numbering Addon is concerned, these methods are used as following:

### Basic
```vb
‘ NumberingDecorationComboBox is a dialog element that provides a decoration string value.
‘ PageNumber is a specific field that represents page numbering LO struct. 

    Select Case NumberingDecorationComboBox.Text
        Case "#"
            Num_Position.insertTextContent(NumCursor, PageNumber, False)
        Case "-#-"
            Num_Position.insertString(NumCursor, "-", False)
            Num_Position.insertTextContent(NumCursor, PageNumber, False)
            Num_Position.insertString(NumCursor, "-", False)
        Case "[#]"
            Num_Position.insertString(NumCursor, "[", False)
            Num_Position.insertTextContent(NumCursor, PageNumber, False)
            Num_Position.insertString(NumCursor, "]", False)
        Case "(#)"
            Num_Position.insertString(NumCursor, "(", False)
            Num_Position.insertTextContent(NumCursor, PageNumber, False)
            Num_Position.insertString(NumCursor, ")", False)
        Case Else
            Print "Custom decoration unimplemented feature"
    End Select
```
### Python
```python
# NumberingDecorationComboBoxText object is a dialog control that provides decoration option
NumberingDecorationComboBoxText = oDialog1Model.getByName(
        "NumberingDecoration").Text

    if NumberingDecorationComboBoxText == "#":
        Num_Position.insertTextContent(NumCursor, PageNumber, False)
    elif NumberingDecorationComboBoxText == "-#-":
        Num_Position.insertString(NumCursor, "-", False)
        Num_Position.insertTextContent(NumCursor, PageNumber, False)
        Num_Position.insertString(NumCursor, "-", False)
    elif NumberingDecorationComboBoxText == "[#]":
        Num_Position.insertString(NumCursor, "[", False)
        Num_Position.insertTextContent(NumCursor, PageNumber, False)
        Num_Position.insertString(NumCursor, "]", False)
    elif NumberingDecorationComboBoxText == "(#)":
        Num_Position.insertString(NumCursor, "(", False)
        Num_Position.insertTextContent(NumCursor, PageNumber, False)
        Num_Position.insertString(NumCursor, ")", False)
    else:
        raise Exception("Custom decoration unimplemented feature")
```

More on Cursors on Andrew Pitonyak ’s [OpenOffice.org Macros Explained](http://www.pitonyak.org/book/) book 

[1] Andrew Pitonyak ’s [OpenOffice.org Macros Explained](http://www.pitonyak.org/book/) book
