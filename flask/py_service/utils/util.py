def SplicingSql(args, comma, object={}, *ignores):
    for k, v in object.items():
        for ingore in ingores:
            if k==ingore:
                continue
        SplicingDebris(args, comma, k, v)
        pass


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
        