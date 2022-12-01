def html_exp():
    with open('employees.csv', encoding='utf-8') as data:
        data = data.readlines()
    style = 'style = "font-size:21px;"'
    html = '<html>\n <head></head>\n <body>\n'
    for i in data:
        html += '     <p {}> {} </p>\n'.format(style, i.removesuffix('\n').replace(',', ' ').replace(';', ''))
    with open('employees.html', 'w', encoding='utf-8') as page:
        page.write(html)
    return html