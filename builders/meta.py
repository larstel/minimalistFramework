def build_meta_tags(build_config, page_file_name):
    if(page_file_name in build_config["navigationBlacklist"]):
        return '<meta name="robots" content="noindex, nofollow">'
    else:
        return ''