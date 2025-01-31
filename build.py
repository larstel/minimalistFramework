from pathlib import Path
from distutils.dir_util import copy_tree
from utils.unicode import *
from utils.substitutions import *
from utils.logging import *
from utils.sitemap import *

def build_sites():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print(os.path.dirname(os.path.realpath(__file__)))
    build_config = json.load(open("../buildConfig.json"))
    Path("./build").mkdir(exist_ok=True)
    copy_tree("../additionalFilesForServer", "./build")
    general_localization = json.load(open("../" + build_config["contentTemplatesPath"] + "localization.json"))
    template_html = Path("../template.html").read_text()

    sitemap = {}

    for language_code in build_config["availableLanguages"]:
        logging.info(f"==== Start building pages for the language: {language_code} ====")

        language_path = Path(f"./build/{language_code}/{use_unidecode(general_localization['language'][language_code])}")
        language_path.mkdir(parents=True, exist_ok=True)
        logging.info("-> Folder created")

        content_path = f"../{build_config['contentTemplatesPath']}"

        sitemap[language_code] = []
        for page_file_name in sorted(os.listdir(content_path)):
            if page_file_name.endswith(".html"):
                logging.info(f"== -> File: {page_file_name} loaded. ==")

                page_path = os.path.join(content_path, page_file_name)
                localization_path = f"{os.path.splitext(page_path)[0]}_localization.json"
                translation_dict = json.load(open(localization_path))
                logging.info("-> Localization for page loaded. :" + localization_path)

                page_content = translate_text(Path(page_path).read_text(), translation_dict, language_code)
                logging.info("-> Page localized.")

                content_copy = apply_substitutions(template_html, build_config, translation_dict, language_code, general_localization, page_content, page_file_name)

                content_copy = translate_text(content_copy, general_localization, language_code)

                translated_filename = translation_dict["filename"][language_code]
                output_file = language_path / f"{use_unidecode(translated_filename)}.html"
                with open(output_file, 'w') as outfile:
                    outfile.write(content_copy)
                logging.info(f"-> {translated_filename} saved.")

                sitemap[language_code].append(output_file)

    create_sitemap(sitemap, build_config)

if __name__ == "__main__":
    build_sites()