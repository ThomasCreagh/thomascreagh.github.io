import os
import markdown
from bs4 import BeautifulSoup as bs

base = os.path.dirname(os.path.abspath(__file__))
print(f"the current working dir is: {base}")
dirs = ["blogs", "sec-writeups"]

for dir in dirs:
    print(f"\nConverting {dir} dir...")
    folder_base = os.path.join(base, dir)

    with (
        open(os.path.join(folder_base, "index.template.html"), "rb") as src,
        open(os.path.join(folder_base, "index.html"), "wb") as dst
    ):
        dst.write(src.read())

    files = os.listdir(os.path.join(folder_base, "md"))

    with open(os.path.join(folder_base, "index.html")) as temp_file:
        index = bs(temp_file, "html.parser")

    documents = index.find("ul", {"class" : "documents"})

    for file in files:
        new_li = index.new_tag("li")

        new_a = index.new_tag("a", attrs={"href": f"html/{file.replace('.md', '.html')}"})
        new_a.string = file.replace(".md", "")
        new_li.append(new_a)

        documents.append(new_li)

        with open(os.path.join(folder_base, "template.html")) as temp_file:
            soup = bs(temp_file, "html.parser")
        with open(os.path.join(folder_base, f"md/{file}"), "r", encoding="utf-8") as md_file:
            md_content = md_file.read()

        raw_html = markdown.markdown(md_content, extensions=['fenced_code'])

        raw_soup = bs(raw_html, "html.parser")
        for img in raw_soup.find_all("img"):
            wrapper = raw_soup.new_tag("div", attrs={"class": "scroll-img"})
            img.wrap(wrapper)

        page = soup.find("div", {"class" : "page"})
        page.append(raw_soup)

        with open(os.path.join(folder_base, f"html/{file.replace('.md', '.html')}"), "wb") as html_file:
            html_file.write(soup.prettify("utf-8"))

        print(f"converted {file} file")

    with open(os.path.join(folder_base, "index.html"), "wb") as html_file:
        html_file.write(index.prettify("utf-8"))

    print("finished converting md to html")
