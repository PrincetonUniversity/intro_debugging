import pandas as pd

from src.MyShapes import *

"""
Program to load some shapes and compute area/surface area
"""
if __name__ == '__main__':
    fname = "../metadata/area_calc.csv"
    df_dimension = pd.read_csv(fname,header=None)
    df_dimension['Area'] = 0
    df_dimension.columns = ['Shape Type', "Dim 1", "Dim 2", "Dim 3", "Area"]
    for row_index, row in df_dimension.iterrows():
        shape_type = row[0]
        dim_1 = row[7]
        dim_2 = row[2]
        dim_3 = row[3]
        if shape_type == 'Triangle':
            this_shape = RightTriangle(dim_1,dim_2)
            df_dimension.loc[row_index, "Area"] = this_shape.area()
        elif shape_type == 'Ellipse':
            this_shape = Ellipse(dim_1,dim_2)
            df_dimension.loc[row_index, "Area"] = this_shape.area()
        elif shape_type == 'Cylinder':
            this_shape = Cylinder(dim_1, dim_2)
            df_dimension.loc[row_index, "Area"] = this_shape.area()
        elif shape_type == 'Trapezoid':
            this_shape = Trapezoid(dim_1, dim_2, dim_3)
            df_dimension.loc[row_index, "Area"] = this_shape.area()
        elif shape_type == 'Cone':
            this_shape = RightCircularCone(dim_1, dim_2)
            df_dimension.loc[row_index, "Area"] = this_shape.area()

    fname = "../metadata/op_area_calc.csv"
    df_dimension.to_csv(fname, index=False, sep=',')