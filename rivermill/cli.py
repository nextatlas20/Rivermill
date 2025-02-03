"""Command line entry points."""

import argparse
import sys

from rivermill.config import load_settings
from rivermill.delivery.worker import DeliveryWorker
from rivermill.storage.postgres import PostgresStore


def cmd_replay(args) -> int:
    store = PostgresStore(load_settings().database_url)
    for event_id in args.event_ids:
        store.schedule(event_id, None)
    print(f"scheduled {len(args.event_ids)} event(s) for replay")
    return 0


def cmd_serve(args) -> int:
    store = PostgresStore(load_settings().database_url)
    worker = DeliveryWorker(store, sender=lambda url, payload: None)
    print(f"worker started, delivered {worker.run_once()} event(s)")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="rivermill")
    sub = parser.add_subparsers(dest="command", required=True)

    replay = sub.add_parser("replay", help="replay stored events")
    replay.add_argument("event_ids", nargs="+")
    replay.set_defaults(func=cmd_replay)

    serve = sub.add_parser("serve", help="run a delivery worker")
    serve.set_defaults(func=cmd_serve)
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
