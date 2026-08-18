# Title: Washington, DC Residential Property Valuation Analysis
# Author: Alexander Zakrzeski
# Date: August 17, 2026

import polars as pl

houses = pl.read_parquet("data/raw/CAMA-Houses.parquet")
houses = houses.rename(str.lower)
houses = houses.rename({"intwall_d": "floor_d"})
houses = houses.drop("objectid", "heat", "style", "struct", "grade", "cndtn", 
                     "extwall", "roof", "intwall", "gis_last_mod_dttm")
houses = houses.with_columns(pl.col("ssl").str.replace(r"\s+", " "))



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
# EXTWALL_D - String
# ROOF_D - String
# INTWALL_D - String
# KITCHENS - Int64
# FIREPLACES - Int64
# USECODE - Int64
# LANDAREA - Int64