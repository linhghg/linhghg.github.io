#!/usr/bin/env python

import shutil;
import os.path;

cv_pdf  = "../../pandoc_resume/cv.pdf";
cv_html = "../../pandoc_resume/cv.html";

dst_pdf = ".";
dst_html = ".";

if (os.path.isfile(cv_pdf)):
    shutil.copy(cv_pdf, dst_pdf);
else:
    print("ERROR: cannot find "+cv_pdf+" ...\n");
if (os.path.isfile(cv_html)):
    shutil.copy(cv_html, dst_html);
else:
    print("ERROR: cannot find "+cv_html+" ...\n");
