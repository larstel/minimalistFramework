def build_meta_tags(build_config, page_file_name):
    return '<meta name="robots" content="noindex">' if page_file_name in build_config["noindex"] else ''
