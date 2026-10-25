"""Allows ``python -m datasphere_lineage`` as an alternative to the
installed ``datasphere-lineage`` console script."""

from .cli import main

if __name__ == "__main__":
    main()
