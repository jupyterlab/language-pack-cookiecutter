# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import sys

from babel import Locale

locale = "{{ cookiecutter.locale }}"
locale_underscore = "{{ cookiecutter.locale_underscore }}"


try:
    babel_locale = Locale.parse(locale_underscore)
    parsed_locale = babel_locale.language + "_" + babel_locale.territory
    if parsed_locale != locale_underscore:
        print("ERROR: Locale \"{0}\" is invalid!".format(locale))
        sys.exit(1)
except Exception:
    print("ERROR: Locale \"{0}\" is invalid!".format(locale))
    sys.exit(1)


if "_" in locale:
    print("ERROR: Locales with language variants must use `-` and not `_`")
    sys.exit(1)


if "-" in locale_underscore:
    print("ERROR: `locale_underscore` must use `_` and not `-`")
    sys.exit(1)
