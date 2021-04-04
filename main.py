import requests
import treeTest


def remove_all_of_a_kind(input_string, element_begin, element_end, max_rotations_bool=False, max_rotations=2):
    element_before_link = True
    count = 0
    while element_before_link:
        if max_rotations_bool & count == max_rotations:
            element_before_link = False
            break
        link_position = input_string.find('<a')
        element_beginning = input_string.find(element_begin)
        element_ending = input_string.find(element_end)
        next_element = input_string[element_beginning+1:len(input_string):].find(element_begin)

        if next_element < element_ending:
            element_ending_helper = input_string[element_ending+2:len(input_string):]
            element_ending_helper_2 = input_string[0:element_ending+2:]
            element_ending = element_ending_helper.find(element_end) + len(element_ending_helper_2)

        if (element_beginning < link_position) & (element_beginning != -1):
            input_string = input_string[0:element_beginning:] + input_string[element_ending + len(element_end):len(input_string):]
        else:
            element_before_link = False
        count += 1
    return input_string


def getfirstlink(url):
    url = 'https://en.wikipedia.org' + url
    headers = {'Accept-Encoding': 'identity'}
    r = requests.get(url, headers=headers)
    output = r.text

    # get the text body
    output = output.split('class="mw-parser-output">')[1]

    # remove Table
    table_exists = True
    count = 0
    while table_exists:
        if count > 2:
            table_exists = False
            break

        table_beginning = output.find('<tbody>')
        if table_beginning != -1:
            table_ending = output.find('</tbody>')
            output = output[0:table_beginning:] + output[table_ending + 8: len(output):]
        else:
            table_exists = False
        count += 1

    # get the first paragraph
    output = output.split('<p>')[1]

    # remove Brackets
    output = remove_all_of_a_kind(output, '(', ')')

    bracketspositionbeginning = output.find('(')

    if bracketspositionbeginning != -1:
        bracketspositionending = output.find(')')
        output = output[0:bracketspositionbeginning:] + output[bracketspositionending+1: len(output):]

    # remove cities
    cite_before_link = True
    while cite_before_link:

        link_position = output.find('<a')
        cite_beginning = output.find('<sup')
        if (cite_beginning < link_position) & (cite_beginning != -1):
            cite_ending = output.find('</sup>')
            output = output[0:cite_beginning:] + output[cite_ending+6: len(output):]
        else:
            cite_before_link = False

    # remove span
    # span_before_link = True
    # while span_before_link:
    #     link_position = output.find('<a')
    #     cite_beginning = output.find('<span')
    #     if (cite_beginning < link_position) & (cite_beginning != -1):
    #         cite_ending = output.find('</span>')
    #         output = output[0:cite_beginning:] + output[cite_ending+6: len(output):]
    #     else:
    #         span_before_link = False


    # get the first link
    output = output.split('<a href="')[1]
    output = output.split('" ')[0]
    print(output)
    return output


apple_link = '/wiki/Apple_Inc.'
big_array = []


def get_links_from_article(url):


    not_philosophy = True
    link = '/wiki/' + url
    array = [link]
    while not_philosophy:
        link = getfirstlink(link)
        array.append(link)
        if link == '/wiki/Philosophy':
            break
    return array


big_array.append(get_links_from_article('Marmalade'))
big_array.append(get_links_from_article('Pear'))
big_array.append(get_links_from_article('Decorative_arts'))

print(big_array)
# big_array = [['/wiki/Botany', '/wiki/Science', '/wiki/Scientific_method', '/wiki/Empirical_evidence', '/wiki/Information', '/wiki/Uncertainty', '/wiki/Epistemology', '/wiki/Philosophy'], ['/wiki/Branches_of_science', '/wiki/Science', '/wiki/Scientific_method', '/wiki/Empirical_evidence', '/wiki/Information', '/wiki/Uncertainty', '/wiki/Epistemology', '/wiki/Philosophy']]

treeTest.draw_tree(big_array)


# getfirstlink('https://en.wikipedia.org/wiki/Marmalade')

# getfirstlink('https://en.wikipedia.org/wiki/Economics')

# getfirstlink('https://en.wikipedia.org/wiki/Wikipedia:Ge tting_to_Philosophy')

#getfirstlink('https://en.wikipedia.org/wiki/Epistemology')


#print(r.text)