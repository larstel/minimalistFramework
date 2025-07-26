from pathlib import Path
from distutils.dir_util import copy_tree
from utils.unicode import *
from utils.substitutions import *
from utils.logging import *
from utils.sitemap import *
from utils.files_and_directories import *

def build_sites():
    change_to_directory_of_file(__file__)

    build_config = json.load(open("../buildConfig.json"))
    Path("./build").mkdir(exist_ok=True)
    copy_tree("../additionalFilesForServer", "./build")

    for content in build_config["content"]:
        if content.strip():
            content = content + "/"

        general_localization = json.load(open("../" + build_config["contentTemplatesPath"] + "/" + content + "localization.json"))
        template_html = Path("../template.html").read_text()

        sitemap = {}

        logging.info("Start iterating through content.")

        for language_code in build_config["availableLanguages"]:
            logging.debug(f"==== Start building pages for the language: {language_code} ====")

            if content.strip():
                language_path = Path(f"./build/{language_code}/{use_unidecode(general_localization[content][language_code])}")
            else:
                language_path = Path(f"./build/{language_code}/")

            language_path.mkdir(parents=True, exist_ok=True)
            logging.debug("-> Folder created")

            content_path = f"../{build_config['contentTemplatesPath']}/{content}"
            print(content_path)

            sitemap[language_code] = []
            sorted_page_file_names = sorted(os.listdir(content_path))
            sorted_page_file_names = [file for file in sorted_page_file_names if file.endswith('.html')]
            for i, current_page_file_name in enumerate(sorted_page_file_names):

                if current_page_file_name.endswith(".html"):
                    logging.debug(f"== -> File: {current_page_file_name} loaded. ==")

                    previous_page_file_name = sorted_page_file_names[i - 1] if i > 0 else None
                    next_page_file_name = sorted_page_file_names[i + 1] if i < len(sorted_page_file_names) - 1 else None

                    page_path = os.path.join(content_path, current_page_file_name)
                    localization_path = f"{os.path.splitext(page_path)[0]}_localization.json"
                    translation_dict = json.load(open(localization_path))
                    logging.debug("-> Localization for page loaded. :" + localization_path)

                    page_content = translate_text(Path(page_path).read_text(), translation_dict, language_code)
                    logging.debug("-> Page localized.")

                    content_copy = apply_substitutions(template_html, build_config, translation_dict, language_code, general_localization, page_content, current_page_file_name, previous_page_file_name, next_page_file_name)

                    content_copy = translate_text(content_copy, general_localization, language_code)

                    translated_filename = translation_dict["filename"][language_code]
                    output_file = language_path / f"{use_unidecode(translated_filename)}.html"
                    with open(output_file, 'w') as outfile:
                        outfile.write(content_copy)
                    logging.debug(f"-> {translated_filename} saved.")

                    sitemap[language_code].append(output_file)

        logging.info("Iteration finished.")

        create_sitemap(sitemap, build_config)

if __name__ == "__main__":
    build_sites()