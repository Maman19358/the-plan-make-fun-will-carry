"""
Module for publishing the make.fun bounty entry plan in public.
Second revision pass: structured with clean helper functions and robust path resolution.
"""

import os
from pathlib import Path


def resolve_output_dir() -> Path:
    """Resolve the target output directory from environment or default path."""
    output_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_env:
        return Path(output_env)
    return Path("/output")


def main() -> None:
    output_dir = resolve_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    target_file = output_dir / "entry.txt"
    
    plan_text = "Day 1: find 500 dentists paying for Google Ads with no landing page. Email 25/day offering a $79 AI-built landing page + SEO audit, delivered in 2 hours, paid via Stripe. Close 8 in 30 days = $632. Spend $50 on ads to the same offer. Net $582."
    target_file.write_text(plan_text, encoding="utf-8")


if __name__ == "__main__":
    main()
