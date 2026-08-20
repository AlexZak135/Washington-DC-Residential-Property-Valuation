# Title: Washington, DC Residential Property Valuation Analysis
# Author: Alexander Zakrzeski
# Date: August 19, 2026

from datetime import date
import polars as pl

houses = (
    pl.read_parquet("data/raw/CAMA-Houses.parquet")
      .rename(str.lower)
      .rename({"saledate": "sale_date", 
               "intwall_d": "floor_d",
               "usecode": "use_code", 
               "landarea": "land_area"})
      .drop("objectid", "heat", "style", "struct", "extwall", "roof", "intwall",
            "gis_last_mod_dttm")
    )

houses = (
    houses.filter()
          .with_columns(
              pl.col("ssl").str.replace(r"\s+", " ")             
              )
    )



houses = houses.with_columns(pl.col("sale_date").str.to_datetime("%Y/%m/%d %H:%M:%S%#z", strict = True).dt.date())
houses = houses.with_columns(pl.col("sale_date").dt.year().alias("sale_year"))
houses = houses.with_columns(pl.col("qualified").str.strip_chars_end())
houses = houses.filter(pl.col("ayb").is_between(1750, 2026))
houses = houses.filter((pl.col("ayb") <= pl.col("yr_rmdl")) | pl.col("yr_rmdl").is_null())
houses = houses.filter(pl.col("ayb") <= pl.col("sale_year"))
houses = houses.filter((pl.col("yr_rmdl") <= pl.col("sale_year")) | pl.col("yr_rmdl").is_null())
houses = houses.filter(pl.col("sale_date").is_between(date(2022, 8, 1), date(2026, 7, 31)))
houses = houses.filter(pl.col("qualified") == "Q")
houses = houses.filter(pl.col("bldg_num") == 1)
houses = houses.filter(~pl.col("style_d").is_in(["No Data", "Outbuildings", "Vacant"]) & pl.col("style_d").is_not_null())
houses = houses.with_columns(pl.col("ssl").str.replace(r"\s+", " "))
houses = houses.with_columns(pl.when(pl.col("yr_rmdl").is_not_null()).then(1).otherwise(0).alias("rmdl"))

"bathrm"
"hf_bathrm"
"heat_d"
"ac"
"num_units"
"rooms"
"bedrm"
"ayb"
"yr_rmdl"
"eyb"
"stories"
"sale_date"
"price"
"qualified"
"sale_num"
"gba"
"bldg_num"
"style_d"
"struct_d"
"grade"
"grade_d"
"cndtn"
"cndtn_d"
"extwall_d"
"roof_d"
"floor_d"
"kitchens"
"fireplaces"
"use_code"
"land_area"