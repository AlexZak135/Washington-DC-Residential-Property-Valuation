# Title: Washington, DC Residential Property Valuation Analysis
# Author: Alexander Zakrzeski
# Date: August 14, 2026

import polars as pl

houses = pl.read_parquet("data/raw/CAMA-Houses.parquet")
houses = houses.rename(str.lower)
houses = houses.drop("objectid", "heat", "style", "struct", "grade", "cndtn")

# SSL - String
# BATHRM - Int64
# HF_BATHRM - Int64
# HEAT_D - String 
# AC - String
# NUM_UNITS - Int64
# ROOMS - Int64
# BEDRM - Int64
# AYB - Int64
# YR_RMDL - Int64
# EYB - Int64
# STORIES - Float64
# SALEDATE - String
# PRICE - Int64
# QUALIFIED - String
# SALE_NUM - Int64
# GBA - Int64
# BLDG_NUM - Int64
# STYLE_D - String
# STRUCT_D - String
# GRADE_D - String
# CNDTN_D - String

# EXTWALL - Int64
# EXTWALL_D - String
# ROOF - Int64
# ROOF_D - String
# INTWALL - Int64
# INTWALL_D - String
# KITCHENS - Int64
# FIREPLACES - Int64
# USECODE - Int64
# LANDAREA - Int64
# GIS_LAST_MOD_DTTM - String
