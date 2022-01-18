## JsonConfigParser
A simple program that simplifies the use of JSON as config files

# Example Snippet

```python
import jsonconfig

config = jsonconfig.JsonConfig("file_path.json", keep_structure=True) 
# if keep_structure == True it will keep the structure of the config file when writing to it
# keep_structure is default False

config.new_section("section_name")
config.new_variable("section_name", "variable_name", "value")

print(config.get_variable("section_name", "variable_name"))
print(config.get_section("section_name"))
```

# Functions 

```python
set_variable(section_name, variable_name, value)# Changes the value of a variable in a specified section
new_section(section_name) # Creates a new section
new_variable(section_name, variable_name, value) # Creates a new variable in a specified section
get_section(section_name) # Gets all the variables and their values in a section
get_variable(section_name, variable_name) # Gets a variable in a specified section
delete_section(section_name) # Deletes a section and all its variables and their values
delete_variable(section_name, variable_name) # Deletes a variable and its value
```

# File Structuring 

To be able to use this program you need to follow a simple file structure (The structure is basically the same as .ini files).
You can have as many sections and variables as you like

```
{
    "sectionOne": {
        "variableOne": false,
        "variableTwo": 123,
        "variableThree": "string"
    },
    "sectionTwo": {
        "variableOne": false,
        "variableTwo": 123,
        "variableThree": "string"
    },
    "sectionThree": {
        "variableOne": false,
        "variableTwo": 123,
        "variableThree": "string"
    }
}
```

