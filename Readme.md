

xmlparser.py:
This python script replaces the values of the tags in xml

running instructions:
python xmlparser.py <xml file name> <json file name>
xmlfile and jsonfile needs to be placed in resources folder

json file name  contains key value pairs with key as tag name and value as tag value.

If the tag value in xml is different from the value avialable in json ,python script
replaces the value with the one available in json .

This script goes into any depth of the xml to check the values.

