def SplicingSql(args, comma, kw={}, *ignores):
    for k, v in kw.items():
        if k in ignores:
            continue         
        args, comma = SplicingDebris(args, comma, k, v)
    return args, comma

def SplicingDebris(args, comma, k, v):
    if not v:
            return args, comma
    if isinstance(v, int):
        args = "%s %s %s = %s"%(args, comma, k, v)
    if isinstance(v, str):
        args = "%s %s %s = '%s'"%(args, comma, k, v)
    if  isinstance(v, bool):
        args = "%s %s %s = %s"%(args, comma, k, v)
    if isinstance(v, float):
        args = "%s %s %s = %s"%(args, comma, k, v)
    return args, parseComma(comma)
    

def parseComma(comma=''):
    if comma.upper() == "WHERE":
        comma ="AND"
    if not comma:
        comma="AND"
    if comma.upper()=="SET":
        comma=','
    return comma
        