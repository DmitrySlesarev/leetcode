# from jinja2 import Template
# from markupsafe import escape
#
# data = '''Jinja module
# puts corresponding value
# instead of {{ name }}
# '''
#
# data = '''{% raw %}Jinja module
# puts corresponding value
# instead of {{ name }} {% endraw %}'''
#
# link = '''HTML docs are defined as:
# <a href="#">Link</a>'''
#
# # tm = Template(data)
# # msg = tm.render(name="Fedor")
#
# # tm = Template("{{ link | e }}")
# # msg = tm.render(link=link)
#
# msg = escape(link)
# # msg = tm.render(link=link)
#

from jinja2 import Template


cities = [{'id': 1, 'city': 'Moscow'},
          {'id': 5, 'city': 'Tver'},
          {'id': 7, 'city': 'Minsk'},
          {'id': 8, 'city': 'Smolensk'},
          {'id': 11, 'city': 'Kaluga'}]

link = '''<select name="cities">
    {% for c in cities -%}
    {% if c.id > 6 -%}
        <option value="{{c['id']}}">{{c['city']}}</option>
    {%elif c.city == "Moscow" -%}
        <option>{{c['city']}}</option>
    {% else -%}
        {{ c['city'] }}
    {% endif -%}
    {% endfor -%}
    </select>'''

tm = Template(link)
msg = tm.render(cities=cities)

if __name__ == "__main__":
    print(msg)
