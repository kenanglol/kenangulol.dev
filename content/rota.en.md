---
title: "Route"
slug: "route"
layout: "rota"
description: "Kenan Gülol's career and education: the ports of call from Ege University to DefineX."
aliases: ["/cv/"]
location: "Istanbul, Türkiye"
pdf: "/files/kenan-gulol-cv-en.pdf"
lead: >
  I build banking and payment systems in Java and Spring Boot. This page charts
  the ports I have called at so far, newest first. The course began in İzmir, at Ege University.
ports:
  - name: "Ege University"
    role: "B.Sc. Computer Engineering"
    when: "2017 – 2021"
    where: "İzmir"
    text: "GPA 3.48 / 4.00. Graduation thesis: [a hybrid deep learning model](/en/projects/stock-forecasting/) for forecasting stock market indices and stock prices, funded by TÜBİTAK 2209-A."
  - name: "Yapı Kredi Teknoloji"
    role: "Software Engineer"
    when: "Sep 2020 – Sep 2022"
    where: "Remote"
    items:
      - "Designed and built, with my team, a Host Card Emulation (HCE) system that lets customers pay contactless with their phones, as with Apple Pay or Google Pay."
  - name: "n11.com"
    role: "Software Engineer"
    when: "Sep 2022 – Sep 2023"
    where: "Remote"
    text: "One of Turkey's leading marketplaces, with 20M+ products and 23M registered users."
    items:
      - "Wrote an image-cropping algorithm that fixed product photo format problems in several categories, and ran it as a Python batch job."
  - name: "DefineX"
    role: "Senior Backend Engineer"
    when: "Sep 2023 – Present"
    where: "Remote, consultant at Garanti Teknoloji"
    current: true
    text: "Promoted from Software Engineer to Senior Backend Engineer in 2025."
    legs:
      - name: "Treasury systems"
        when: "Sep 2023 – Apr 2026"
        items:
          - "Moved outdated treasury systems onto Spring Boot microservices integrated with Murex, the trading and risk platform used by most banks in Turkey."
          - "Built flows that load Murex reports into the bank's data warehouse with Oracle Data Integrator (ODI)."
      - name: "Card authorization modernization"
        when: "May 2026 – Present"
        items:
          - "Migrating the bank's debit card authorization from Mainframe to a new Java/Spring Boot architecture in a 6-person team."
          - "Built e-commerce authorization end to end: card, transaction and account eligibility, security, fraud, and limit and cap checks."
          - "Delivered refund and reversal flows; ported 26 purchase and 8 refund checks from COBOL; proposed the adopted step-based flow design."
          - "Designed the project's first Camunda BPM flow, linking POS to credit and debit card authorization, and tested it end to end."
---

## Skills

- **Languages:** Java, Python
- **Frameworks and architecture:** Spring Boot, microservices, Camunda BPM
- **Data and integration:** Oracle, PostgreSQL, Elasticsearch, Oracle Data Integrator (ODI), Apache Kafka, XSLT
- **Platforms:** Docker, OpenShift
- **Domain:** card authorization, payment systems, treasury (Murex)
- **AI tooling:** Claude Code, MCP, LLM-based development

## Languages

Turkish (native), English (full professional proficiency)
