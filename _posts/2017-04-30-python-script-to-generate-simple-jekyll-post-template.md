---
layout: post
title:  Python script to generate simple Jekyll post template
date:   2017-04-30 14:15:11
categories: [website dev]
tags:       [Python, Jekyll]
---

It's a waste of time to manually type the date in the file name and type the front matter when creating a new post. I tried out the [Jekyll::Compose](https://github.com/jekyll/jekyll-compose), but the generated front matter is not complete (maybe I missed something...).

So I created the following simple python script to generate post template for me.
{% highlight py %}
#!/usr/bin/env python

import argparse
import time
import re

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='Generate post template.')
    argparser.add_argument("title", nargs='+', help="post title")
    args = argparser.parse_args()

    # Avoid using quotes when typing in the args
    title = ' '.join(args.title)

    # Time info
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%Y-%m-%d")
    date_str = current_date+" "+current_time

    if title:
        # Generate lower case filename
        filename = re.sub('\s+','-',title)
        filename = current_date+"-"+filename+".md"
        filename = filename.lower()

        # Front matter
        outfile = open(filename, 'w')
        outfile.write("---\n")
        outfile.write("layout: post\n")
        outfile.write("title:  "+title+"\n")
        outfile.write("date:   "+date_str+"\n")
        outfile.write("categories: []\n")
        outfile.write("tags:       []\n")
        outfile.write("---\n\n")
        outfile.close()
    else:
        print("Please provide a title...\n")
{% endhighlight %}

I put the script in the `_posts` directory.

Usage:
```
usage: post.py [-h] title
```
For example, to generate a template for this post:
```
./post.py Python script to generate simple Jekyll post template
```
