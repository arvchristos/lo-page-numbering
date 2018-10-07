Before proceeding, please consider creating a different branch for your contributions (e.g. l10n-locale).

In order to localize Page Numbering Addon, the following steps should be followed:
## UI localization

1. Clone this repository:
   ```bash
   git clone https://gitlab.com/lo_extensions/lo-page-numbering.git 
   ``` 

2. Navigate to base code directory:
    ```bash
    cd ./lo-page-numbering/LibreOffice/python/build_files/python/ 
    ``` 

3. Generate most recent `.pot` template:
    ```bash
    $(locate pygettext.py 2>&1 | head -n 1) -d base -o ./locales/base.pot ./main.py
    ```
    For Windows the previous command will look like:
    ```
    C:\>py -3.4 C:\Python34\Tools\i18n\pygettext.py -d base -o ./locales/base.pot ./main.py
    ```

4. Create new folder for the locale in the directory tree:
	
    ```bash
    mkdir locales/new_locale/LC_MESSAGES
    ```
    ```.
    ├── locales
    │   ├── el
    │   │   └── LC_MESSAGES
    │   │       ├── base.mo
    │   │       └── base.po
    │   ├── en
    │   │   └── LC_MESSAGES
    │   │       ├── base.mo
    │   │       └── base.po
    │   ├── new_locale (e.g. it)
    │   │   └── LC_MESSAGES
    │   └── base.pot
    └── main.py
    ```

5. Fill template and create `.po` file:
    Based on the `.pot` template, fill the `msgstr` fields and then save the file as `base.po` in the `locales/new_locale/LC_MESSAGES/` directory.
    For Windows, as well as Linux, the [Poedit](http://poedit.net/) software can be used. If you decide to use poedit, the *next step can be skipped* because the catalog file is automatically created.

6. Generate locale catalog file:
    ```bash
    cd locales/new_locale/LC_MESSAGES
    $(locate msgfmt.py 2>&1 | head -n 1) -o base.mo base
    ```

7. Submit a pull request with your changes.

For a more detailed tutorial of gettext usage please visit [PhraseApp blog](https://phraseapp.com/blog/posts/translate-python-gnu-gettext/).

## Help pages localization
In order to localize the help pages the following steps should be followed:
1. Clone this repository:
   ```bash
   git clone https://gitlab.com/lo_extensions/lo-page-numbering.git 
   ``` 

2. Navigate to base code directory:
    ```bash
    cd ./lo-page-numbering/LibreOffice/python/build_files/ 
    ```

3. Open *PageNumberingAddonPython.odt* with LibreOffice

4. Navigate to *Help pages for PageNumberingAddonPython* section (Ctrl + Left click from the contents table)

5. Copy the english help pages (Starting from **Help en** and finishing at **/node**) 

6. Navigate to the end of the document (whitespace)

7. Paste the english man pages

8. Edit the text with your locale text (do not forget to change the `Help en` to `Help new_locale`). Do not edit text starting with `Page*`

9. Save the file

10. Submit a pull request with your changes.

## Extension description and legal info localization

### Extension description

1. Navigate to `oxt_metadata/Descriptions` directory 

2. Create new file with the same naming conventions as the existing ones: `descr-locale.txt`

3. Edit and save the newly created file.
 
### Legal text

1. Navigate to `oxt_metadata/Legal` directory 

2. Create new file with the same naming conventions as the existing ones: `license-locale.txt`

3. Edit and save the newly created file.

4. Submit a pull request with your changes.
