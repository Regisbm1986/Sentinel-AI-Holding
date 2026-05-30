import os
import sys

def run_spiderfoot(target, executor):

    if target:

        sf_script = os.path.expanduser("~/spiderfoot/sf.py")

        if os.path.exists(sf_script):

            cmd_sf = [
                "/home/sentineladmin/sentinel-os/venv/bin/python",
                sf_script,
                "-t", "ALL",
                "-u", "all",
                "-q",
                "-s", target
            ]

            executor(cmd_sf, "SpiderFoot-OSINT")

        else:
            print("SpiderFoot não encontrado no servidor.")

    else:
        print("Nenhum alvo especificado.")
