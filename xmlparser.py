import os
import sys
import json
from xml.etree import ElementTree as et


class XmlParser:

    def __init__(self):
        self.xml_file_name = sys.argv[1]
        self.json_file_name = sys.argv[2]
        self.xml_file_path = 'resources/' + self.xml_file_name
        self.json_file_path = 'resources/' + self.json_file_name

        final_xml = self.replace_tags(self.xml_file_path,self.json_file_path)
        final_xml.write('resources/' + self.xml_file_name + '_modified')

    def replace_tags(self,xml_path,json_path):

        tree = et.parse(xml_path)
        json_keywords = json.load(open(json_path))
        for k, v in json_keywords.items():

            x = tree.findall('.//' + k)
            for tag in x:

                if not (tag.text.strip() == v.strip()):
                    tag.text = v
        return tree


if __name__ == "__main__":
    XmlParser()






















