import re
from utils.unicode import *

def translate_text(input_text, translation_dict, language_code):
    translate_pattern = re.compile(r'<translate>(.*?)<\/translate>', re.DOTALL)
    m_pattern = re.compile(r'(m-href="#([\w-]+)"|m-href="([^#"]+)"|m-id="([\w-]+)")')

    def replace_translation(match):
        text_to_translate = match.group(1).strip()
        translation = translation_dict.get(text_to_translate, {}).get(language_code, text_to_translate)
        return f'{translation}'


    def replace_match(match):
        if match.group(2):  # for m-href="#word"
            attribute = 'href-hashtag'
            word = match.group(2)
        elif match.group(3): # for m-href="word"
            attribute = 'href'
            word = match.group(3)
        else:   # for m-id="word"
            attribute = 'id'
            word = match.group(4)

        
        if word in translation_dict and language_code in translation_dict[word]:
            if attribute == 'href-hashtag':
                return f'href="#{use_unidecode(translation_dict[word][language_code])}"'
            elif attribute == 'id':
                return f'id="{use_unidecode(translation_dict[word][language_code])}"' 
            else:
                return f'href="{use_unidecode(translation_dict[word][language_code])}"' 
        else:
            return match.group(0)  # Return the original match if word or language_code is not in the dictionary

    # Use re.sub to replace the text within <translate></translate> tags with translations
    output_text = translate_pattern.sub(replace_translation, input_text)
    output_text = m_pattern.sub(replace_match, output_text)

    return output_text