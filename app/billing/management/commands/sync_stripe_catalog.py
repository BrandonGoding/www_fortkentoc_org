# billing/management/commands/sync_stripe_catalog.py
from __future__ import annotations

from django.core.management.base import BaseCommand

from billing.service import StripeService


class Command(BaseCommand):
    help = "Sync Products (and Prices) from Stripe into the local database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--all",
            action="store_true",
            help="Include inactive/archived products and prices (default is active-only).",
        )
        parser.add_argument(
            "--no-prices",
            action="store_true",
            help="Do not sync prices (only products).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Validate and show counts without writing.",
        )

    def handle(self, *args, **options):
        active_only = not options["all"]
        sync_prices = not options["no_prices"]
        dry_run = options["dry_run"]

        service = StripeService()
        self.stdout.write(self.style.MIGRATE_HEADING("Stripe → DB (catalog)"))

        summary = service.pull_catalog(
            active_only=active_only,
            sync_prices=sync_prices,
            dry_run=dry_run,
        )

        self.stdout.write(
            "Products: created {p_c}  updated {p_u}\nPrices:   created {r_c}  updated {r_u}\n"
            "Options:  active_only={a}  sync_prices={s}  dry_run={d}".format(
                p_c=summary["products_created"],
                p_u=summary["products_updated"],
                r_c=summary["prices_created"],
                r_u=summary["prices_updated"],
                a=summary["active_only"],
                s=sync_prices,
                d=summary["dry_run"],
            )
        )
        self.stdout.write(self.style.SUCCESS("Done"))
