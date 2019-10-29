import clr
clr.AddReference("System.Net")
clr.AddReference("Scripting")

from Scripting import *

test = Product.Attributes.GetByName('SOL_NeedMaX')

