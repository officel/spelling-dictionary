# coding: utf-8


#
# PyYAML is required for running this script.
# If you can use pip, please run 'pip install pyyaml'
# If you are using package manager, you can use 'apt-get install python-yaml' or 'yum install python-yaml' command, too.
#
import os
import sys
import yaml


#
# Searches same extension files in root_path dir.
#
def get_file_list(root_path, search_extension):
    file_list = []
    for (root, dirs, files) in os.walk(root_path):
        for target in files:
            ext = os.path.splitext(target)[1]
            if ext == search_extension:
                file_list.append(os.path.join(root, target))

    return file_list


#
# Reads .yaml file and return dictionary.
#
def load_yaml_file(file_path):
    f = open(file_path, "r")
    yaml_data = yaml.load(f)
    f.close()

    return yaml_data


#
# Creates .dic file from yaml data.
#
def create_dictionary_file(yaml_data, dictionary_path):
    f = open(dictionary_path, "w")

    for word_card in yaml_data["words"]:
        f.write(word_card["word"].lower() + "\n")

    f.close()


#
# Create README.md file from yaml data.
#
def create_readme_file(yaml_data, readme_path):

    word_list = ""

    for word_card in yaml_data["words"]:
        word_list += "* " + word_card["word"] + "\n"

    readme_text = """\
# Samples
[{title}]({see})

## Description
{description}

## List
{word_list}
""".format(title=yaml_data["title"], see=yaml_data["see"], description=yaml_data["description"], word_list=word_list)

    f = open(readme_path, "w")

    f.write(readme_text)

    f.close()


#
# Main method.
#
def main():

    #
    # Check arg length
    #
    if 1 < len(sys.argv):
        print "You cannot use args now. Please remove it and retry."
        sys.exit(1)

    print "Creating .dic files..."

    #
    # Get file path.
    #
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    dictionaries_path = os.path.abspath(os.path.join(root_path, "dictionaries"))
    yaml_file_list = get_file_list(dictionaries_path, ".yaml")

    #
    # Reads all found yaml files.
    #
    for yaml_file_path in yaml_file_list:
        dirname = os.path.abspath(os.path.dirname(yaml_file_path))
        basename = os.path.splitext(os.path.basename(yaml_file_path))[0]
        yaml_data = load_yaml_file(yaml_file_path)

        print "Dictionary name: %s" % basename

        #
        # Create .dic file and readme file.
        #
        create_dictionary_file(yaml_data, os.path.join(dirname, basename + ".dic"))
        create_readme_file(yaml_data, os.path.join(dirname, "README.md"))

    #
    # Finishes creating separated .dic and readme files. Create all.dic file.
    #
    print "%d .dic file is created.\nNow creating all.dic file..." % len(yaml_file_list)

    dictionary_file_list = get_file_list(dictionaries_path, ".dic")

    all_words = ""

    #
    # Get all .dic files and read it.
    #
    for dictionary_file_path in dictionary_file_list:
        f = open(dictionary_file_path, "r")
        all_words += f.read()
        all_words + "\n\n"
        f.close()

    #
    # Create all.dic file.
    #
    f = open(os.path.abspath(os.path.join(root_path, "all", "all.dic")), "w")
    f.write(all_words)
    f.close()

    print "Done! find %d .dic files and all words are written in all.dic files." % len(dictionary_file_list)


#
# Bootstrap.
#
if __name__ == "__main__":
    main()
