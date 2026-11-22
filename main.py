"""Write the make.fun bounty plan text to the designated output directory."""

import os
from pathlib import Path

PLAN_TEXT = (
    "Day 1: find 100 local businesses paying for Google Ads but with no landing page. "
    "Email 10/day offering a $49 AI-built landing page + SEO audit, delivered in 2 hours, "
    "paid via Stripe. Close 4 in 30 days = $196. Spend $50 on ads to the same offer. Target $300."
)

def write_entry() -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(PLAN_TEXT, encoding="utf-8")

if __name__ == "__main__":
    write_entry()
