import clr
clr.AddReference("System.Net")
clr.AddReference("Scripting")
from System.Net import CookieContainer
from System.Net import Cookie
from System.Net import WebRequest
from System.Net import HttpWebResponse
import Scripting

test = Scripting.Product.Attr('SOL_NeedMaX').GetValue()

