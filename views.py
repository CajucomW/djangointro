import os
import glob
from jinja2 import Template
from django.shortcuts import render

def base(request):
    print('Index page is processing...')
    context = {
        'content': 'index.html',
        'title': 'About Me',
        'active': '{{index_is_active}}',
    }
    return render(request, 'base.html', context)

def index(request):
    context = {}
    return render(request, 'index.html', context)

def tech(request):
    context = {}
    return render(request, 'tech.html', context)

def pta(request):
    context = {}
    return render(request, 'pta.html', context)
    
def jiujitsu(request):
    context = {}
    return render(request, 'jiujitsu.html', context)

# def templates(content, template, html_file):
#     combined = template.replace('{{content}}', html_file)
#     combined = combined.replace('{{title}}', content['title'])
#     combined = combined.replace(content['active'], 'active')
#     return combined

# def process(content):
#     template = open('templates/base.html').read()
#     html_file = open(content['filename']).read()
#     combined = templates(content, template, html_file)
#     open(content['output'], 'w+').write(combined)

# def main():
#     for content in pages:
#         print("Processing...", content['title'])
#         process(content)
#     print('Done')

# if __name__ == "__main__":
#     main()   

# def html_files():
#     pages = []
    
#     all_html_files = glob.glob("content/*.html")
#     output = glob.glob('docs/*.html')

#     for html_path in all_html_files:                            # html_path is content/*.html
#         file_name = os.path.basename(html_path)                 # file_name is *.html
#         name_only, extension = os.path.splitext(file_name)      # name_only is *
#         html_content = open(html_path).read()
#         doc_dir = "docs/" + file_name

#         pages.append({
#             "title": name_only,
#             "output": doc_dir,
#             "filename": file_name,
#             "content": html_content,
#         })
#     return render(request, 'html_files', context)

# def template_pages():
#     template_html = open('templates/base.html').read()

#     for page in pages:
#         title = page['title']
#         output = page['output']
#         filename = page['filename']                             # filename is content/*html from list
#         content = page['content']
#         template = Template(template_html)
#         result = template.render(
#             title=title, 
#             output=output,
#             filename=filename,
#             content=content,
#             pages=pages,       #### <<< links break when this line isn't inlcuded. Not sure why. ####
#             )
#         open(page['output'], 'w+').write(result)
#     return render(request, 'template_pages', context)

