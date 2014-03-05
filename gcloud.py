#!/usr/bin/env python3

# Copyright (C) 2014 LiuLang <gsushzhsosgsu@gmail.com>
# Use of this source code is governed by GPLv3 license that can be found
# in http://www.gnu.org/licenses/gpl-3.0.html

import sys

from gcloud.App import App


def main():
    app = App()
    app.run(sys.argv)

if __name__ == '__main__':
    main()
