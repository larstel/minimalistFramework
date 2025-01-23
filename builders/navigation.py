import os, json
from utils.unicode import *

def build_navigation(build_config, page_file_name, language_code, general_localization):
    if(page_file_name not in build_config["noNavigation"]):

        nav_html = '<nav class="main-navigation" onmouseleave="closeSideNavigation()">'
        
        file_list = os.listdir("../" + build_config["contentTemplatesPath"])
        file_list = [path for path in file_list if path.endswith('.html')] # this removes localization files
        sortedList = sorted(file_list)

        for page in sortedList:
            page_name_of_list = os.path.basename(page)

            translation_dict_of_list = json.load(open("../" + build_config["contentTemplatesPath"] + page.split(".")[0] + "_localization.json"))

            if(page_name_of_list not in build_config["navigationBlacklist"]):
                if page_name_of_list != page_file_name: # do not highlight navigation entry
                    nav_html = nav_html + f'\n<a class="navigationElement" href="../../{language_code}/{use_unidecode(general_localization["language"][language_code])}/{use_unidecode(translation_dict_of_list["filename"][language_code])}.html">{translation_dict_of_list["title"][language_code]}</a>'
                else: # do highlight navigation entry
                    nav_html = nav_html + f'\n<a class="navigationElement {"active" if page_name_of_list != page_file_name else ""}" href="../../{language_code}/{use_unidecode(general_localization["language"][language_code])}/{use_unidecode(translation_dict_of_list["filename"][language_code])}.html" id="_nav" onclick="onSideNavigationLinkClicked(_nav)">{translation_dict_of_list["title"][language_code]}</a>'
        
        nav_html = nav_html + "</nav>"
        return nav_html
    
    else:
        return ""