import clr
clr.AddReference("System.Net")
clr.AddReference("Scripting")
from Scripting import *

test = Product.Attr('SOL_NeedMaX').GetValue()

