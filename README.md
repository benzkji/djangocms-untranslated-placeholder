# djangocms-untranslated-placeholder

[![CI](https://github.com/bnzk/djangocms-untranslated-placeholder/actions/workflows/ci.yml/badge.svg)](https://github.com/bnzk/djangocms-untranslated-placeholder/actions/workflows/ci.yml)
[![Version](https://img.shields.io/pypi/v/djangocms-untranslated-placeholder.svg?style=flat-square "Version")](https://pypi.python.org/pypi/djangocms-untranslated-placeholder/)
[![Licence](https://img.shields.io/github/license/bnzk/djangocms-untranslated-placeholder.svg?style=flat-square "Licence")](https://pypi.python.org/pypi/djangocms-untranslated-placeholder/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/djangocms-untranslated-placeholder?style=flat-square "PyPi Downloads")](https://pypistats.org/packages/djangocms-untranslated-placeholder)

Untranslated placeholder (one language only) for django-cms 4.1+.


## Features

Placeholders will be filled in one (you define which one) language only.

## Why

Placeholder structure will be shared across languages. Enabling a big 
efficiency boost for editors, when managing multiple languages.

## Installation & Usage

To get the latest stable release from PyPi

    pip install djangocms-untranslated-placeholder  # not yet!

Add ``djangocms_untranslated_placeholder`` to your ``INSTALLED_APPS``

    INSTALLED_APPS = (
        ...,
        'djangocms_untranslated_placeholder',
    )

### Important

Plugins must provide the language specific contents - this has been done with django-modeltranslation in the wild,
other methods (django-parler, etc.) should work as well.

### Howto

`UNTRANSLATED_PLACEHOLDER = True` or `UNTRANSLATED_PLACEHOLDER = 'lang_code'` is required to enable 
untranslated placeholder mode. If you don't specify your default language explicitly, `settings.LANGUAGE_CODE`
will be used.


## Development


### Getting started

- there is test app, available with `./manage.py runserver`.
- to run tests: ./manage.py test
- to run tests with django 1.8 / 1.9 / 1.10 / 1.11: `tox`


### Contributions

If you want to contribute to this project, please perform the following steps

    # Fork this repository
    # Clone your fork
    mkvirtualenv djangocms-untranslated-placeholder
    pip install -r requirements_dev.txt
    git checkout -b feature_branch
    # Implement your feature and tests
    git add . && git commit
    tox
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
