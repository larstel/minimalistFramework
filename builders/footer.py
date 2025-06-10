from datetime import datetime
from utils.unicode import use_unidecode
import json

def build_footer(build_config, language_code, general_localization, current, previousChapterName, nextChapterName):
    if(build_config["hasFooter"]=='true'):
        current_year = datetime.now().year
        copyright_text = f"© {build_config['copyrightSince']} - {current_year} {build_config['header'].lower()}{build_config['subHeader'].lower()} "
        
        def localized_link(filename_key, text_key):
            filename = use_unidecode(general_localization[filename_key][language_code].lower())
            text = general_localization[text_key][language_code]
            language = use_unidecode(general_localization["language"][language_code])
            return f'<a href="../../{language_code}/{language}/{filename}.html">{text}</a>'
        
        impressum = localized_link("impressum_filename", "impressum")
        datenschutzhinweise = localized_link("datenschutzhinweise_filename", "datenschutzhinweise")
        datenschutzeinstellungen = localized_link("datenschutzhinweise_filename", "datenschutzeinstellungen")
        kontakt_button = f'<button class="footer-button" onclick="writeEmail();">{general_localization["kontakt"][language_code]}</button>'
        build_with = f'<translate>build_with</translate> <a href="https://github.com/larstel/minimalistFramework" rel="nofollow noopener" target="_blank">MinimalistFramework</a>.'
        
        if(previousChapterName != None):
            translation_dict_of_list = json.load(open("../" + build_config["contentTemplatesPath"] + previousChapterName.split(".")[0] + "_localization.json"))
            previous_chapter = f'<a href="../../{language_code}/{use_unidecode(general_localization["language"][language_code])}/{use_unidecode(translation_dict_of_list["filename"][language_code])}.html" class="chapter-button chapter-left">{translation_dict_of_list["title"][language_code]}</a>' if previousChapterName is not None else '<a></a>'
        else:
            previous_chapter = "<span></span>"

        if(nextChapterName != None):
            translation_dict_of_list = json.load(open("../" + build_config["contentTemplatesPath"] + nextChapterName.split(".")[0] + "_localization.json"))
            next_chapter = f'<a href="../../{language_code}/{use_unidecode(general_localization["language"][language_code])}/{use_unidecode(translation_dict_of_list["filename"][language_code])}.html" class="chapter-button chapter-right">{translation_dict_of_list["title"][language_code]}</a>'
        else:
            next_chapter = "<span></span>"

        return (
            f'<footer class="footer">'
            f'<div class="chapter-buttons">'
            f'{previous_chapter}'
            f'{next_chapter}'
            f'</div>'
            f'<div class="footer-line"></div>'
            f'<div class="footer-links">'
            f'<span class="footer-margin">{impressum}</span>'
            f'<span class="footer-margin">{datenschutzhinweise}</span>'
            f'<span class="footer-margin">{datenschutzeinstellungen}</span>'
            f'<span class="footer-margin">{kontakt_button}</span>'
            f'</div>'
            f'<br>'
            f'<br>'
            f'<br>'
            f'<span>{build_with}</span>'
            f'<br>'
            f'<br>'
            f'<span>{copyright_text}</span>'
            f'</footer>'
        )
    else:
        return ""
