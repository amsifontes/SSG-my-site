def ingest_base(base_file_path):
    base_file = open(base_file_path).read()
    return base_file

def content_insert(template, content, insert_marker="{{ content }}"):
    output = template.replace(insert_marker, content)
    return output

def main():
    pages = [
        {
            'input': 'content/index.html',
            'output': 'docs/index.html',
            'title': 'Homepage',
        },
        {
            'input': 'content/bio.html',
            'output': 'docs/bio.html',
            'title': 'Bio',
        },
        {
            'input': 'content/blog.html',
            'output': 'docs/blog.html',
            'title': 'Blog',
        },
        {
            'input': 'content/projects.html',
            'output': 'docs/projects.html',
            'title': 'Projects',
        },
        ]

    print("website fragments... assemble!!!")
    # ingest top and bottom
    # top = open('templates/top.html').read()
    # bottom = open('templates/bottom.html').read()
    # print("top and bottom are in position")

    #ingest base template
    template = ingest_base('templates/base.html')

    for page in pages:
        content = open(page['input']).read()
        # full_page = template.replace("{{ content }}", content)
        full_page = content_insert(template, content)
        open(page['output'], 'w+').write(full_page)

        #
        # open(page['output'], 'a+').write(top)
        # open(page['output'], 'a+').write(content)
        # open(page['output'], 'a+').write(bottom)

    # # Read index
    # print("reading index...")
    # index = open('content/index.html').read()
    #
    # # Assemble index
    # open('docs/index.html', 'a+').write(top)
    # open('docs/index.html', 'a+').write(index)
    # open('docs/index.html', 'a+').write(bottom)
    #
    #
    # # Read bio
    # print("reading bio...")
    # bio = open('content/bio.html').read()
    #
    # # Assemble bio
    # open('docs/bio.html', 'a+').write(top)
    # open('docs/bio.html', 'a+').write(bio)
    # open('docs/bio.html', 'a+').write(bottom)
    #
    #
    # # Read blog
    # print("reading blog...")
    # blog = open('content/blog.html').read()
    #
    # # Assemble blog
    #
    # open('docs/blog.html', 'a+').write(top)
    # open('docs/blog.html', 'a+').write(blog)
    # open('docs/blog.html', 'a+').write(bottom)
    #
    #
    # # Read projects
    # print("reading projects...")
    # projects = open('content/projects.html').read()
    #
    # # Assemble projects
    # open('docs/projects.html', 'a+').write(top)
    # open('docs/projects.html', 'a+').write(projects)
    # open('docs/projects.html', 'a+').write(bottom)

    print("fragments assembled successfully! :)")


if __name__ == '__main__':
    main()
