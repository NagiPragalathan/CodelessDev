import random
import re
import cssutils

# Load the CSS file
# with open('styles.css', 'r') as f:
#     css = f.read()

css = """
article p:first-of-type {
  color: red;
  font-size: 1.5em;
}"""

# Parse the CSS using cssutils
sheet = cssutils.parseString(css)

# Find all color values used in the CSS
colors = set()
for rule in sheet:
    for i in range(rule.style.length):
        key = rule.style.item(i)
        value = rule.style.getPropertyValue(key)
        if key.endswith('color') and value.startswith('#'):
            colors.add(value)

# Print the list of color values
print('Colors used in the CSS:')
for color in colors:
    print(color)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Second code >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Parse the CSS using cssutils
sheet = cssutils.parseString(css)

# List of named colors in CSS
named_colors = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon',
                'navy', 'olive', 'orange', 'purple', 'red', 'silver', 'teal', 'white', 'yellow']

# Find all named colors used in the CSS
used_colors = set()
for rule in sheet:
    for i in range(rule.style.length):
        key = rule.style.item(i)
        value = rule.style.getPropertyValue(key)
        if value in named_colors:
            used_colors.add(value)

# Print the list of named colors used in the CSS
print('Named colors used in the CSS:')
for color in used_colors:
    print(color)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> code for change the colors >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

css_content = """
article p:first-of-type {
  color: red;
  font-size: 1.5em;
}"""

# List of named CSS colors
named_colors = [
    "aliceblue",
    "antiquewhite",
    "aqua",
    "aquamarine",
    "azure",
    # ... add more named colors as needed
]

# Regular expression pattern to match CSS color values
color_pattern = r"#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})"

# Read the CSS file
with open("styles.css", "r") as f:
    css_content = f.read()

# Find all color values in the CSS file
colors = re.findall(color_pattern, css_content)

# Replace each color with a random named CSS color
for color in colors:
    if color.lower() not in named_colors:
        new_color = random.choice(named_colors)
        css_content = css_content.replace(f"#{color}", new_color)

# Write the updated CSS content to the file
with open("styles.css", "w") as f:
    f.write(str(css_content))
