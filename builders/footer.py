from datetime import datetime
from utils.unicode import use_unidecode

def build_footer(build_config, language_code, general_localization):
    current_year = datetime.now().year
    copyright_text = f"© {build_config['copyrightSince']} - {current_year} {build_config['header'].lower()}{build_config['subHeader'].lower()}"
    
    def localized_link(filename_key, text_key):
        filename = use_unidecode(general_localization[filename_key][language_code].lower())
        text = general_localization[text_key][language_code]
        language = use_unidecode(general_localization["language"][language_code])
        return f'<a href="../../{language_code}/{language}/{filename}.html">{text}</a>'
    
    impressum = localized_link("impressum_filename", "impressum")
    datenschutzhinweise = localized_link("datenschutzhinweise_filename", "datenschutzhinweise")
    datenschutzeinstellungen = localized_link("datenschutzhinweise_filename", "datenschutzeinstellungen")
    kontakt_button = f'<button class="footer-button" onclick="writeEmail();">{general_localization["kontakt"][language_code]}</button>'
    
    return (
        f'<footer class="footer">'
        f'<span>{copyright_text} |</span>'
        f'<span>{impressum}&nbsp;|</span>'
        f'<span>{datenschutzhinweise}&nbsp;|</span>'
        f'<span>{datenschutzeinstellungen}&nbsp;|</span>'
        f'<span>{kontakt_button}</span>'
        f'</footer>'
    )
