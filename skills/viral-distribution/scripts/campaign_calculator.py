#!/usr/bin/env python3
"""
campaign_calculator.py - Model short-form viral campaign economics
and payout structures across Clipping, UGC, and Slideshow Syndication engines.
"""

import argparse
import sys

def calculate_clipping(target_views: int, cpm: float, bot_reserve_pct: float = 15.0) -> dict:
    """Calculate budget, spend, and reserves for a clipping campaign."""
    gross_spend = (target_views / 1000.0) * cpm
    bot_reserve = gross_spend * (bot_reserve_pct / 100.0)
    net_payout = gross_spend
    total_budget_needed = gross_spend + bot_reserve
    estimated_clippers = max(1, int(target_views / 25000))  # avg clipper delivers ~25k views
    return {
        "engine": "Clipping Campaign",
        "target_views": target_views,
        "cpm": cpm,
        "gross_spend": gross_spend,
        "bot_reserve": bot_reserve,
        "total_budget_needed": total_budget_needed,
        "estimated_clippers_needed": estimated_clippers,
        "cost_per_view": total_budget_needed / target_views if target_views else 0
    }

def calculate_ugc(target_views: int, base_fee: float, cpm: float, avg_views_per_video: int = 15000) -> dict:
    """Calculate creator fleet, base fees, and performance payouts for UGC."""
    num_videos = max(1, int(target_views / avg_views_per_video))
    total_base_spend = num_videos * base_fee
    performance_spend = (target_views / 1000.0) * cpm
    total_spend = total_base_spend + performance_spend
    effective_cpm = (total_spend / target_views) * 1000.0 if target_views else 0
    return {
        "engine": "UGC / AI-UGC Program",
        "target_views": target_views,
        "num_videos_required": num_videos,
        "base_fee_per_video": base_fee,
        "performance_cpm": cpm,
        "total_base_spend": total_base_spend,
        "performance_spend": performance_spend,
        "total_spend": total_spend,
        "effective_cpm": effective_cpm,
        "cost_per_view": total_spend / target_views if target_views else 0
    }

def calculate_slideshow(
    target_views: int,
    payout_100k: float = 100.0,
    payout_1m: float = 350.0,
    bonus_pct: float = 15.0,
    bot_reserve_pct: float = 10.0,
    avg_hit_views: int = 200000
) -> dict:
    """
    Calculate milestone syndication economics for TikTok/IG photo slideshows.
    0 to 100k views are unpaid ($0 hurdle). Posts crossing 100k unlock milestone
    bounties ($100 @ 100k, $350 @ 1M) plus surprise loyalty bonuses.
    """
    num_hits = max(1, int(target_views / avg_hit_views))
    # Blended milestone cost per qualifying post hitting ~avg_hit_views
    if avg_hit_views >= 1000000:
        base_payout_per_hit = payout_1m
    elif avg_hit_views >= 500000:
        base_payout_per_hit = payout_100k + ((payout_1m - payout_100k) * (avg_hit_views - 100000) / 900000.0)
    else:
        base_payout_per_hit = payout_100k

    gross_milestone_spend = num_hits * base_payout_per_hit
    loyalty_bonus_spend = gross_milestone_spend * (bonus_pct / 100.0)
    bot_reserve = gross_milestone_spend * (bot_reserve_pct / 100.0)
    total_spend = gross_milestone_spend + loyalty_bonus_spend + bot_reserve
    effective_cpm = (total_spend / target_views) * 1000.0 if target_views else 0

    return {
        "engine": "Slideshow Syndication",
        "target_views": target_views,
        "num_hits_required": num_hits,
        "avg_hit_views": avg_hit_views,
        "base_milestone_payout": gross_milestone_spend,
        "loyalty_bonus_spend": loyalty_bonus_spend,
        "bot_reserve": bot_reserve,
        "total_budget_needed": total_spend,
        "effective_cpm": effective_cpm,
        "cost_per_view": total_spend / target_views if target_views else 0
    }

def calculate_fleet(
    target_views_per_month: int,
    num_phones: int = 20,
    cost_per_phone: float = 90.0,
    monthly_proxy_per_phone: float = 18.0,
    monthly_sim_per_phone: float = 10.0,
    monthly_ai_tools: float = 120.0,
    months_amortized: int = 6
) -> dict:
    """Removed: phone farm / account fleet modeling is out of scope for this
    skill (platform ToS violation — see SKILL.md)."""
    raise SystemExit(
        "Phone farm / account fleet modeling is not supported. These "
        "operations violate platform terms of service. Use 'clipping', 'ugc', "
        "or 'slideshow' instead."
    )

def print_table(title: str, rows: list):
    print(f"\n=== {title} ===")
    max_k = max(len(k) for k, _ in rows)
    for k, v in rows:
        print(f"  {k.ljust(max_k)} : {v}")

def main():
    parser = argparse.ArgumentParser(description="Short-form viral campaign economic modeler.")
    subparsers = parser.add_subparsers(dest="command")

    # Compare
    p_comp = subparsers.add_parser("compare", help="Compare all three engines for target views")
    p_comp.add_argument("--views", type=int, default=1_000_000, help="Target views (default: 1,000,000)")
    p_comp.add_argument("--clipping-cpm", type=float, default=1.0, help="Clipping CPM (default: $1.00)")
    p_comp.add_argument("--ugc-base", type=float, default=25.0, help="UGC Base fee per video (default: $25)")
    p_comp.add_argument("--ugc-cpm", type=float, default=1.0, help="UGC Performance CPM (default: $1.00)")
    p_comp.add_argument("--slide-100k", type=float, default=100.0, help="Slideshow 100k bounty (default: $100)")
    p_comp.add_argument("--slide-1m", type=float, default=350.0, help="Slideshow 1M bounty (default: $350)")

    # Clipping
    p_clip = subparsers.add_parser("clipping", help="Model pure clipping campaign")
    p_clip.add_argument("--views", type=int, required=True, help="Target verified views")
    p_clip.add_argument("--cpm", type=float, default=1.0, help="Target CPM in USD (default: $1.00)")
    p_clip.add_argument("--bot-reserve", type=float, default=15.0, help="Fraud reserve %% (default: 15.0)")

    # UGC
    p_ugc = subparsers.add_parser("ugc", help="Model UGC creator campaign")
    p_ugc.add_argument("--views", type=int, required=True, help="Target views")
    p_ugc.add_argument("--base", type=float, default=25.0, help="Base pay per creative")
    p_ugc.add_argument("--cpm", type=float, default=1.0, help="Performance CPM")
    p_ugc.add_argument("--avg-views", type=int, default=15000, help="Avg views per creative")

    # Slideshow
    p_slide = subparsers.add_parser("slideshow", help="Model TikTok/IG slideshow milestone syndication")
    p_slide.add_argument("--views", type=int, required=True, help="Target verified views")
    p_slide.add_argument("--payout-100k", type=float, default=100.0, help="Payout milestone at 100k views (default: $100)")
    p_slide.add_argument("--payout-1m", type=float, default=350.0, help="Payout milestone at 1M views (default: $350)")
    p_slide.add_argument("--bonus", type=float, default=15.0, help="Loyalty bonus pool %% (default: 15.0)")
    p_slide.add_argument("--bot-reserve", type=float, default=10.0, help="Fraud reserve %% (default: 10.0)")
    p_slide.add_argument("--avg-hit", type=int, default=200000, help="Average views per qualifying hit (default: 200,000)")

    # Fleet
    p_fleet = subparsers.add_parser("fleet", help="Model phone farm / account fleet")
    p_fleet.add_argument("--views", type=int, default=1_000_000, help="Target monthly views")
    p_fleet.add_argument("--phones", type=int, default=25, help="Number of devices")
    p_fleet.add_argument("--cost-per-phone", type=float, default=90.0, help="Phone CapEx")

    args = parser.parse_args()

    if args.command == "clipping":
        res = calculate_clipping(args.views, args.cpm, args.bot_reserve)
        rows = [
            ("Target Views", f"{res['target_views']:,}"),
            ("Target CPM", f"${res['cpm']:.2f}"),
            ("Gross Performance Spend", f"${res['gross_spend']:,.2f}"),
            ("Bot / Fraud Reserve", f"${res['bot_reserve']:,.2f}"),
            ("Total Budget Requisite", f"${res['total_budget_needed']:,.2f}"),
            ("Est. Clippers Needed", f"~{res['estimated_clippers_needed']}"),
            ("Effective Cost Per View", f"${res['cost_per_view']:.4f}")
        ]
        print_table("Clipping Campaign Economic Model", rows)

    elif args.command == "ugc":
        res = calculate_ugc(args.views, args.base, args.cpm, args.avg_views)
        rows = [
            ("Target Views", f"{res['target_views']:,}"),
            ("Videos Needed", f"{res['num_videos_required']}"),
            ("Base Fee Spend", f"${res['total_base_spend']:,.2f}"),
            ("Performance CPM Spend", f"${res['performance_spend']:,.2f}"),
            ("Total Campaign Spend", f"${res['total_spend']:,.2f}"),
            ("Effective CPM", f"${res['effective_cpm']:.2f}"),
            ("Cost Per View", f"${res['cost_per_view']:.4f}")
        ]
        print_table("UGC / Creator Fleet Economic Model", rows)

    elif args.command == "slideshow":
        res = calculate_slideshow(
            args.views,
            args.payout_100k,
            args.payout_1m,
            args.bonus,
            args.bot_reserve,
            args.avg_hit
        )
        rows = [
            ("Target Views", f"{res['target_views']:,}"),
            ("Estimated Hit Posts Needed", f"~{res['num_hits_required']} (avg {res['avg_hit_views']:,} views/hit)"),
            ("Base Milestone Payouts", f"${res['base_milestone_payout']:,.2f}"),
            ("Creator Loyalty Bonus Pool", f"${res['loyalty_bonus_spend']:,.2f}"),
            ("Bot / Fraud Reserve", f"${res['bot_reserve']:,.2f}"),
            ("Total Budget Requisite", f"${res['total_budget_needed']:,.2f}"),
            ("Effective CPM", f"${res['effective_cpm']:.2f}"),
            ("Cost Per View", f"${res['cost_per_view']:.4f}")
        ]
        print_table("Slideshow Syndication Milestone Economic Model", rows)

    elif args.command == "fleet":
        # Refusal stub: phone farm / account fleet ops are out of scope.
        calculate_fleet(args.views, args.phones, args.cost_per_phone)

    elif args.command == "compare" or not args.command:
        views = getattr(args, "views", 1_000_000)
        c_cpm = getattr(args, "clipping_cpm", 1.0)
        u_base = getattr(args, "ugc_base", 25.0)
        u_cpm = getattr(args, "ugc_cpm", 1.0)
        s_100k = getattr(args, "slide_100k", 100.0)
        s_1m = getattr(args, "slide_1m", 350.0)

        clip = calculate_clipping(views, c_cpm)
        ugc = calculate_ugc(views, u_base, u_cpm)
        slide = calculate_slideshow(views, s_100k, s_1m)

        print(f"\n==========================================================================")
        print(f" SHORT-FORM DISTRIBUTION ENGINE BENCHMARK: {views:,} VIEWS")
        print(f"==========================================================================")
        print(f"{'Engine':<25} | {'Total Cost':<12} | {'Eff. CPM':<10} | {'Control':<8} | {'Trust / Conv.'}")
        print(f"{'-'*25}-|-{'-'*12}-|-{'-'*10}-|-{'-'*8}-|-{'-'*15}")
        print(f"{'Clipping (Pure CPM)':<25} | ${clip['total_budget_needed']:<11,.2f} | ${clip['cpm']:<9.2f} | {'Low':<8} | {'Low-Medium'}")
        print(f"{'UGC (Base + CPM)':<25} | ${ugc['total_spend']:<11,.2f} | ${ugc['effective_cpm']:<9.2f} | {'High':<8} | {'Highest'}")
        print(f"{'Slideshow (Milestones)':<25} | ${slide['total_budget_needed']:<11,.2f} | ${slide['effective_cpm']:<9.2f} | {'Medium':<8} | {'High (Utility)'}")
        print(f"\nKey Takeaways:")
        print(f"  1. UGC has highest upfront cost (${ugc['total_spend']:,.2f}), but highest conversion for trust-heavy products.")
        print(f"  2. Slideshows deliver lowest effective CPM (${slide['effective_cpm']:.2f}) and zero downside on flop posts ($0 under 100k).")
        print(f"  3. Clipping scales fast (${clip['total_budget_needed']:,.2f}), but requires bot fraud scrubbing.")
        print(f"  4. Phone farm / account fleet ops are out of scope: they violate platform terms of service.")

if __name__ == "__main__":
    main()
