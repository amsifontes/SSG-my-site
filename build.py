print("website fragments... assemble!!!")
# ingest top and bottom
top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()
print("top and bottom are in position")
# Read index
print("reading index...")
index = open('content/index.html').read()

# Assemble index
open('index.html', 'a+').write(top)
open('index.html', 'a+').write(index)
open('index.html', 'a+').write(bottom)


# Read bio
print("reading bio...")
bio = open('content/bio.html').read()

# Assemble bio
open('bio.html', 'a+').write(top)
open('bio.html', 'a+').write(bio)
open('bio.html', 'a+').write(bottom)


# Read blog
print("reading blog...")
blog = open('content/blog.html').read()

# Assemble blog

open('blog.html', 'a+').write(top)
open('blog.html', 'a+').write(blog)
open('blog.html', 'a+').write(bottom)


# Read projects
print("reading projects...")
projects = open('content/projects.html').read()

# Assemble projects

open('projects.html', 'a+').write(top)
open('projects.html', 'a+').write(projects)
open('projects.html', 'a+').write(bottom)

print("fragments assembled successfully! :)")
