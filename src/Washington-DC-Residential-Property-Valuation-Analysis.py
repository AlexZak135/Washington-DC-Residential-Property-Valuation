# Title: Washington, DC Residential Property Valuation Analysis
# Author: Alexander Zakrzeski
# Date: August 17, 2026

from datetime import date
import polars as pl

houses = pl.read_parquet("data/raw/CAMA-Houses.parquet")
houses = houses.rename(str.lower)
houses = houses.rename({"saledate": "sale_date",
                        "intwall_d": "floor_d"})
houses = houses.drop("objectid", "heat", "style", "struct", "grade", "cndtn", 
                     "extwall", "roof", "intwall", "gis_last_mod_dttm")
houses = houses.with_columns(pl.col("sale_date").str.to_datetime("%Y/%m/%d %H:%M:%S%#z", strict = True).dt.date())
houses = houses.with_columns(pl.col("sale_date").dt.year().alias("sale_year"))
houses = houses.with_columns(pl.col("qualified").str.strip_chars_end())
houses = houses.filter(pl.col("ayb").is_between(1750, 2026))
houses = houses.filter((pl.col("ayb") <= pl.col("yr_rmdl")) | pl.col("yr_rmdl").is_null())
houses = houses.filter(pl.col("ayb") <= pl.col("sale_year"))
houses = houses.filter((pl.col("yr_rmdl") <= pl.col("sale_year")) | pl.col("yr_rmdl").is_null())
houses = houses.filter(pl.col("sale_date").is_between(date(2021, 8, 1), date(2026, 7, 31)))
houses = houses.filter(pl.col("qualified") == "Q")
houses = houses.with_columns(pl.col("ssl").str.replace(r"\s+", " "))
houses = houses.with_columns(pl.when(pl.col("yr_rmdl").is_not_null()).then(1).otherwise(0).alias("rmdl"))
houses = houses.drop("yr_rmdl")



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