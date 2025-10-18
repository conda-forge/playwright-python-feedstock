from subprocess import call
import sys
import shutil

from playwright._impl import _driver as d

SCRIPTS = [
    ([shutil.which("playwright"), "install", "--help"], None),
    ([*d.compute_driver_executable(), "--version"], d.get_driver_env()),
]


def check(args: list[str], env: dict[str, str] | None=None) -> int:
    print("\n>>>", *args, flush=True)
    rc = call(args, env=env)
    print("<<<", rc, "\n", flush=True)
    return rc


if __name__ == "__main__":
    sys.exit(max(check(cmd, env) for cmd, env in SCRIPTS))
