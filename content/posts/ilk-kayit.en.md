---
title: "First entry in the logbook"
slug: "first-entry"
date: 2026-11-17
description: "Why this site exists and what I will write about here."
tags: ["site"]
---

A ship's logbook gets the same things written in it every day: the date, the position, the wind, what was done. A single entry looks ordinary, but once the book fills up a voyage appears. That is how I think about this site.

Here I will mostly write about:

- What I learn while moving banking systems onto new architectures
- Payment systems, authorization flows and the design decisions behind them
- Turning AI into a real product: MCP servers, LLMs and law

Entries will include code. An entry in this logbook, for instance, would look like this in Java:

```java
record Entry(LocalDate date, String title, Set<String> topics) {

    Entry {
        Objects.requireNonNull(date, "Every entry has a date");
        topics = Set.copyOf(topics);
    }
}
```

You can leave a comment under each post. Questions and objections help me more than agreement does.
