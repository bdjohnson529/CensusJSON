"""
CensusTracts.py
=====================
Functions to filter GeoJSON data
"""

import json
import pandas as pd

def filterGeoJSON(df, filepath):
	"""
	Filter GeoJSON to tracts selected in df.
	Columns = [['TractID', 'Color', 'County', 'Population', ...]]
	:param df: Informational dataframe
	:type df: Pandas dataframe
	"""

	# convert df to dict
	d_selected = df.set_index('TractID').to_dict('index')

	# read in raw data
	with open(filepath) as f:
		data = json.load(f)

	# generate lookup index
	lkup_ix = {}

	for i in range(len(data['features'])):
		item = data['features'][i]
		tbl = item['properties']['description']
		df = pd.read_html(tbl)[0]
		tractID = df['Attributes.1'][4]
		
		lkup_ix[tractID] = i
		

	outputFeatures = []

	# generate new JSON dataset
	for x in d_selected:
		ix = lkup_ix[x]

		# info to be displayed
		info = d_selected[x]
		county = info['County']
		pop = info['Population']
		color = info['Color']
		
		feature = data['features'][ix]

		d = {}
		
		d['type'] = feature['type']
		
		# properties of JSON feature
		d['properties'] = { "color": color,
							"population": pop,
							"county": county }
		
		d['geometry'] = feature['geometry']
		d['geometry'] = feature['geometry']
		
		outputFeatures.append(d)

	newData = {'type': 'FeatureCollection',
				'features': outputFeatures}

	return newData