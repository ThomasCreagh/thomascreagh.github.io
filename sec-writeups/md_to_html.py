import os
import markdown
from bs4 import BeautifulSoup

print(f"the current working dir is: {os.getcwd()}")

files = os.listdir("md")

page_links = [
    f'<li><a href="html/{i.replace("md", "html")}">{i.split(".")[0]}</a></li>' for i in files]
index_nav = """
  <nav>
    <ul class="nav">
      <li><a href="../index.html">Home</a></li>
      <li><a href="https://github.com/ThomasCreagh/">Github</a></li>
      <li>
        <a href="https://www.linkedin.com/in/thomas-creagh/">Linkedin</a>
      </li>
      <li><a href="../projects.html">Projects</a></li>
      <li><a href="index.html">SecurityWriteups</a></li>
    </ul>
  </nav>
"""
html_content = '<head><link rel="stylesheet" href="../css/styles.css">' + \
    '<link rel="icon" href="/../favicon-32x32.png" sizes="32x32" type="image/png" />' + \
    '<link rel="icon" href="/../favicon-16x16.png" sizes="16x16" type="image/png" />' + \
    '<title>SecurityWriteups</title></head>' + \
    f'<body>{index_nav}<div class="projects"><h1>Security Write Ups</h1>' + \
    f'<div class=project-list><ul>{str(page_links)[2:-2].replace(",","")}' + \
    '</ul></div></div></body>'
with open("index.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("wrote index.html succefully")


for file in files:
    with open(f"md/{file}", "r", encoding="utf-8") as md_file:
        md_content = md_file.read()

    raw_html = markdown.markdown(md_content, extensions=['fenced_code'])

    soup = BeautifulSoup(raw_html, "html.parser")
    for img in soup.find_all("img"):
        wrapper = soup.new_tag("div", attrs={"class": "scroll-img"})
        img.wrap(wrapper)

    nav = """
    <nav>
        <ul class="nav">
        <li><a href="../../index.html">Home</a></li>
        <li><a href="https://github.com/ThomasCreagh/">Github</a></li>
        <li>
            <a href="https://www.linkedin.com/in/thomas-creagh/">Linkedin</a>
        </li>
        <li><a href="../../projects.html">Projects</a></li>
        <li><a href="../index.html">SecurityWriteups</a></li>
        </ul>
    </nav>
    """

    full_html = '<head><link rel="stylesheet" href="../css/main.css">' + \
        '<link rel="icon" href="/../../favicon-32x32.png" sizes="32x32" type="image/png" />' + \
        '<link rel="icon" href="/../../favicon-16x16.png" sizes="16x16" type="image/png" />' + \
        f'<title>{file.replace(".md", "").replace("_", " ")}</title></head>' + \
        f'<body>{nav}<div class="page">{str(soup)}</div></body>'

    with open(f"html/{file.replace('.md', '.html')}", "w", encoding="utf-8") as html_file:
        html_file.write(full_html)

    print(f"converted {file} file")

print("finished converting md to html")
