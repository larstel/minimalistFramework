import re
from utils.unicode import *

def translate_text(input_text, translation_dict, language_code):
    # Regular expression to find text within <translate></translate> tags
    translate_pattern = re.compile(r'<translate>(.*?)<\/translate>', re.DOTALL)
    pattern = re.compile(r'(m-href="#([\w-]+)"|m-href="([^#"]+)"|m-id="([\w-]+)")'
)
    
    def replace_translation(match):
        # Extract the text within <translate></translate> tags
        text_to_translate = match.group(1).strip()

        # Get the translation from the dictionary, defaulting to the original text if not found
        try:
            translation_from_dict = translation_dict[text_to_translate][language_code]
        except Exception as error:
            print("localization error in file.")
            raise error 


        translation = translation_from_dict
 
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
    output_text = pattern.sub(replace_match, output_text)

    return output_text