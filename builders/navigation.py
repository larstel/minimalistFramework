import os, json, re
from utils.unicode import *
from bs4 import BeautifulSoup

def build_navigation(build_config, page_file_name, language_code, general_localization, page_content, translations):
    if(page_file_name not in build_config["noNavigation"]):

        nav_html = '<nav class="main-navigation" onmouseleave="closeSideNavigation()">'
        
        file_list = os.listdir("../" + build_config["contentTemplatesPath"])
        file_list = [path for path in file_list if path.endswith('.html')] # this removes localization files
        sortedList = sorted(file_list)

        for page in sortedList:
            page_name_of_list = os.path.basename(page)

            translation_dict_of_list = json.load(open("../" + build_config["contentTemplatesPath"] + "/" + page.split(".")[0] + "_localization.json"))

            if(page_name_of_list not in build_config["navigationBlacklist"]):
                if page_name_of_list != page_file_name: # do not highlight navigation entry
                    nav_html = nav_html + f'\t<a class="navigationElement" href="../../{language_code}/{use_unidecode(general_localization["language"][language_code])}/{use_unidecode(translation_dict_of_list["filename"][language_code])}.html">{translation_dict_of_list["title"][language_code]}</a>\n'
                else: # do highlight navigation entry
                    nav_html = nav_html + f'\t<a class="navigationElement {"active" if page_name_of_list != page_file_name else ""}" href="../../{language_code}/{use_unidecode(general_localization["language"][language_code])}/{use_unidecode(translation_dict_of_list["filename"][language_code])}.html" id="_nav" onclick="onSideNavigationLinkClicked(_nav)">{translation_dict_of_list["title"][language_code]}</a>\n'
                    # add sub navigation
                    # --> alphabet
                    soup = BeautifulSoup(page_content, "html.parser")

                    header_containers = soup.find_all("div", class_="header-container")

                    id_values = [div.get("data-static-id") for div in header_containers if div.has_attr("data-static-id")]

                    for entry in id_values:
                        nav_html = nav_html + f'<a class="subNavigationElement" href="#{use_unidecode(translations[entry][language_code])}" id="{use_unidecode(translations[entry][language_code])}_nav" onclick="onSideNavigationLinkClicked()">{translations[entry + "-title"][language_code]}</a>\n'
        
        nav_html = nav_html + "\n</nav>"
        return nav_html
    
    else:
        return ""