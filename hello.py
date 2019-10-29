import clr
clr.AddReference("System.Net")
from System.Net import CookieContainer
from System.Net import Cookie
from System.Net import WebRequest
from System.Net import HttpWebResponse

Trace.Write("Hello, world")
for x in range(1,5):
  Trace.Write(x)
Trace.Write("Success")
