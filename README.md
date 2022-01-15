## JsonConfigParser
A simple program that simplifies the use of JSON as config files

# Example Snippet

```python
from jsonconfig import JsonConfig

config = JsonConfig("file_path.json", keep_structure=True) # if keep_structure == True it will keep the structure of the config file when writing to it

config.new_section("section_name") # creates a new section
config.set_variable("section_name", "variable_name", "value") # creates a new variable and assigns it a value 

print(config.get_variable("section_name", "variable_name") # prints the value of a variable
print(config.get_section("section_name") # prints all variables and their values in a section
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

