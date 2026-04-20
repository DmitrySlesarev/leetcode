def os_path(disk, *args, sep='\\', **kwargs ):
    print(kwargs)
    args = (disk, ) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [x.strip() for x in args]
    path = sep.join(args)
    return path


p = os_path("F:", "  ~coursera.org",
            "Kind Kind Python   ",
            "39\\p39. Functions.docx",
            sep='/',
            trim=Trueexe)
print(p)