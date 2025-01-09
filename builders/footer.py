from datetime import datetime
from utils.unicode import *

def build_footer(build_config, language_code, general_localization):
    return \
    f'<footer class="footer"> \
        <span>© {build_config["copyrightSince"]} - {datetime.now().year} {build_config["header"].lower()}{build_config["subHeader"].lower()} |</span> \
        <span><a href="../../{language_code}/{use_unidecode(general_localization["language"][language_code])}/{use_unidecode(general_localization["impressum_filename"][language_code].lower())}.html">{general_localization["impressum"][language_code].capitalize()}</a>&nbsp;|</span> \
        <span><a href="../../{language_code}/{use_unidecode(general_localization["language"][language_code])}/{use_unidecode(general_localization["datenschutzhinweise_filename"][language_code].lower())}.html">{general_localization["datenschutzhinweise"][language_code]}</a>&nbsp;|</span> \
        <span><a href="../../{language_code}/{use_unidecode(general_localization["language"][language_code])}/{use_unidecode(general_localization["datenschutzhinweise_filename"][language_code].lower())}.html">{general_localization["datenschutzeinstellungen"][language_code]}</a>&nbsp;|</span> \
        <span><button class="footer-button" onclick="writeEmail();">{general_localization["kontakt"][language_code]}</button></span> \
    </footer>'