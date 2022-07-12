import plotly.graph_objects as go
import urllib, urllib.request, json

# Original url
# 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
with open("data.json", "r") as f:
    data = json.load(f)

# Show json data
import pprint
pprint.pprint(data)

# Configure plotly diagram
# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                    for src in data['data'][0]['link']['source']]

# Format label as - <label> <total> 
labels = data['data'][0]['node']['label']
values = data['data'][0]['link']['value']
targets = data['data'][0]['link']['target']
sources = data['data'][0]['link']['source']

## Aggregate target_totals for each label
target_totals = {}
for i, target in enumerate(targets):
    if target not in target_totals:
        target_totals[target] = values[i]
    else:
        target_totals[target]+= values[i]

## Aggregate source_totals for each label
source_totals = {}
for i, source in enumerate(sources):
    if source not in source_totals:
        source_totals[source] = values[i]
    else:
        source_totals[source]+= values[i]

## Combine the label with the source_totals 
for i, label in enumerate(labels):
    if i in target_totals:
        labels[i] = f"{labels[i]} {target_totals[i]}"
    else:
        labels[i] = f"{labels[i]} {source_totals[i]}"

print("labels", labels)
print("target_totals", target_totals)
print("source_totals", source_totals)

# Build Sankey diagram
fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    # Define nodes
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  labels,
      color =  data['data'][0]['node']['color']
    ),
    # Add links
    link = dict(
        source =  data['data'][0]['link']['source'],
        target =  data['data'][0]['link']['target'],
        value =  data['data'][0]['link']['value'],
        label =  data['data'][0]['link']['label'],
        color =  data['data'][0]['link']['color']
))])

fig.update_layout(
    title_text="Craiglist Housing Search<br>1 bedroom, 1 bath",
    font_size=10
)

# Show the diagram
fig.show()

# Save as html
filename = "./assets/sankey.html"
fig.write_html(filename)
