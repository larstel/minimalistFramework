def build_localization_options(build_config, language_code, general_localization, translation_dict):
    localization_content = ''
    for available_language_code in build_config["availableLanguages"]:
        if available_language_code != language_code:
            localization_content += f'<button onclick="window.location.href=\'file:///Users/lars/Documents/GitRepos/Grammatikson/minimalist/build/{available_language_code}/{general_localization["language"][available_language_code]}/{translation_dict["filename"][available_language_code]}.html\';"><span class="header-button">{available_language_code.upper()}</span></button>'
    return localization_content