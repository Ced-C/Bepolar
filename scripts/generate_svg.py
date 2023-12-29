#!/bin/python3
import xml.etree.ElementTree as ET
import json
from lxml import etree
from lxml.builder import E



##
# Read Json and make a dict to change svg
#####
def get_layout(layout):
    """
    Parse Kalamine json file to get dict of form 
    KeyX:   
        levelY:z
    with:
    level1 = alpha
    level2 = shift
    level3 = altGr
    level4 = shift altGr
    level5 = lafayetteDeadKey
    level1 = shift lafayetteDeadKey
    """

    keymap = {}

    for id, symbols in layout['keymap'].items():
        keymap[id] = {}
        for i, symbol in enumerate(symbols):
            level = 'level'+str(i+1)
            keymap[id][level] = symbol
            # Add also lafayette dead key possible symbol as level 5&6
            if i in [0,1] and symbol in layout['deadkeys']['**']:
                level = 'level' + str(i+5)
                keymap[id][level] = layout['deadkeys']['**'][symbol]
        
        # if one level is undefined, add it anyway with no symbol
        for l in range(1,7):
            level = 'level'+str(l)
            if level not in keymap[id]:
                keymap[id][level] = ''
    return keymap



####
# Load SVG and change keycaps
###
def svg(keymap, context='Default', template_path='x-keyboard.svg', output_path='out.svg'):

    
    def keycap_layout(key, context='Default'):
        def format_svg(level, isDeadKey=False):
            def escape_xml_forbiden_char(text):
                forbiden_char = {
                    '&': '&amp;',
                    '<': '&lt;', 
                    '>': '&gt;',
                    "'": '&apos;',
                    '"': '&quot;',
                }
                for char, char_escaped in forbiden_char.items():
                    text = text.replace(char, char_escaped)
                return text
                
            svg_key = {
                "level1": '<text class="level1    {additional_class}"   width="22" height="22" x="12.8" y="43.4" text-anchor="middle">{symbol}</text>',
                "level2": '<text class="level2    {additional_class}"   width="22" height="22" x="12.8" y="20.6" text-anchor="middle">{symbol}</text>',
                "level3": '<text class="level3    {additional_class}"   width="22" height="22" x="38"   y="43.4" text-anchor="middle">{symbol}</text>',
                "level4": '<text class="level4    {additional_class}"   width="22" height="22" x="38"   y="20.6" text-anchor="middle">{symbol}</text>',
                "level5": '<text class="level5 dk {additional_class}"   width="22" height="22" x="38"   y="43.4" text-anchor="middle">{symbol}</text>',
                "level6": '<text class="level6 dk {additional_class}"   width="22" height="22" x="38"   y="20.6" text-anchor="middle">{symbol}</text>',
            }
            if isDeadKey:
                return  svg_key[level].format(
                            symbol = escape_xml_forbiden_char( key[level][1] ),
                            additional_class = 'deadKey'
                        )

            return  svg_key[level].format(
                        symbol = escape_xml_forbiden_char( key[level] ),
                        additional_class = ''
                    )

        svg_text = '<g class="key">'

        match context:
            case 'Default':
                for level in ['level2', 'level5', 'level1']:
                    if level == 'level1' and key['level1'].upper() == key['level2'].upper():
                        break # Skip level1 if level2 is uppercase level1

                    svg_text += format_svg(
                                    level,
                                    isDeadKey=( key[level] in LAYOUT['deadkeys'] )
                                )

            
            case 'AltGr':
                for level in ['level2', 'level3', 'level4', 'level1']:
                    if level == 'level1' and key['level1'].upper() == key['level2'].upper():
                        break # Skip level1 if level2 is uppercase level1
                    
                    svg_text += format_svg(
                                    level,
                                    isDeadKey=( key[level] in LAYOUT['deadkeys'] )
                                )
                        
            case 'DeadKey':
                for level in ['level2', 'level5', 'level6', 'level1']:
                    if level == 'level1' and key['level1'].upper() == key['level2'].upper():
                        break # Skip level1 if level2 is uppercase level1
                    if level == 'level6' and key['level5'].upper() == key['level6'].upper():
                        pass
                    else: 
                        svg_text += format_svg(
                                    level,
                                    isDeadKey=( key[level] in LAYOUT['deadkeys'] )
                                )
            
            case 'All':
                for l in range(1,7):
                    level = 'level'+str(l)
                    svg_text += format_svg(
                                    level,
                                    isDeadKey=( key[level] in LAYOUT['deadkeys'] )
                                )

        

        svg_text += '</g>'
        return svg_text

    svg_class = {
        'Default': '',
        'AltGr': ' altgr',
        'All': '',
        'DeadKey': ' dk'
    }

    # Remove <g class='key'> children and replace it by générated svg
    svg = etree.parse(template_path, etree.XMLParser(remove_blank_text=True))
    svg.getroot().attrib['class'] += svg_class[context]
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    for key_name in keymap:
        for svg_key_group in svg.xpath(f'//svg:g[@id="{key_name}"]', namespaces=ns):
            sub_g = svg_key_group.find('svg:g', namespaces=ns)
            for child in list(sub_g):
                sub_g.remove(child)
            sub_g.append(etree.fromstring( keycap_layout(keymap[key_name], context) ))
    svg.write(output_path)
    return svg
...




path = ''

with open(path+'dist/bepolar.json') as f:
    LAYOUT = json.load(f)

path = 'img/'
keymap = get_layout(LAYOUT)
for context in ['Default', 'AltGr', 'DeadKey']:
    output = f'{path}bepolar_{context}.svg'
    svg(
        keymap,
        context=context,
        template_path=path+'x-keyboard.svg',
        output_path=output
    )
    print(f'Generating {output}')
