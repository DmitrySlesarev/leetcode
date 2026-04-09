from jinja2 import Template

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Shkoda', 'price': 17300},
#     {'model': 'Volvo', 'price': 44300},
#     {'model': 'Volkswagen', 'price': 21300}
# ]
#
# # sentence = "Sum of all cars' prices {{ cs | sum(attribute='price') }}"
# # sentence = "Sum of all cars' prices {{ (cs | max(attribute='price'))['model'] }}"
# # sentence = "Sum of all cars' prices {{ (cs | min(attribute='price'))['model'] }}"
# sentence = "Sum of all cars' prices {{ cs | replace('o', 'O') }}"
# tm = Template(sentence)
# msg = tm.render(cs = cars)

persons = [
    {"name": "Alexy", "age": 18, "weight": 78.5},
    {"name": "Nick", "age": 28, "weight": 82.3},
    {"name": "Ivan", "age": 33, "weight": 94.0},
]

tmpl = '''
{%- for u in users -%}
    {% filter lower %}{{u.name}}{% endfilter %}
{% endfor -%}
'''

tm = Template(tmpl)
msg = tm.render(users = persons)

if __name__ == "__main__":
    print(msg)