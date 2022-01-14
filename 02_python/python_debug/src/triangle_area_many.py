from MyShapes import RightTriangle
import random
import pandas as pd

def create_10000_traingles(op_file):
  df_triag = pd.DataFrame(columns=['name','base','hieght'])
  for x in range(10000):
    base = random.randint(10, 100)
    hieght = random.randint(10, 100)
    df_triag = df_triag.append(pd.Series([x,base,hieght],index=df_triag.columns), ignore_index=True)
  df_triag.to_csv(op_file,index=False)

def sum_triangles(inp_file):
  df_triag = pd.read_csv(inp_file)
  sum_area = 0
  for index, row in df_triag.iterrows():
    name = row[0]
    base = float(row[1])
    hieght = float(row[2])
    mytriangle = RightTriangle(base, hieght)
    sum_area = sum_area + mytriangle.area()
  print("triangle area sum = {} ".format(sum_area))

"""
A program to sum the area of all the triangles in 10000_triangle_area_calc.csv
"""
if __name__ == '__main__':
  sum_triangles('../metadata/10000_triangle_area_calc.csv')


