"""
    Python script to add content to common web templates for Matris Health Pages
"""

def get_heading_template():
    with open("heading_template.html") as head_file:
        return head_file.read()

def get_trailing_template():
    with open("trailing_template.html") as trail_file:
        return trail_file.read()

def get_content(page):
    with open(page) as p:
        return p.read();

def get_page(page):

    if not page:
        page = input("Please input filename: ")

    head = get_heading_template()
    tail = get_trailing_template()
    content = get_content(page)
    
    webpage = head + content + tail

    with open(page, 'w') as content:
        content.write(webpage)
        print(page + " saved!!")


def get_title(link):
    """
        Convert a link in the all_links.txt file to a user friendly string
    """
    return ' '.join(link.split('.')[0].split('-')).title()

def generate_titles(file):
    """
        Generate all titles from the specified all_links.txt file. 
        Save to titles.txt
    """
    with open(file) as f:
        l = f.readlines()

        for i, link in enumerate(l):
            l[i] = get_title(link) + "\n"

    with open(file.split("/")[0] + "/titles.txt", 'w') as o:
        o.writelines(l)


def create_links(dir):
    """
        Generate list of anchor tags with given links and having text as titles
    """
    with open(dir + "/all_links.txt") as all_links:
        links = all_links.readlines()
    
    with open(dir + "/titles.txt") as all_titles:
        titles = all_titles.readlines()
    
    l = []
    for link, title in zip(links, titles):
        l.append("<li><a href=\"{0}\">{1}</a></li>\n".format(link.strip(), title.strip()))

    with open("content.txt", 'w') as c:
        c.writelines(l)

def main():
    get_page(None)

if __name__ == "__main__":
    main()