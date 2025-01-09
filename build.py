import logging
from pathlib import Path
from distutils.dir_util import copy_tree
from utils.unicode import *
from builders.footer import *
from builders.localization_options import *
from builders.navigation import *
from builders.translate import *
from builders.translate import *
from builders.meta import *

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Set the format
)


def replacement_function(match):
    # Extract the current line's indentation
    line = match.group(0)
    leading_spaces = re.match(r'\s*', line).group(0)  # Get leading spaces
    # Replace while keeping the indentation
    return f"{leading_spaces}print('This is a replacement!')"

build_config = json.load(open("../buildConfig.json"))
Path("./build").mkdir(exist_ok=True)
copy_tree("../additionalFilesForServer", "./build")
general_localization = json.load(open("../" + build_config["contentTemplatesPath"] + "localization.json"))
template_html = Path("../template.html").read_text()

# for every language
for language_code in build_config["availableLanguages"]:
    logging.info("==== Start building pages for the language: " + language_code + " ====")

    # create a folder for the current language
    Path("./build/" + language_code + "/" + use_unidecode(general_localization["language"][language_code])).mkdir(parents=True, exist_ok=True)
    logging.info("-> folder created")


    content_path = "../" + build_config["contentTemplatesPath"]
    for page_file_name in sorted(os.listdir(content_path)):
        if page_file_name.endswith(".html"):
            logging.info(f"== -> File: {page_file_name} loaded. ==")

            page_path = os.path.join(content_path, page_file_name)
            localization_path = f"{os.path.splitext(page_path)[0]}_localization.json"

            translation_dict = json.load(open(localization_path))
            logging.info("-> Localization for page loaded.")

            page_content = translate_text(Path(page_path).read_text(), translation_dict, language_code)
            logging.info("-> Page localizated.")

            content_copy = template_html # create a copy of the template


            # insert content language
            content_copy = re.sub('builder-content-language', language_code, content_copy)

            # insert content description
            content_copy = re.sub('builder-content-description', translation_dict["description"][language_code], content_copy)

            # insert content keywords
            content_copy = re.sub('builder-content-keywords', translation_dict["keywords"][language_code], content_copy)

            # insert title
            content_copy = re.sub('<builder-title></builder-title>', general_localization["title"][language_code] + " | " + translation_dict["title"][language_code], content_copy)

            # insert header
            content_copy = re.sub('<builder-header></builder-header>', build_config["header"], content_copy)

            # insert sub header
            content_copy = re.sub('<builder-sub-header></builder-sub-header>', build_config["subHeader"], content_copy)

            # insert localization options
            content_copy = re.sub('<language-selector-content></language-selector-content>', build_localization_options(build_config, language_code, general_localization, translation_dict), content_copy)

            # insert content into template
            content_copy = re.sub('<builder-content></builder-content>', f'{page_content}', content_copy)

            # insert navigation
            content_copy = re.sub('<builder-nav></builder-nav>', build_navigation(build_config, page_file_name, language_code, general_localization), content_copy)

            # insert footer
            content_copy = re.sub('<builder-footer></builder-footer>', build_footer(build_config, language_code, general_localization), content_copy)

            # insert translation language
            content_copy = re.sub('builder-translation-language', f'var languages = {use_unidecode(general_localization["language"])}', content_copy)

            # insert translation filename
            content_copy = re.sub('builder-translation-filename', f'var filenames = {use_unidecode(translation_dict["filename"])}', content_copy)

            # insert meta tags
            content_copy = re.sub('<builder-header-tags></builder-header-tags>', build_meta_tags(build_config, page_file_name), content_copy)


            # translate with the general localization
            content_copy = translate_text(content_copy, general_localization, language_code)


            # save everything into file
            translated_filename = translation_dict["filename"][language_code]

            with open(f'./build/{language_code}/{use_unidecode(general_localization["language"][language_code])}/{use_unidecode(translated_filename)}.html', 'w') as outfile:
                outfile.write(content_copy)

