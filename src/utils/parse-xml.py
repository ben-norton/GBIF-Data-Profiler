from lxml import etree
import glob, os
import config as cfg

def get_meta(str):
    archive_code = str
    root_dir = cfg.get_project_root()
    source_path = str(root_dir) + '/source-data/' + archive_code + '/dataset'
    os.chdir(source_path)
    for f in glob.glob("*.xml"):
        xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
        tree = etree.parse(
            f,
            parser=xml_parser
        )
        package_id = tree.xpath('/*/@packageId')[0]
        title = tree.xpath('//dataset/title[1]/text()')[0]
        doi_id = tree.xpath('//dataset/alternateIdentifier[1]')
        doi = 'https://doi.org/' + doi_id[0].text
        meta = {}
        meta['packageID'] = package_id
        meta['title'] = title
        meta['doi'] = doi

    return meta

