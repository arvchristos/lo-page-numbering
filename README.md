![GitHub release](https://img.shields.io/github/release/arvchristos/lo-page-numbering.svg)
![GitHub repo size in bytes](https://img.shields.io/github/repo-size/arvchristos/lo-page-numbering.svg?colorB=fedcba)
![Python version](https://img.shields.io/badge/python-3.5-green.svg)
![GitHub issues](https://img.shields.io/github/issues/arvchristos/lo-page-numbering.svg)

# Page Numbering Addon

This plugin, or by LO/OO terminology add-on(an extension that includes any kind of UI implementation/customization), includes the following features:

![Page numbering addon](https://extensions.libreoffice.org/extensions/page-numbering-addon/@@images/screenshot/large)

## Features
* Add page numbering simplifying the previous page-break approach:

  Although Page Breaks are an intuitive and effective approach for document layout and styling, users migrating from Microsoft Office suites find it more than difficult to understand)

* Configure styling options such as Font, Character height, Alignment and page position (Header/Footer)
* Page offset and First page options
* Numbering type selection such as Roman, Arabic or Greek
* Multiple Page numbering setups per document

## Download
Page Numbering Addon can be found either in this repository or at the following links:
1. [LibreOffice Official Extensions](https://extensions.libreoffice.org/extensions/page-numbering-addon).
2. [Apache OpenOffice Extensions](https://extensions.openoffice.org/en/project/page-numbering-addon)

## Acknowledgments
People that have contributed one way or another for this project are acknowledged at the ACKNOWLEDGEMENTS.md file.

## Implementation
In order to get familiar with LO API a version of the plugin in LO Basic language was implemented. Although this is the most documented among LO/OO compatible languages, it follows an archaic programming approach with little to none modern features. That is the reason that led to the Python port for the official version of the extension.

Page Numbering Addon 0.0.1 was part of the [librecust](https://github.com/eellak/gsoc2018-librecust) GSOC project, suggested by [GFOSS Open Technologies Alliance](https://gfoss.eu/home-posts/). 
Source code will, surely, be available and suggestions, improvements or bug reports will be more than welcome. Any updates will be distributed through the official extension manager.

Future versions will be distributed from the official LO extension site as well as from this repository (LibreOffice/versions/
 directory). 

## Installation
Each implementation (Python/LO Basic) is packaged as an extension in `.oxt` format. The LO Basic version has no dependencies. For the suggested Python version the following are applied:

**Before installing the extension, make sure that the following dependencies are installed**


*In order to use the latest features implemented, you should install the Python version. The LO Basic implementation is not
maintained until a new maintainer is found.*

### Python Dependencies
* libreoffice-script-provider-python package or even better [uno-tools](https://pypi.org/project/unotools/)
* uno-tools required dependencies
  - OpenOffice.org/LibreOffice 3.4 or later
  - Python 3.3 or later

### Warning
In order to avoid unexpected results you are suggested to avoid installing together the two different versions (Basic and Python) of this add-on.

## Contribute 
Extensive info about the development of this extension is provided in the repository [wiki](https://gitlab.com/lo_extensions/lo-page-numbering/wikis/home).

Also, the contributor is suggested to pay a visit to the contributing [guide](https://github.com/arvchristos/lo-page-numbering/blob/master/CONTRIBUTING.md) 

## Discussion
Discussion about the extension as well as suggestions can be issued either at the repo or at the following IRC channel:

[IRC channel](https://riot.im/app/#/room/!pywEKwnnGVkNrbMljv:matrix.org)

Suggestions and ideas are more than welcome. We suggest including them in issues, however personal emails are not discouraged.

### Localization 
Localization guidelines are described in the corresponding [wiki page](https://gitlab.com/lo_extensions/lo-page-numbering/wikis/Localization-tutorial)

However, a localization tool for LO extensions is developed and can be found on the corresponding [repository](https://gitlab.com/lo_extensions/l10n-utility).

## Team 
* Developer: Arvanitis Christos ([@arvchristos](https://github.com/arvchristos))
