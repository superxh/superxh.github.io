# Hang Xu's personal blog
## Notes

1. The blog is proudly powered by [Pelican](https://getpelican.com/), which takes great advantage of [Python](https://www.python.org/)
2. The blog is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/) 
3. The theme is built based on the Pelican *Simple* theme
4. Part of CSS statements and idea of the theme is from the [The Art Gallery Guardian](https://chaoxuprime.com/blog.html) by [Chao Xu](https://chaoxuprime.com/)

## Pre-request

Pelican (with markdown) 
```
python -m pip install "pelican[markdown]"
```
[Git](https://git-scm.com/)

## Installation

```
git clone https://github.com/superxh/superxh.github.io.git
```

## Automation

1. Compose posts in the *content* folder with Markdown
2. Update the blog post

```
cd superxh.github.io
```

```
pelican content
```

3. Publish with Github Pages

```
git add .
```

```
git commit -m "message"
```

```
git push -u origin master
```

To duplicate the blog system to your own repository add the remote repository before *git push*

```
git remote add origin url.git
```

## File system

pelican setting -- pelicanconf.py

theme -- simpleplus (the folder)