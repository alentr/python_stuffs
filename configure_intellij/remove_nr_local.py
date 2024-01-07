import xml.etree.ElementTree as ET

envs = [
    'NEW_RELIC_AGENT_ENABLED',
    'NEW_RELIC_APP_ID',
    'NEW_RELIC_APP_NAME',
    'NEW_RELIC_LICENSE_KEY'
]

xml_path = '../workspace.xml'
app_name = 'CallsRouterApplicationKt'


def xml_file_to_string(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Convert the root element and its children to a string
    return ET.tostring(root, encoding='utf-8').decode('utf-8')


def save_xml_to_file(xml_string, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(xml_string)


xml_string = xml_file_to_string(xml_path)

# Parse the XML string
xml = ET.fromstring(xml_string)

# Find the specified configuration element
config_element = xml.find(".//configuration[@name='" + app_name + "']")

if config_element is not None:
    # Check if <envs> element exists, create it if not
    envs_element = config_element.find("envs")
    if envs_element is None:
        envs_element = ET.SubElement(config_element, "envs")

    for env_to_remove in envs:
        env = envs_element.find(f".//env[@name='{env_to_remove}']")
        envs_element.remove(env)

    # Convert the modified tree back to a string
    modified_xml = ET.tostring(xml, encoding='utf-8').decode('utf-8')
    save_xml_to_file(modified_xml, xml_path)
else:
    print(f"Error: Configuration '{app_name}' not found in the XML.")
