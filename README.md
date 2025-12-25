# Digital-Addiction-and-Focus-Guardian

Overview

Digital Addiction & Focus Guardian is a system-level focus enforcement tool designed to prevent digital distractions by blocking websites and desktop applications using policy-based controls instead of easily bypassed browser extensions.

The system protects long-term user intent from short-term impulsive behavior through time-locked rules, OS-level enforcement, and tamper detection.

Key Features

System-level website blocking using the OS hosts file

Application blocking via real-time process monitoring

Unified web dashboard for managing website and app policies

Time-locked enforcement (no instant unblock)

Tamper detection & self-healing for hosts file modifications

Auto-start on system boot for persistent enforcement

Activity and violation logging

How It Works
1. Website Blocking

Websites are redirected to localhost using the system hosts file.

Blocking applies across all browsers.

Multiple domain variants (e.g., www, m) and IPv4/IPv6 are handled.

Entries are added only once (duplicate-safe).

2. Application Blocking

A background process monitors running applications.

If a blocked app is detected (e.g., WhatsApp, VLC, Edge), it is immediately terminated.

Each attempt is logged for accountability.

3. Policy Enforcement

Blocks are stored in a local SQLite database.

Users cannot instantly remove blocks.

Unlocking occurs automatically after the policy duration expires.

4. Tamper Detection

The system continuously monitors the hosts file.

If blocked entries are manually removed, they are automatically restored.

All tampering attempts are logged.

5. Auto-Start on Boot

Enforcement services are registered as privileged startup tasks.

Focus protection continues even after system restarts.

Technology Stack

Backend: Python

Web Framework: Flask

Database: SQLite

System Enforcement: OS hosts file + process monitoring

Platform: Windows

Intended Use Cases

Students preparing for exams

Competitive programmers

Remote workers

Digital detox programs

Educational institutions

Ethical Design

No permanent lock-out

System-level recovery remains possible via administrator access

Prevents impulsive misuse while allowing legitimate recovery

Conclusion

Digital Addiction & Focus Guardian demonstrates a practical, secure, and scalable approach to digital well-being by combining system-level enforcement, tamper resistance, and user-defined focus policies.
