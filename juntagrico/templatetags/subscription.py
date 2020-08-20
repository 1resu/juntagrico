from django import template

register = template.Library()


@register.filter
def overview(part_overview):
    def loop(result_list, key, value, more_than_one=False):
        if more_than_one:
            result_list.append('<li>{}</li>'.format(key))
            result_list.append('<ul>')
        for new_key, new_value in value.items():
            if isinstance(new_value, int):
                display_name = new_key[1] if new_key[1] != '' else key
                result_list.append('<li> {} : {} </li>'.format(display_name, new_value))
            else:
                loop(result_list, new_key, new_value, len(value.items()) > 1)
        if more_than_one:
            result_list.append('</ul>')

    result = ['<ul>']
    loop(result, '', part_overview)
    result.append('</ul>')
    return '\n'.join(result)



