from parkMoaApp.search import park_info_index
from django.db import models

# Create your models here.
# def indexing(self):
#     obj = park_info_index(
#     meta = {'Num': self.Num},
#     District = self.District,
#     Park_division = self.Park_division,
#     Park_name = self.Park_name,
#     Road_address = self.TeRoad_addressxt,
#     Parcel_address = self.Parcel_address,
#     Park_overview = self.Park_overview,
#     Park_area = self.Park_area,
#     Main_facility = self.Main_facility,
#     Sporting_goods = self.Sporting_goods,
#     Guidemap = self.Guidemap,
#     Direction = self.Direction,
#     Use_notes = self.Use_notes,
#     Image = self.Image,
#     Park_number = self.Park_number,
#     Latitude = self.Latitude,
#     Longitude = self.Longitude,
#     Shortcut = self.Shortcut,
#     Grade = self.Grade,
#     )
#     obj.save()
#     return obj.to_dict(include_meta=True)