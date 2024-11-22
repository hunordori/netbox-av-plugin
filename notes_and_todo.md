# Models

## AVInterface

To store port details that belong to a device.

| name | description |
|------|-------------|
|Medium| Type of the cable/connector|
|Video Signal Rate | Speed of the data transfer|
|Signal Type | Video, audio or data signal type|
|Signal Direction | input/output/configurable|
|Device | Parent field |

Detailed choices in choices.py file.

## AV cable

- [ ] Utilize Netbox's cables
- [ ] Add interface choices to Netbox' current model


# TO DO

## AV Interfaces

- [ ] add bulk import/export
- [ ] clean and finalize edit/list/detail views

## Cables

- [ ] create constrains (SDI port only with SDI cables)