"""Products namespace package with legacy aliases."""

import sys
from importlib import import_module
from typing import Dict


def _register_aliases(mapping: Dict[str, str]) -> None:
	for alias, target in mapping.items():
		if alias in sys.modules:
			continue
		module = import_module(target)
		sys.modules[alias] = module


_ALIASES = {
	"products.sentinel-career": "products.sentinel_career",
	"products.sentinel-os": "products.sentinel_os",
}

_register_aliases(_ALIASES)

