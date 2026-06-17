import shlex

from backend.core.config import PYTHON_BIN
from dataclasses import dataclass

from backend.modules.beef.module import run_beef_daemon
from backend.modules.dagda.module import check_dagda_status, run_dagda
from backend.modules.enum4linux.module import run_enum4linux
from backend.modules.john.module import run_john_the_ripper
from backend.modules.kubehunter.module import run_kube_hunter
from backend.modules.nikto.module import run_nikto_api
from backend.modules.setoolkit.module import run_setoolkit_daemon
from backend.modules.spiderfoot.module import run_spiderfoot


@dataclass(frozen=True)
class ModuleDefinition:
    key: str
    title: str
    description: str
    mode: str
    fields: tuple


def get_module_definitions():
    return [
        ModuleDefinition(
            key="nikto",
            title="Nikto",
            description="Web server vulnerability scan.",
            mode="direct",
            fields=("target",),
        ),
        ModuleDefinition(
            key="spiderfoot",
            title="SpiderFoot",
            description="OSINT collection and analysis.",
            mode="executor",
            fields=("target",),
        ),
        ModuleDefinition(
            key="dagda",
            title="Dagda",
            description="Docker image analysis.",
            mode="direct",
            fields=("image_name",),
        ),
        ModuleDefinition(
            key="kubehunter",
            title="KubeHunter",
            description="Kubernetes remote assessment.",
            mode="executor",
            fields=("cluster_ip", "flags_extras"),
        ),
        ModuleDefinition(
            key="enum4linux",
            title="Enum4Linux",
            description="SMB enumeration.",
            mode="executor",
            fields=("target",),
        ),
        ModuleDefinition(
            key="john",
            title="John",
            description="Credential cracking workflow.",
            mode="executor",
            fields=("hash_text",),
        ),
        ModuleDefinition(
            key="beef",
            title="BeEF",
            description="Start the BeEF daemon.",
            mode="background",
            fields=(),
        ),
        ModuleDefinition(
            key="set",
            title="SET",
            description="Start the Social-Engineer Toolkit daemon.",
            mode="background",
            fields=(),
        ),
    ]


def _python_command(script):
    return f"{PYTHON_BIN} -c {shlex.quote(script)}"


def _build_module_goal(module_key, values):
    target = values.get("target")
    image_name = values.get("image_name")
    cluster_ip = values.get("cluster_ip")

    if module_key == "nikto":
        return f"Run Nikto against {target}"

    if module_key == "spiderfoot":
        return f"Run SpiderFoot against {target}"

    if module_key == "dagda":
        return f"Run Dagda against image {image_name}"

    if module_key == "kubehunter":
        return f"Run KubeHunter against cluster {cluster_ip}"

    if module_key == "enum4linux":
        return f"Run Enum4Linux against {target}"

    if module_key == "john":
        return "Run John against provided hashes"

    if module_key == "beef":
        return "Start BeEF daemon"

    if module_key == "set":
        return "Start SET daemon"

    raise ValueError(f"Unsupported module key: {module_key}")


def _build_module_command(module_key, values):
    target = values.get("target")
    image_name = values.get("image_name")
    cluster_ip = values.get("cluster_ip")
    flags_extras = values.get("flags_extras", "")
    hash_text = values.get("hash_text")

    if module_key == "nikto":
        script = f"""
from backend.modules.nikto.module import run_nikto_api
import json, sys
result = run_nikto_api({target!r})
print(json.dumps(result))
sys.exit(0 if result.get('status') == 'success' else 1)
""".strip()
        return _python_command(script)

    if module_key == "spiderfoot":
        script = f"""
import subprocess, sys
from backend.modules.spiderfoot.module import run_spiderfoot

def executor(command, label):
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.stdout:
        print(completed.stdout, end='')
    if completed.stderr:
        print(completed.stderr, end='', file=sys.stderr)
    if completed.returncode != 0:
        raise subprocess.CalledProcessError(completed.returncode, command, output=completed.stdout, stderr=completed.stderr)

run_spiderfoot({target!r}, executor)
""".strip()
        return _python_command(script)

    if module_key == "dagda":
        script = f"""
from backend.modules.dagda.module import run_dagda
import json, sys
result = run_dagda({image_name!r})
print(json.dumps(result))
sys.exit(0 if result.get('status') == 'success' else 1)
""".strip()
        return _python_command(script)

    if module_key == "kubehunter":
        script = f"""
import subprocess, sys
from backend.modules.kubehunter.module import run_kube_hunter

def executor(command, label):
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.stdout:
        print(completed.stdout, end='')
    if completed.stderr:
        print(completed.stderr, end='', file=sys.stderr)
    if completed.returncode != 0:
        raise subprocess.CalledProcessError(completed.returncode, command, output=completed.stdout, stderr=completed.stderr)

run_kube_hunter({cluster_ip!r}, executor, flags_extras={flags_extras!r})
""".strip()
        return _python_command(script)

    if module_key == "enum4linux":
        script = f"""
import subprocess, sys
from backend.modules.enum4linux.module import run_enum4linux

def executor(command, label):
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.stdout:
        print(completed.stdout, end='')
    if completed.stderr:
        print(completed.stderr, end='', file=sys.stderr)
    if completed.returncode != 0:
        raise subprocess.CalledProcessError(completed.returncode, command, output=completed.stdout, stderr=completed.stderr)

run_enum4linux({target!r}, executor)
""".strip()
        return _python_command(script)

    if module_key == "john":
        script = f"""
import subprocess, sys
from backend.modules.john.module import run_john_the_ripper

def executor(command, label):
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.stdout:
        print(completed.stdout, end='')
    if completed.stderr:
        print(completed.stderr, end='', file=sys.stderr)
    if completed.returncode != 0:
        raise subprocess.CalledProcessError(completed.returncode, command, output=completed.stdout, stderr=completed.stderr)

run_john_the_ripper({hash_text!r}, executor)
""".strip()
        return _python_command(script)

    if module_key == "beef":
        script = "from backend.modules.beef.module import run_beef_daemon\nrun_beef_daemon()"
        return _python_command(script)

    if module_key == "set":
        script = "from backend.modules.setoolkit.module import run_setoolkit_daemon\nrun_setoolkit_daemon()"
        return _python_command(script)

    raise ValueError(f"Unsupported module key: {module_key}")


def build_module_execution_task(module_key, values):
    definition = next((item for item in get_module_definitions() if item.key == module_key), None)

    if definition is None:
        raise ValueError(f"Unsupported module key: {module_key}")

    missing_fields = [field for field in definition.fields if not values.get(field)]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

    return {
        "type": "command",
        "module": module_key,
        "goal": _build_module_goal(module_key, values),
        "command": _build_module_command(module_key, values),
        "inputs": {field: values.get(field) for field in definition.fields},
    }


def build_module_execution_task_for_queue(module_key, values):
    return build_module_execution_task(module_key, values)


def execute_module(module_key, values, executor=None, logger=None):
    if module_key == "nikto":
        return run_nikto_api(values.get("target"))

    if module_key == "spiderfoot":
        return run_spiderfoot(values.get("target"), executor)

    if module_key == "dagda":
        return run_dagda(values.get("image_name"))

    if module_key == "kubehunter":
        return run_kube_hunter(
            values.get("cluster_ip"),
            executor,
            logger=logger,
            flags_extras=values.get("flags_extras", ""),
        )

    if module_key == "enum4linux":
        return run_enum4linux(values.get("target"), executor)

    if module_key == "john":
        return run_john_the_ripper(values.get("hash_text"), executor, logger=logger)

    if module_key == "beef":
        return run_beef_daemon(logger=logger)

    if module_key == "set":
        return run_setoolkit_daemon(logger=logger)

    raise ValueError(f"Unsupported module key: {module_key}")


def get_dagda_status():
    return check_dagda_status()
