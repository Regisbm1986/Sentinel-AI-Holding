import subprocess


def run_nikto(target, executor):

    clean_target = (
        target
        .replace("https://", "")
        .replace("http://", "")
        .split("/")[0]
    )

    cmd_nikto = [
        "nikto",
        "-h", clean_target,
        "-Tuning", "1,2,3,4,b,x",
        "-evasion", "1,5",
        "-custom-header",
        "User-Agent: Mozilla/5.0"
    ]

    executor(cmd_nikto, "Nikto-Warfare")
