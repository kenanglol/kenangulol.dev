---
title: "TickPilot"
description: "An algorithmic portfolio platform that runs on live US stock data, puts its decisions through a risk check and simulates all trades internally."
status: "sea"
years: "2026 –"
stack: ["Python", "SQLite", "Docker", "GitHub Actions", "Alpaca API"]
weight: 2
---

TickPilot is a platform I built to try trading strategies on the live market without putting real money at risk. It takes real-time data for US exchanges from Alpaca, puts strategy decisions through a risk check and simulates orders entirely on its own; no order ever reaches a broker. It has run on a server around the clock since September 2026. The plan is to mature it on the US market first, then move it to Borsa İstanbul.

## How it works

The system is three services, each the sole owner of its data. market-data is the only one that connects to Alpaca or reaches the outside network: it validates the data, reports when the feed goes stale or drops, and writes events for 30 stocks to an ordered journal. strategy-host reads that journal and runs an SMA cross, an RSI and an opening-range breakout strategy. Strategies can only say buy or sell; they cannot touch cash or positions. core owns the risk checks, the simulated orders and the ledger. Each strategy has its own $3,000 virtual budget, and its profit and loss is tracked separately.

Alongside these there is a replay tool that reruns a recorded session, sped up, without touching the live system, a dashboard with daily reports computed from nightly backups, and a monitor that sends a Telegram message when a problem persists.

## What I did

I designed the service boundaries and the single path a decision follows until it becomes an order, and recorded the key decisions in nine architecture decision records (ADRs). I built the live feed, the strategy plugin interface, a layered risk engine and the release setup. The services run with read-only file systems and expose no ports; every release is tagged with its commit SHA and rolls back on its own if it fails its health check.

What taught me the most were the places where live data changed the design. In the first six sessions, about half of all signals tried to sell shares the strategy did not hold. So I took the decision of how much to buy away from the strategy and gave it to the risk budget. When six sessions of data passed 18 GiB on the server, I designed a layout that splits data into hot and archive tiers.

The project has over 150 commits, 48 pull requests and 570 tests. I develop it with Claude Code; the source is private for now.
