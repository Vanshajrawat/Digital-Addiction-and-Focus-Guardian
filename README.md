# Digital Addiction \& Focus Guardian

GitHub link: https://github.com/Vanshajrawat/Digital-Addiction-and-Focus-Guardian


### Overview

Digital Addiction \& Focus Guardian is a system-level focus enforcement tool designed to prevent digital distractions by blocking websites and desktop applications using policy-based controls instead of easily bypassed browser extensions.

The system protects long-term user intent from short-term impulsive behavior through time-locked rules, OS-level enforcement, and tamper detection.



### Key Features

1. System-level website blocking using the OS hosts file
2. Application blocking via real-time process monitoring
3. Unified web dashboard for managing website and app policies
4. Time-locked enforcement (no instant unblock)
5. Auto-start on system boot for persistent enforcement
6. Activity and violation logging



### How It Works

#### Website Blocking

1. Websites are redirected to localhost using the system hosts file.
2. Blocking applies across all browsers.
3. Multiple domain variants (e.g., www, m) and IPv4/IPv6 are handled.
4. Entries are added only once (duplicate-safe).



#### Application Blocking

1. A background process monitors running applications.
2. If a blocked app is detected, it is immediately terminated.
3. Each attempt is logged for accountability.



#### Policy Enforcement

1. Blocks are stored in a local SQLite database.
2. Users cannot instantly remove blocks.
3. Unlocking occurs automatically after the policy duration expires.



#### Auto-Start on Boot

1. Enforcement services are registered as privileged startup tasks.
2. Focus protection continues even after system restarts.



### Technology Stack

1. Backend: Python
2. Web Framework: Flask
3. Database: SQLite
4. System Enforcement: OS hosts file + process monitoring
5. Platform: Windows



### Intended Use Cases

1. Students preparing for exams
2. Competitive programmers
3. Remote workers
4. Digital detox programs
5. Educational institutions
6. Ethical Design
7. No permanent lock-out
8. System-level recovery remains possible via administrator access
9. Prevents impulsive misuse while allowing legitimate recovery



### Conclusion

Digital Addiction \& Focus Guardian demonstrates a practical, secure, and scalable approach to digital well-being by combining system-level enforcement, and user-defined focus policies.

