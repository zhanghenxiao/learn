"失败"
import  time, base64, string
from _md5 import md5
def makeSessionId(st):
    m = md5.new()
    m.update('this is a test of the emergency broadcasting system')
    m.update(str(time.time()))
    m.update(str(st))
    return string.replace(base64.encodestring(m.digest())[:-3], '/', '/span>')

def makeSessionId_nostring(st):
    m = md5.new()
    m.update('this is a test of the emergency broadcasting system')
    m.update(str(time.time()))
    m.update(str(st))
    return base64.encodestring(m.digest())[:-3].replace('/', '/span>')
makeSessionId('ftifo')
makeSessionId_nostring('13123')