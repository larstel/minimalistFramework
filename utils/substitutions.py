from builders.footer import *
from builders.navigation import *
from builders.translate import *
from builders.meta import *


def apply_substitutions(content, build_config, translation_dict, language_code, general_localization, page_content, page_file_name):
    replacements = {
        'builder-content-language': language_code,
        'builder-content-description': translation_dict["description"][language_code],
        'builder-content-keywords': translation_dict["keywords"][language_code],
        '<builder-title></builder-title>': f'{general_localization["title"][language_code]} | {translation_dict["title"][language_code]}',
        '<builder-header></builder-header>': build_config["header"],
        '<builder-sub-header></builder-sub-header>': build_config["subHeader"],
        '<builder-content></builder-content>': page_content,
        '<builder-nav></builder-nav>': build_navigation(build_config, page_file_name, language_code, general_localization),
        '<builder-footer></builder-footer>': build_footer(build_config, language_code, general_localization),
        'builder-translation-language': f'var languages = {use_unidecode(general_localization["language"])}',
        'builder-translation-filename': f'var filenames = {use_unidecode(translation_dict["filename"])}',
        '<builder-header-tags></builder-header-tags>': build_meta_tags(build_config, page_file_name),
    }
    
    # Perform replacements
    for placeholder, value in replacements.items():
        content = re.sub(placeholder, value, content)
    
    return content