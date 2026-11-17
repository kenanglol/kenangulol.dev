---
title: "AI assistant for Turkish law"
slug: "turkish-law-ai"
description: "A start-up bringing lawyers' case, hearing and document tracking together with an AI built for Turkish law, in one desktop app."
status: "slip"
years: "2026 –"
role: "Co-founder and software architect"
stack: ["Tauri", "React", "TypeScript", "PostgreSQL", "pgvector", "Python", "MCP"]
weight: 1
---

A legal-tech start-up that lawyers and developers are building together, not yet released. Today lawyers track their cases in one place and research case law and legislation in others. We bring these into a single desktop app: each case becomes its own workspace with its documents, hearings and notes, and the AI answers within that case's context, backed by the relevant statutes and precedents. When it doesn't know something, it asks rather than guesses.

I am a co-founder and the software architect, responsible for architecture, data pipelines, the AI infrastructure and the release process. We built two pipelines for public legal data. The first narrows more than ten million court decisions down to the most influential through citation analysis, strips personal data and makes hundreds of thousands of passages searchable with hybrid search; a single fix to the query plan took search time from minutes to milliseconds. The second turns all of Turkish legislation into a versioned database at the level of articles, paragraphs and clauses. The lawyers' request to see "the statute first, then the decisions" shaped that data model directly.

The desktop app is built with Tauri and React and updates itself. Privacy has been part of the architecture from day one: client and case data will never be used to train models, and the AI that works with that data will run in Turkey.

I work closely with Claude on the project. The stronger model plans and checks, a cheaper model handles mechanical bulk work, and we recount the cheaper model's numbers with code every time.
