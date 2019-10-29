import clr
clr.AddReference("System.Net")
from System.Net import CookieContainer
from System.Net import Cookie
from System.Net import WebRequest
from System.Net import HttpWebResponse
from System.Diagnostics import Trace

test = Product.Attr('SOL_NeedMaX').GetValue()

Trace.Write("Hello, world")
a = 0
for x in range(1,5):
  a = a + 1
Trace.Write("Success")
