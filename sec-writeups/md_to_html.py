import os
import markdown

print(f"the current working dir is: {os.getcwd()}")

files = os.listdir("md")
for file in files:
    with open(f"md/{file}", "r", encoding="utf-8") as md_file:
        md_content = md_file.read()

    html_content = '<head><link rel="stylesheet" href="../css/main.css"></head>\n' + \
        '<body>' + markdown.markdown(md_content,
                                     extensions=['fenced_code']) + '</body>'

    with open(f"html/{file.replace('.md', '.html')}", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    print(f"converted {file} file")

print("finished converting md to html")
