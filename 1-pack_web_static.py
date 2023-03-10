#!/usr/bin/python3
"""
 module
"""
from fabric.api import local

def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    tgz_file = "versions/web_static_$(date '+%Y%m%d%H%M%S').tgz"
    try:
        local("tar -czvf {} web_static". format(tgz_file))
        return tgz_file
    except:
        return None