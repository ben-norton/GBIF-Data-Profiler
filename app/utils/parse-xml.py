from lxml import etree
import glob, os
import globals as cfg

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

#get_meta('0052489-241126133413365')

def get_dwc_terms(str):
    archive_code = str
    root_dir = cfg.get_project_root()
    print(root_dir)
    source_file = root_dir + '/source-data/' + archive_code + '/meta.xml'

    with open(source_file) as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)
    for elem in root.getchildren():
        if(elem.tag == '{http://rs.tdwg.org/dwc/text/}core'):
            for child in elem.getchildren():
                if 'term' in child.attrib:
                    term = child.attrib['term']
                    print(term)

get_dwc_terms('0052489-241126133413365')