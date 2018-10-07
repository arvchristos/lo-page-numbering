# Code Layout

## Indentation
* Use 4 spaces per indentation level.
* Continuation lines should align wrapped elements.
### Reference: [PEP-8 Indentation](https://www.python.org/dev/peps/pep-0008/?#indentation)
## Tabs or spaces
* Spaces are the preferred indentation method.
* Tabs should be used solely to remain consistent with code that is already indented with tabs.
### Reference: [PEP-8 Tabs or Spaces?](https://www.python.org/dev/peps/pep-0008/?#tabs-or-spaces)
## Maximum Line Length
* Limit all lines to a maximum of 79 characters.
* For flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters.
### Reference: [PEP-8 Maximum Line Length](https://www.python.org/dev/peps/pep-0008/?#maximum-line-length)
## Blank lines
* Surround top-level function and class definitions with two blank lines.
* Method definitions inside a class are surrounded by a single blank line.
* Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).
### Reference: [PEP-8 Blank Lines](https://www.python.org/dev/peps/pep-0008/?#blank-lines)
## Imports
* Imports should usually be on separate lines.
* Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
* Imports should be grouped in the following order:
* Standard library imports.
* Related third party imports.
* Local application/library specific imports.
### Reference: [PEP-8 Imports](https://www.python.org/dev/peps/pep-0008/?#imports)
# String Quotes

* Please use double-quoted strings
### Reference: [PEP-8 String Quotes](https://www.python.org/dev/peps/pep-0008/?#string-quotes)
# Whitespace in Expressions and Statements

Avoid extraneous whitespace in the following situations:

* Immediately inside parentheses, brackets or braces.

    Yes: `spam(ham[1], {eggs: 2})`  
    No:  `spam( ham[ 1 ], { eggs: 2 } )`
* Between a trailing comma and a following close parenthesis.

    Yes: `foo = (0,)`  
    No:  `bar = (0, )`
* Immediately before a comma, semicolon, or colon:

    Yes: `if x == 4: print x, y; x, y = y, x`  
    No:  `if x == 4 : print x , y ; x , y = y , x`
### Reference: [PEP-8 Whitespace in Expressions and Statements](https://www.python.org/dev/peps/pep-0008/?#whitespace-in-expressions-and-statements)
# Comments

* Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).
* Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period.
* You should use two spaces after a sentence-ending period in multi- sentence comments, except after the final sentence.
## Block comments
* Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).
* Paragraphs inside a block comment are separated by a line containing a single #.
## Inline comments
* An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.
Reference: [PEP-8 Comments](https://www.python.org/dev/peps/pep-0008/?#comments)
## Documentation strings
* Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.
* Note that most importantly, the """ that ends a multiline docstring should be on a line by itself:
  `"""Return a foobang`
  `Optional plotz says to frobnicate the bizbaz first.`
  `"""`
* For one liner docstrings, please keep the closing """ on the same line.
### Reference: [PEP-8 Documentation strings](https://www.python.org/dev/peps/pep-0008/?#documentation-strings)
# Naming Conventions
## Names to avoid
* Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
* In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.
## Method Names and Instance Variables
* Please use CamelCase
### Reference: [PEP-8 Naming Conventions](https://www.python.org/dev/peps/pep-0008/?#naming-conventions)
