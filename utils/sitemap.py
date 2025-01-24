import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

def create_sitemap(pages_dict, build_config):
    current_date = datetime.now().strftime('%Y-%m-%d')

    urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9",
                        xmlns_xhtml="http://www.w3.org/1999/xhtml")

    num_pages = len(next(iter(pages_dict.values())))

    for i in range(num_pages):
        url = ET.SubElement(urlset, 'url')

        loc = ET.SubElement(url, 'loc')
        loc.text = f'https://{build_config["domain"]}/{str(pages_dict[build_config["mainLanguage"]][i]).replace("build/", "")}'

        lastmod = ET.SubElement(url, 'lastmod')
        lastmod.text = current_date

        for language, pages in pages_dict.items():
            if language != 'en':  # Skip the main English page
                link = ET.SubElement(url, '{http://www.w3.org/1999/xhtml}link')
                link.set('rel', 'alternate')
                link.set('hreflang', language)
                link.set('href', f'https://{build_config["domain"]}/{str(pages[i]).replace("build/", "")}')

    tree = ET.ElementTree(urlset)

    output_path = './build/sitemap.xml'
    tree.write(output_path, encoding='UTF-8', xml_declaration=True)

    print(f"Sitemap successfully written to {output_path}")