"""
datasphere_lineage
==================

Field-level and object-level data lineage resolver for SAP Datasphere
exports (Analytic/Consumption Models, Graphical Views, local tables, and
Replication Flows), enriched with S/4 ABAP table/field metadata via CDS
view DDL and a plain ABAP data dictionary export.

Every edge in the lineage graph this package reports comes from explicit
structure in the exported JSON/DDL - never from matching field names
across unrelated objects.

Typical usage is via the command line (see :mod:`datasphere_lineage.cli`),
but the resolution pipeline is also importable for programmatic use.
"""

from __future__ import annotations

__version__ = "2.0.0"

__all__ = ["__version__"]
