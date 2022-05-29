
def get_default_archive_methods():
    return [
        'favicon',
        'headers',
        'singlefile',
        'pdf',
        'screenshot',
        'dom',
        'wget',
        'title',                   # keep title and readability below wget and singlefile, as it depends on them
        'readability',
        'mercury', 
        'git', 
        'media', 
        'archive_org'
    ]
