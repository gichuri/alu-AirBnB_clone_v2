from fabric.api import local

def do_pack():
    local("mkdir -p versions")
    tgz_file = "versions/web_static_$(date '+%Y%m%d%H%M%S').tgz"
    try:
        local("tar -czvf {} web_static". format(tgz_file))
        return tgz_file
    except:
        return None