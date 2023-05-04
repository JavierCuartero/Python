import ifcopenshell
import ifcopenshell.util.element as Element
import ifcopenshell.util.placement
import pandas as pd


# Importing the IFC file

file_path = "C:\IfcOpenShell\TestHouse.ifc"
csv_export_path = file_path.split(".")[0] + ".csv"

ifc_file = ifcopenshell.open(file_path)

# Prints out all items in a row
#products = ifc_file.by_type('IfcProduct')
#for product in products:
#    print(product.is_a())
#    print(product)


def get_objects_data_by_class(file, class_type):
    """Gets object atributes based on a given IFC Class"""
    def add_pset_attributes(psets):
        for pset_name, pset_data in psets.items():
            for property_name in pset_data.keys():
                pset_attributes.add(f"{pset_name}.{property_name}")

    pset_attributes = set()
    objects_data = []
    ifc_object = file.by_type(class_type)

    for obj in ifc_object:  
        psets = Element.get_psets(obj, psets_only=True)
        add_pset_attributes(psets)
        qtos =  Element.get_psets(obj, qtos_only=True)
        add_pset_attributes(qtos)
        matrix = ifcopenshell.util.placement.get_local_placement(obj.ObjectPlacement)
        global_coordinates = matrix[:,3][:3]
        x_coordinate = matrix[:,3][0]
        y_coordinate = matrix[:,3][1]
        z_coordinate = matrix[:,3][2]

        object_id = obj.id()
        objects_data.append({
            "ExpressId" : obj.id(),
            "GlobalId" : obj.GlobalId,
            "Class" : obj.is_a(),
            "PredefinedType" : Element.get_predefined_type(obj),
            "Name" : obj.Name,
            "Level" : Element.get_container(obj).Name if Element.get_container(obj) else "",
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate,
            "z_coordinate": z_coordinate,
            "Type" :  Element.get_type(obj).Name if Element.get_type(obj) else "",
            "Material" : Element.get_material(obj).Name if Element.get_material(obj) else "",
            "QuantitySets" : qtos,
            "PropertySets" : psets
        })
    return objects_data, list(pset_attributes)


def get_attribute_value(object_data, attribute):
    """Get Pset attributes values"""
    if "." not in attribute:
        return object_data[attribute]
    elif "." in attribute:
        pset_name = attribute.split(".",1)[0]
        prop_name = attribute.split(".",-1)[1]
        if pset_name in object_data["PropertySets"].keys():
            if prop_name in object_data["PropertySets"][pset_name].keys():
                return object_data["PropertySets"][pset_name][prop_name]
            else:
                return None
        if pset_name in object_data["QuantitySets"].keys():
            if prop_name in object_data["QuantitySets"][pset_name].keys():
                return object_data["QuantitySets"][pset_name][prop_name]
            else:
                return None
    else:
        return None


# Input an Ifc class
#   IfcBuildingElement will get all elements in our file
#   IfcSpace will get all rooms
#   IfcBuilding will get Project information
#   IfcSite 
#   IfcProduct

data, pset_attributes = get_objects_data_by_class(ifc_file, "IfcBuildingElement")


attributes = ["ExpressId", "GlobalId", "Class","PredefinedType", "Name", "Level", "x_coordinate", "y_coordinate", "z_coordinate", "Type", "Material"] + pset_attributes

pandas_data = []
for object_data in data:
    row = []
    for attribute in attributes:
        value = get_attribute_value(object_data, attribute)
        row.append(value)
    pandas_data.append(tuple(row))


dataframe = pd.DataFrame.from_records(pandas_data, columns=attributes)

# print(dataframe)


## Export to csv
dataframe.to_csv(csv_export_path)

print("csv exported!")