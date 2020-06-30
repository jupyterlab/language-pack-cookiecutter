# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
