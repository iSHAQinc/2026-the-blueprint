# 2026: The Enterprise Engineering Blueprint

A rigorous, 12-month self-study curriculum designed to build Enterprise-Grade backend systems. Focus: Python, Go, AWS, and Distributed Systems.

**Objective:** Rival a Masters in Computer Science while building a Senior Portfolio.
**Theme:** "Theory in the Morning. Production Engineering in the Evening."
**Stack:** Python (Expert), Go (Systems), AWS (Cloud), Postgres (Data).

---

## 📚 The Required Library

1.  **Architecture:** _Designing Data-Intensive Applications (DDIA)_ — Martin Kleppmann
2.  **Code Quality:** _Clean Code_ — Robert C. Martin
3.  **Python:** _Fluent Python (2nd Ed)_ — Luciano Ramalho
4.  **Go:** _The Go Programming Language_ — Donovan & Kernighan
5.  **Database:** _PostgreSQL: Up and Running_ — Regina Obe
6.  **System Design:** _System Design Interview_ — Alex Xu
7.  **Monitoring:** _Observability Engineering_ — Charity Majors
8.  **Security:** _Web Application Security_ — Andrew Hoffman
9.  **Algorithms:** _Grokking Algorithms_ — Aditya Bhargava
10. **DevOps:** _The DevOps Handbook_ — Gene Kim

### 🔧 Tooling Manuals (Reference)

- **Testing:** _Python Testing with pytest_ (Brian Okken)
- **Git:** _Pro Git_ (Scott Chacon)
- **Django:** _Two Scoops of Django 3.x_ (Feldroy)

---

## 🏁 Q1: The Architect (Jan - Mar)

**Project:** "VenueOS" (High-Concurrency Event System)
**Goal:** Master Django Internals, ACID Transactions, and TDD.

### **JANUARY: Standards & Schema Design**

**Week 1 (Jan 1-4): Design & Setup**

- [x] **01 Thu JAN (AM):** **Read** _Clean Code_ (Ch 1: Clean Code) LeetCode problem.
- [x] **01 Thu JAN (PM):** **Task:** Write the **Technical Design Doc**. Define Schema (Venues, Spaces, Bookings). Save as `docs/design_v1.md`.
- [x] **02 Fri JAN (AM):** **Read** _Clean Code_ (Ch 2: Clean The Code!), LeetCode problem.
- [ ] **02 Fri JAN (PM):** **Task:** Setup Docker Dev Environment (Django + Postgres). Config `pre-commit` hooks (Black, Flake8).
- [ ] **03 Sat JAN (AM):** **Read** _Postgres Up & Running_ (Ch 1: Basics), LeetCode problem.
- [ ] **03 Sat JAN (PM):** **Task:** Initialize Django Models. Run Migrations. **Deep Work:** Write tests for User Model _before_ implementation.
- [ ] **04 Sun JAN (AM):** **Read:** Review `design_v1.md` against actual models, LeetCode problem..
- [ ] **04 Sun JAN (PM):** **Task:** Refactor initial setup. Ensure Docker runs smoothly.

**Week 2 (Jan 5-11): Test Driven Development (TDD)**

- [ ] **05 Mon JAN (AM):** **Algorithm Practice:** 2 Array problems (Medium). **Read** _Clean Code_ (Ch 3: Functions).
- [ ] **05 Mon JAN (PM):** **Task:** Implement Venue/Space Logic. **Constraint:** TDD Only (Red -> Green -> Refactor).
- [ ] **06 Tue JAN (AM):** **Algorithm Practice:** 2 String problems. **Read** _Clean Code_ (Ch 4: Comments).
- [ ] **06 Tue JAN (PM):** **Task:** Add "Opening Hours" logic to Venues.
- [ ] **07 Wed JAN (AM):** **Algorithm Practice:** 2 HashMap problems. **Read** _Fluent Python_ (Ch 1: Data Model).
- [ ] **07 Wed JAN (PM):** **Task:** Implement Booking Model. Test constraint: "End time cannot be before Start time".
- [ ] **08 Thu JAN (AM):** **Algorithm Practice:** 2 Two Pointer problems. **Read** _Fluent Python_ (Ch 2: Sequences).
- [ ] **08 Thu JAN (PM):** **Task:** Refactor "Fat Models". Move business logic to `services.py`.
- [ ] **09 Fri JAN (AM):** **Algorithm Practice:** 2 Sliding Window problems. **Read** _Postgres Up & Running_ (Constraints).
- [ ] **09 Fri JAN (PM):** **Task:** Add DB Constraints (`CheckConstraint`) to prevent invalid dates at the DB level.
- [ ] **10 Sat JAN (AM):** **Algorithm Practice:** Review week's problems.
- [ ] **10 Sat JAN (PM):** **Deep Work:** Implement "Recursive Spaces" (Building -> Floor -> Room). Use Recursive CTEs.
- [ ] **11 Sun JAN (AM):** **Read:** Review _Clean Code_ highlights from the week.
- [ ] **11 Sun JAN (PM):** **Refactor:** Ensure 100% Test Pass rate. Daily Habit: 15 min open source contribution.

**Week 3 (Jan 12-18): Advanced Data Integrity**

- [ ] **12 Mon JAN (AM):** **Algorithm Practice:** 2 Stack problems. **Read** _DDIA_ (Ch 7: Transactions).
- [ ] **12 Mon JAN (PM):** **Task:** Research `select_for_update` in Django.
- [ ] **13 Tue JAN (AM):** **Algorithm Practice:** 2 Binary Search problems. **Read** _DDIA_ (Ch 7: Isolation Levels).
- [ ] **13 Tue JAN (PM):** **Task:** The "Double Booking" Problem. Write a test that spawns 2 threads trying to book the same slot.
- [ ] **14 Wed JAN (AM):** **Algorithm Practice:** 2 LinkedList problems.
- [ ] **14 Wed JAN (PM):** **Task:** Fix the Double Booking using Pessimistic Locking.
- [ ] **15 Thu JAN (AM):** **Algorithm Practice:** 2 Tree problems.
- [ ] **15 Thu JAN (PM):** **Task:** Write a "Stress Test" script that hammers the booking endpoint.
- [ ] **16 Fri JAN (AM):** **Algorithm Practice:** 2 Graph problems.
- [ ] **16 Fri JAN (PM):** **Task:** Optimize the schema. Add Indexes on `booking_date`.
- [ ] **17 Sat JAN (AM):** **System Design:** Design URL shortener (30 min).
- [ ] **17 Sat JAN (PM):** **Deep Work:** Implement "Dynamic Pricing Engine" (e.g., Weekends cost +20%).
- [ ] **18 Sun JAN (AM):** **Read:** Review _DDIA_ Ch 7 Notes.
- [ ] **18 Sun JAN (PM):** **Review:** Check for spaghetti code in the Pricing Engine.

**Week 4 (Jan 19-25): The API Layer**

- [ ] **19 Mon JAN (AM):** **Read** _RESTful Web APIs_ (Concept: Resources). **Algorithm Practice:** Review Trees.
- [ ] **19 Mon JAN (PM):** **Task:** Install Django Rest Framework (DRF). Build "Venue" endpoints.
- [ ] **20 Tue JAN (AM):** **Read** _Fluent Python_ (Ch 7: Decorators).
- [ ] **20 Tue JAN (PM):** **Task:** Implement Custom Permissions (IsVenueManager).
- [ ] **21 Wed JAN (AM):** **Algorithm Practice:** 2 Heap problems.
- [ ] **21 Wed JAN (PM):** **Task:** Serialize the Recursive Space tree efficiently.
- [ ] **22 Thu JAN (AM):** **Read** _DDIA_ (Ch 1: Reliability). **Algorithm Practice:** Mixed review.
- [ ] **22 Thu JAN (PM):** **Task:** Integrate **Swagger/OpenAPI**. Docs must be auto-generated.
- [ ] **23 Fri JAN (AM):** **Read** _Web Application Security_ (Ch 1-2). **Algorithm Practice:** Security-focused problems.
- [ ] **23 Fri JAN (PM):** **Task:** Rate Limiting. Prevent API abuse using Django Throttling.
- [ ] **24 Sat JAN (AM):** **System Design:** Design distributed cache (30 min). Monthly Review: Update Portfolio.
- [ ] **24 Sat JAN (PM):** **Milestone:** VenueOS Alpha complete. Code Freeze.
- [ ] **25 Sun JAN (AM):** **Read:** Review _RESTful_ principles.
- [ ] **25 Sun JAN (PM):** **Review:** Write "FIXME" comments on messy parts.

### **FEBRUARY: CI/CD & Performance**

**Week 5 (Jan 26-Feb 1): Performance Tuning**

- [ ] **26 Mon JAN (AM):** **Read** _Postgres Up & Running_ (Query Planning). **Algorithm Practice:** 2 Dynamic Programming (Easy).
- [ ] **26 Mon JAN (PM):** **Task:** Install `django-debug-toolbar`. Identify N+1 Queries.
- [ ] **27 Tue JAN (AM):** **Read** _Fluent Python_ (Iterators). **Algorithm Practice:** 2 DP problems.
- [ ] **27 Tue JAN (PM):** **Task:** Fix N+1 queries using `select_related`.
- [ ] **28 Wed JAN (AM):** **Algorithm Practice:** 2 DP problems.
- [ ] **28 Wed JAN (PM):** **Task:** Seed Database with 100,000 bookings. Measure API latency.
- [ ] **29 Thu JAN (AM):** **Algorithm Practice:** 2 DP problems.
- [ ] **29 Thu JAN (PM):** **Task:** Add Caching (Redis) for the "Venue List" endpoint.
- [ ] **30 Fri JAN (AM):** **Read** _DDIA_ (Ch 2: Data Models). **Algorithm Practice:** 2 DP problems.
- [ ] **30 Fri JAN (PM):** **Task:** Verify Cache Invalidation.
- [ ] **31 Sat JAN (AM):** **System Design:** Design notification system (30 min).
- [ ] **31 Sat JAN (PM):** **Deep Work:** Write a Performance Report (Before vs After).
- [ ] **01 Sun FEB (AM):** **Read:** Review _Postgres_ Query Planning notes.
- [ ] **01 Sun FEB (PM):** **Refactor:** Clean up the caching logic.

**Week 6 (Feb 2-8): CI/CD Pipelines**

- [ ] **02 Mon FEB (AM):** **Read** _Modern Software Engineering_ (Ch 5: Continuous Delivery).
- [ ] **02 Mon FEB (PM):** **Task:** Create `.github/workflows/test.yml`.
- [ ] **03 Tue FEB (AM):** **Read** _Clean Code_ (Error Handling).
- [ ] **03 Tue FEB (PM):** **Task:** Config GitHub Actions to run PyTest and Flake8.
- [ ] **04 Wed FEB (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **04 Wed FEB (PM):** **Task:** Add "Build Docker Image" step to pipeline.
- [ ] **05 Thu FEB (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **05 Thu FEB (PM):** **Task:** Fail the build if Test Coverage is < 80%.
- [ ] **06 Fri FEB (AM):** **Read** _Modern Software Engineering_ (Ch 6).
- [ ] **06 Fri FEB (PM):** **Task:** Fix any broken tests. Make the pipeline Green.
- [ ] **07 Sat FEB (AM):** **System Design:** Design a CI/CD system.
- [ ] **07 Sat FEB (PM):** **Deep Work:** Implement "Staging Environment" logic.
- [ ] **08 Sun FEB (AM):** **Read:** Review _Modern Software Engineering_ notes.
- [ ] **08 Sun FEB (PM):** **Review:** Ensure `README.md` explains how to run tests.

**Week 7 (Feb 9-15): Deployment**

- [ ] **09 Mon FEB (AM):** **Read** _DDIA_ (Ch 4: Encoding).
- [ ] **09 Mon FEB (PM):** **Task:** Create AWS/Render Account. Setup Postgres RDS.
- [ ] **10 Tue FEB (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **10 Tue FEB (PM):** **Task:** Deploy the Docker container to the cloud.
- [ ] **11 Wed FEB (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **11 Wed FEB (PM):** **Task:** Connect the App to the RDS Database.
- [ ] **12 Thu FEB (AM):** **Read** _DDIA_ (Ch 5: Replication).
- [ ] **12 Thu FEB (PM):** **Task:** Configure Environment Variables (Secrets).
- [ ] **13 Fri FEB (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **13 Fri FEB (PM):** **Task:** Verify "Production" works. Book a venue on the live site.
- [ ] **14 Sat FEB (AM):** **System Design:** Design Instagram (30 min).
- [ ] **14 Sat FEB (PM):** **CV Update:** Add "VenueOS" to CV. Keywords: "ACID Transactions", "CI/CD".
- [ ] **15 Sun FEB (AM):** **Read:** Review _DDIA_ Ch 5 notes.
- [ ] **15 Sun FEB (PM):** **REST DAY.** (Mandatory).

### **MARCH: Logic & Polish**

**Week 8 (Feb 16-22): Role Based Access**

- [ ] **16 Mon FEB (AM):** **Read** _Clean Code_ (Classes).
- [ ] **16 Mon FEB (PM):** **Task:** Define Roles (Admin, Manager, User).
- [ ] **17 Tue FEB (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **17 Tue FEB (PM):** **Task:** Write Custom Permission Classes in DRF.
- [ ] **18 Wed FEB (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **18 Wed FEB (PM):** **Task:** Unit Test permissions (Ensure User cannot delete Venue).
- [ ] **19 Thu FEB (AM):** **Read** _DDIA_ (Partitioning).
- [ ] **19 Thu FEB (PM):** **Task:** Implement PDF Invoicing (Generating files in Python).
- [ ] **20 Fri FEB (AM):** **Algorithm Practice:** LeetCode (Hard).
- [ ] **20 Fri FEB (PM):** **Task:** Refactor PDF generation to use a background task.
- [ ] **21 Sat FEB (AM):** **System Design:** Design Netflix (30 min).
- [ ] **21 Sat FEB (PM):** **Deep Work:** Audit the entire API for security holes.
- [ ] **22 Sun FEB (AM):** **Read:** Review _Clean Code_ (Classes).
- [ ] **22 Sun FEB (PM):** **Review:** Check database migrations.

**Week 9 (Feb 23-Mar 1): Invoicing & Reporting**

- [ ] **23 Mon FEB (AM):** **Read** _Postgres Up & Running_ (Aggregation).
- [ ] **23 Mon FEB (PM):** **Task:** Write SQL Group By queries for Revenue Reports.
- [ ] **24 Tue FEB (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **24 Tue FEB (PM):** **Task:** Setup basic logging (JSON format).
- [ ] **25 Wed FEB (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **25 Wed FEB (PM):** **Task:** Security Audit (Run bandit and safety checks).
- [ ] **26 Thu FEB (AM):** **Read** _Modern Software Engineering_ (Security).
- [ ] **26 Thu FEB (PM):** **Task:** Sanitize all inputs.
- [ ] **27 Fri FEB (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **27 Fri FEB (PM):** **Task:** Refactor the entire services.py file.
- [ ] **28 Sat FEB (AM):** **System Design:** Design Youtube (30 min).
- [ ] **28 Sat FEB (PM):** **Deep Work:** Connect PDF generation to Celery (Background Task).
- [ ] **01 Sun MAR (AM):** **Read:** Review _Postgres_ Aggregation.
- [ ] **01 Sun MAR (PM):** **Catch Up.**

**Week 10 (Mar 2-8): Hardening**

- [ ] **02 Mon MAR (AM):** **Read** _Modern Software Engineering_ (Security).
- [ ] **02 Mon MAR (PM):** **Task:** Run `bandit` (Security Linter) on code.
- [ ] **03 Tue MAR (AM):** **Algorithm Practice:** LeetCode (Greedy).
- [ ] **03 Tue MAR (PM):** **Task:** Sanitize all inputs.
- [ ] **04 Wed MAR (AM):** **Algorithm Practice:** LeetCode (Greedy).
- [ ] **04 Wed MAR (PM):** **Task:** Add Rate Limiting to sensitive endpoints.
- [ ] **05 Thu MAR (AM):** **Algorithm Practice:** LeetCode (Greedy).
- [ ] **05 Thu MAR (PM):** **Task:** Verify all dependencies are pinned in `requirements.txt`.
- [ ] **06 Fri MAR (AM):** **Algorithm Practice:** LeetCode (Greedy).
- [ ] **06 Fri MAR (PM):** **Task:** Write integration tests for the full booking flow.
- [ ] **07 Sat MAR (AM):** **System Design:** Design Rate Limiter.
- [ ] **07 Sat MAR (PM):** **Deep Work:** Refactor the entire `services.py` file.
- [ ] **08 Sun MAR (AM):** **Read:** Review Week's Security Notes.
- [ ] **08 Sun MAR (PM):** **Rest.**

**Week 11 (Mar 9-15): Documentation**

- [ ] **09 Mon MAR (AM):** **Read** _Clean Code_ (Formatting).
- [ ] **09 Mon MAR (PM):** **Task:** Finalize Swagger/OpenAPI docs.
- [ ] **10 Tue MAR (AM):** **Algorithm Practice:** Review Arrays & Strings.
- [ ] **10 Tue MAR (PM):** **Task:** Write `ARCHITECTURE.md` explaining your design.
- [ ] **11 Wed MAR (AM):** **Algorithm Practice:** Review HashMap & Trees.
- [ ] **11 Wed MAR (PM):** **Task:** Write `CONTRIBUTING.md`.
- [ ] **12 Thu MAR (AM):** **Algorithm Practice:** Review Graphs & DP.
- [ ] **12 Thu MAR (PM):** **Task:** Create a detailed README with screenshots.
- [ ] **13 Fri MAR (AM):** **Algorithm Practice:** Mock Interview Session (Timed).
- [ ] **13 Fri MAR (PM):** **Task:** Record a Loom video demo of VenueOS.
- [ ] **14 Sat MAR (AM):** **System Design:** Design Chat System (WhatsApp).
- [ ] **14 Sat MAR (PM):** **Deep Work:** Write the Case Study for your Portfolio.
- [ ] **15 Sun MAR (AM):** **Read:** Review Documentation Principles.
- [ ] **15 Sun MAR (PM):** **Review:** Polish GitHub Repo.

**Week 12 (Mar 16-22): Final Release**

- [ ] **16 Mon MAR (AM):** **Read** _Observability Engineering_ (Ch 1).
- [ ] **16 Mon MAR (PM):** **Task:** Bug Bash (Fix Issue #1, #2).
- [ ] **17 Tue MAR (AM):** **Algorithm Practice:** Mock Interview Session (Timed).
- [ ] **17 Tue MAR (PM):** **Task:** Bug Bash (Fix Issue #3, #4).
- [ ] **18 Wed MAR (AM):** **Algorithm Practice:** Mock Interview Session (Timed).
- [ ] **18 Wed MAR (PM):** **Task:** Final Polish of README.
- [ ] **19 Thu MAR (AM):** **Algorithm Practice:** Mock Interview Session (Timed).
- [ ] **19 Thu MAR (PM):** **Task:** Verify Deployment.
- [ ] **20 Fri MAR (AM):** **Read** _Observability Engineering_ (Ch 2).
- [ ] **20 Fri MAR (PM):** **Task:** Final Git Commit & Tag.
- [ ] **21 Sat MAR (AM):** **System Design:** Design Twitter Search.
- [ ] **21 Sat MAR (PM):** **Release:** VenueOS v1.0. Tag on GitHub. Share on LinkedIn.
- [ ] **22 Sun MAR (AM):** **Read:** Q1 Retrospective.
- [ ] **22 Sun MAR (PM):** **Q1 Review:** Do you understand Locks? Docker?

**Week 13 (Mar 23-29): The Q1 Buffer & Prep**

- [ ] **23 Mon MAR (AM):** **Read** _Fluent Python_ (Concurrency Preview).
- [ ] **23 Mon MAR (PM):** **Task:** Clean up laptop environment. Archive Q1 notes.
- [ ] **24 Tue MAR (AM):** **Read** _AsyncIO Documentation_.
- [ ] **24 Tue MAR (PM):** **Task:** Research FastAPI vs Django differences.
- [ ] **25 Wed MAR (AM):** **Read** _Redis Documentation_ (Pub/Sub).
- [ ] **25 Wed MAR (PM):** **Task:** Small experiment: Build a 5-line Async script.
- [ ] **26 Thu MAR (AM):** **Algorithm Practice:** LeetCode (Easy) to reset brain.
- [ ] **26 Thu MAR (PM):** **Task:** Pre-read "Constellation Command" requirements.
- [ ] **27 Fri MAR (AM):** **Read** _High Performance Python_ (Intro).
- [ ] **27 Fri MAR (PM):** **Task:** Setup Q2 Repo structure.
- [ ] **28 Sat MAR (AM):** **System Design:** Review Q1 Concepts.
- [ ] **28 Sat MAR (PM):** **Rest/Deep Play:** Do something non-coding.
- [ ] **29 Sun MAR (AM):** **Read:** Plan Q2 Schedule.
- [ ] **29 Sun MAR (PM):** **Review:** Ready for Q2.

---

## 🚀 Q2: The Async Commander (Apr - Jun)

**Project:** "Constellation Command" (Satellite Orbit Manager)
**Goal:** Master AsyncIO, Math, and Real-Time Systems.

### **APRIL: Physics & Async**

**Week 14 (Mar 30-Apr 5): Async Theory**

- [ ] **30 Mon MAR (AM):** **Read** _Fluent Python_ (Ch 19: Concurrency).
- [ ] **30 Mon MAR (PM):** **Task:** Setup FastAPI. Write a "Hello World" using `async def`.
- [ ] **31 Tue MAR (AM):** **Deep Dive:** The Python Event Loop (asyncio).
- [ ] **31 Tue MAR (PM):** **Task:** Build a script that makes 100 HTTP requests synchronously. Time it.
- [ ] **01 Wed APR (AM):** **Algorithm Practice:** LeetCode (Linked List).
- [ ] **01 Wed APR (PM):** **Task:** Rewrite the script using `aiohttp`. Time it. Compare.
- [ ] **02 Thu APR (AM):** **Algorithm Practice:** LeetCode (Tree).
- [ ] **02 Thu APR (PM):** **Task:** Create the `Satellite` Pydantic Model.
- [ ] **03 Fri APR (AM):** **Algorithm Practice:** LeetCode (Graph).
- [ ] **03 Fri APR (PM):** **Task:** Implement CRUD endpoints for Satellites.
- [ ] **04 Sat APR (AM):** **System Design:** Design Typeahead Suggestion.
- [ ] **04 Sat APR (PM):** **Deep Work:** Implement the "Satellite" Class with Vector math (Velocity, Position).
- [ ] **05 Sun APR (AM):** **Read:** Review AsyncIO Concepts.
- [ ] **05 Sun APR (PM):** **Review:** Write tests for the Vector math.

**Week 15 (Apr 6-12): The Physics Engine**

- [ ] **06 Mon APR (AM):** **Math Review:** Vectors & Velocity.
- [ ] **06 Mon APR (PM):** **Task:** Implement `update_position(velocity, time_delta)`.
- [ ] **07 Tue APR (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **07 Tue APR (PM):** **Task:** Create 500 Satellite objects in memory. Update them in a loop.
- [ ] **08 Wed APR (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **08 Wed APR (PM):** **Task:** Ensure the loop runs at 60Hz.
- [ ] **09 Thu APR (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **09 Thu APR (PM):** **Task:** Optimize the loop. Remove blocking calls.
- [ ] **10 Fri APR (AM):** **Read** _DDIA_ (Ch 3: Storage Engines).
- [ ] **10 Fri APR (PM):** **Task:** Output a JSON stream of coordinates.
- [ ] **11 Sat APR (AM):** **System Design:** Design Location Based Service (Yelp).
- [ ] **11 Sat APR (PM):** **Deep Work:** Visualize the output (Simple HTML/Canvas).
- [ ] **12 Sun APR (AM):** **Read:** Review DDIA Storage notes.
- [ ] **12 Sun APR (PM):** **Catch Up.**

**Week 16 (Apr 13-19): Redis Geo**

- [ ] **13 Mon APR (AM):** **Read** _DDIA_ (Ch 6: Partitioning).
- [ ] **13 Mon APR (PM):** **Task:** Spin up Redis. Install `redis-py`.
- [ ] **14 Tue APR (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **14 Tue APR (PM):** **Task:** Persist Satellite positions to Redis using `GEOADD`.
- [ ] **15 Wed APR (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **15 Wed APR (PM):** **Task:** Query "Satellites near London" using `GEORADIUS`.
- [ ] **16 Thu APR (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **16 Thu APR (PM):** **Task:** Implement "Collision Detection".
- [ ] **17 Fri APR (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **17 Fri APR (PM):** **Task:** Optimize Redis calls using Pipelining.
- [ ] **18 Sat APR (AM):** **System Design:** Design Uber Backend.
- [ ] **18 Sat APR (PM):** **Deep Work:** Integrate Redis logic into the main Async Loop.
- [ ] **19 Sun APR (AM):** **Read:** Review Redis Geo docs.
- [ ] **19 Sun APR (PM):** **Review:** Check for memory leaks.

**Week 17 (Apr 20-26): Optimization Week**

- [ ] **20 Mon APR (AM):** **Read** _High Performance Python_ (Profiling).
- [ ] **20 Mon APR (PM):** **Task:** Profile the application.
- [ ] **21 Tue APR (AM):** **Algorithm Practice:** LeetCode (Hard).
- [ ] **21 Tue APR (PM):** **Task:** Optimize JSON serialization (use `orjson`).
- [ ] **22 Wed APR (AM):** **Algorithm Practice:** LeetCode (Hard).
- [ ] **22 Wed APR (PM):** **Task:** Audit Event Loop blocking.
- [ ] **23 Thu APR (AM):** **Algorithm Practice:** LeetCode (Hard).
- [ ] **23 Thu APR (PM):** **Task:** Add Logging to Async Loop.
- [ ] **24 Fri APR (AM):** **Algorithm Practice:** LeetCode (Hard).
- [ ] **24 Fri APR (PM):** **Task:** Write tests for Collision Logic.
- [ ] **25 Sat APR (AM):** **System Design:** Design Youtube/Netflix.
- [ ] **25 Sat APR (PM):** **Deep Work:** Refactor for Clean Architecture.
- [ ] **26 Sun APR (AM):** **Read:** Review Profiling Results.
- [ ] **26 Sun APR (PM):** **Rest.**

### **MAY: Real-Time Websockets**

**Week 18 (Apr 27-May 3): Websockets**

- [ ] **27 Mon APR (AM):** **Read** _High Performance Browser Networking_ (Websockets).
- [ ] **27 Mon APR (PM):** **Task:** Create a FastAPI Websocket endpoint.
- [ ] **28 Tue APR (AM):** **Deep Dive:** WebSocket Handshake.
- [ ] **28 Tue APR (PM):** **Task:** Connect a simple HTML client. Stream coordinates live.
- [ ] **29 Wed APR (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **29 Wed APR (PM):** **Task:** Handle client disconnects gracefully.
- [ ] **30 Thu APR (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **30 Thu APR (PM):** **Task:** Broadcast logic (Fan-out to all clients).
- [ ] **01 Fri MAY (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **01 Fri MAY (PM):** **Task:** Authenticate WebSocket connections (JWT).
- [ ] **02 Sat MAY (AM):** **System Design:** Design Facebook Messenger.
- [ ] **02 Sat MAY (PM):** **Stress Test:** Open 1,000 tabs. Does the server crash? Fix it.
- [ ] **03 Sun MAY (AM):** **Read:** Review WebSocket RFC notes.
- [ ] **03 Sun MAY (PM):** **Review:** Document the Websocket Protocol.

**Week 19 (May 4-10): Background Workers**

- [ ] **04 Mon MAY (AM):** **Read** _DDIA_ (Ch 11: Stream Processing).
- [ ] **04 Mon MAY (PM):** **Task:** Setup **Celery** with Redis Broker.
- [ ] **05 Tue MAY (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **05 Tue MAY (PM):** **Task:** Offload "Fuel Calculation" to a background worker.
- [ ] **06 Wed MAY (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **06 Wed MAY (PM):** **Task:** Schedule a periodic task (beat).
- [ ] **07 Thu MAY (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **07 Thu MAY (PM):** **Task:** Ensure Celery workers auto-restart.
- [ ] **08 Fri MAY (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **08 Fri MAY (PM):** **Task:** Handle failed tasks (Retries).
- [ ] **09 Sat MAY (AM):** **System Design:** Design Web Crawler.
- [ ] **09 Sat MAY (PM):** **Monitor:** Use Flower to monitor Celery tasks.
- [ ] **10 Sun MAY (AM):** **Read:** Review Stream Processing notes.
- [ ] **10 Sun MAY (PM):** **Rest.**

**Week 20 (May 11-17): Telemetry & Docker**

- [ ] **11 Mon MAY (AM):** **Read** _Observability Engineering_ (Ch 3).
- [ ] **11 Mon MAY (PM):** **Task:** Add Telemetry (How many sats tracked?).
- [ ] **12 Tue MAY (AM):** **Read** _DevOps Handbook_ (Ch 1).
- [ ] **12 Tue MAY (PM):** **Task:** Dockerize FastAPI.
- [ ] **13 Wed MAY (AM):** **Read** _DevOps Handbook_ (Ch 2).
- [ ] **13 Wed MAY (PM):** **Task:** Dockerize Celery Worker.
- [ ] **14 Thu MAY (AM):** **Read** _DevOps Handbook_ (Ch 3).
- [ ] **14 Thu MAY (PM):** **Task:** Dockerize Redis.
- [ ] **15 Fri MAY (AM):** **Read** _DevOps Handbook_ (Ch 4).
- [ ] **15 Fri MAY (PM):** **Task:** Run full stack with `docker-compose`.
- [ ] **16 Sat MAY (AM):** **System Design:** Design Google Drive.
- [ ] **16 Sat MAY (PM):** **Deep Work:** Ensure Docker networking is secure.
- [ ] **17 Sun MAY (AM):** **Read:** Review Docker Networking.
- [ ] **17 Sun MAY (PM):** **Catch Up.**

**Week 21 (May 18-24): Polish**

- [ ] **18 Mon MAY (AM):** **Read** _Clean Code_ (Unit Tests).
- [ ] **18 Mon MAY (PM):** **Task:** Write Integration Tests (End-to-End).
- [ ] **19 Tue MAY (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **19 Tue MAY (PM):** **Task:** Refactor Configuration (Pydantic Settings).
- [ ] **20 Wed MAY (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **20 Wed MAY (PM):** **Task:** Add README with Architecture Diagram.
- [ ] **21 Thu MAY (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **21 Thu MAY (PM):** **Task:** Record Demo Video.
- [ ] **22 Fri MAY (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **22 Fri MAY (PM):** **Task:** Audit Codebase.
- [ ] **23 Sat MAY (AM):** **System Design:** Design API Rate Limiter.
- [ ] **23 Sat MAY (PM):** **Deep Work:** Final Polish.
- [ ] **24 Sun MAY (AM):** **Read:** Review Q2 Concepts.
- [ ] **24 Sun MAY (PM):** **Rest.**

### **JUNE: The Job Hunt (Soft Launch)**

**Week 22 (May 25-31): Prep Week**

- [ ] **25 Mon MAY (AM):** **Algorithm Practice:** Mock Interview (Timed).
- [ ] **25 Mon MAY (PM):** **Task:** CV Update: Add "Constellation Command".
- [ ] **26 Tue MAY (AM):** **Algorithm Practice:** Mock Interview (Timed).
- [ ] **26 Tue MAY (PM):** **Task:** Research 5 Target Companies.
- [ ] **27 Wed MAY (AM):** **Algorithm Practice:** Mock Interview (Timed).
- [ ] **27 Wed MAY (PM):** **Task:** Polish LinkedIn Profile.
- [ ] **28 Thu MAY (AM):** **Algorithm Practice:** Mock Interview (Timed).
- [ ] **28 Thu MAY (PM):** **Task:** Refactor Constellation Command (Code Review).
- [ ] **29 Fri MAY (AM):** **Algorithm Practice:** Mock Interview (Timed).
- [ ] **29 Fri MAY (PM):** **Task:** Draft Cover Letter templates.
- [ ] **30 Sat MAY (AM):** **System Design:** Design Twitter Timeline.
- [ ] **30 Sat MAY (PM):** **Deep Work:** Write Case Study for Constellation Command.
- [ ] **31 Sun MAY (AM):** **Read:** Review Application Strategy.
- [ ] **31 Sun MAY (PM):** **Rest.**

**Week 23 (Jun 1-7): Application Sprints**

- [ ] **01 Mon JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium (Timed 20 mins).
- [ ] **01 Mon JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **02 Tue JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium (Timed 20 mins).
- [ ] **02 Tue JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **03 Wed JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium (Timed 20 mins).
- [ ] **03 Wed JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **04 Thu JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium (Timed 20 mins).
- [ ] **04 Thu JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **05 Fri JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium (Timed 20 mins).
- [ ] **05 Fri JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **06 Sat JUN (AM):** **System Design:** Review Distributed Cache.
- [ ] **06 Sat JUN (PM):** **Deep Work:** Refactor older projects (VenueOS).
- [ ] **07 Sun JUN (AM):** **Read:** Review Week's applications.
- [ ] **07 Sun JUN (PM):** **Rest.**

**Week 24 (Jun 8-14): The Grind**

- [ ] **08 Mon JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **08 Mon JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **09 Tue JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **09 Tue JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **10 Wed JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **10 Wed JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **11 Thu JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **11 Thu JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **12 Fri JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **12 Fri JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **13 Sat JUN (AM):** **System Design:** Review Load Balancing.
- [ ] **13 Sat JUN (PM):** **Deep Work:** Learn a new tool (e.g., Prometheus).
- [ ] **14 Sun JUN (AM):** **Read:** Review feedback from any interviews.
- [ ] **14 Sun JUN (PM):** **Catch Up.**

**Week 25 (Jun 15-21): The Grind Continued**

- [ ] **15 Mon JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **15 Mon JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **16 Tue JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **16 Tue JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **17 Wed JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **17 Wed JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **18 Thu JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **18 Thu JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **19 Fri JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **19 Fri JUN (PM):** **Task:** Apply to 1 Role.
- [ ] **20 Sat JUN (AM):** **System Design:** Review Database Sharding.
- [ ] **20 Sat JUN (PM):** **Deep Work:** Final Polish of Constellation Command.
- [ ] **21 Sun JUN (AM):** **Read:** Prepare for Q3 (Go).
- [ ] **21 Sun JUN (PM):** **Rest.**

**Week 26 (Jun 22-28): Capstone Release Week**

- [ ] **22 Mon JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **22 Mon JUN (PM):** **Task:** Write Release Notes.
- [ ] **23 Tue JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **23 Tue JUN (PM):** **Task:** Update Repo with Screenshots.
- [ ] **24 Wed JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **24 Wed JUN (PM):** **Task:** Verify Docker deployment.
- [ ] **25 Thu JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **25 Thu JUN (PM):** **Task:** Add Badge to GitHub Profile.
- [ ] **26 Fri JUN (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **26 Fri JUN (PM):** **Task:** Share project on LinkedIn/Reddit.
- [ ] **27 Sat JUN (All Day):** **Capstone Release:** Constellation Command v1.0.
- [ ] **28 Sun JUN (AM):** **Read:** Introduction to Go.
- [ ] **28 Sun JUN (PM):** **Rest.**

---

## 📡 Q3: The Systems Engineer (Jul - Sep)

**Project:** "Virtual Patchbay" (Audio/Video Routing)
**Goal:** Master Go, UDP, and Low-Level Networking.

### **JULY: Go Bootcamp**

**Week 27 (Jun 29-Jul 5): Go Basics**

- [ ] **29 Mon JUN (AM):** **Read** _The Go Programming Language_ (Ch 1: Tutorial).
- [ ] **29 Mon JUN (PM):** **Task:** Write "Hello World". Setup Go Modules.
- [ ] **30 Tue JUN (AM):** **Read** _Go Lang_ (Ch 2: Program Structure).
- [ ] **30 Tue JUN (PM):** **Task:** Rewrite the "Vector Math" logic from Q2 in Go.
- [ ] **01 Wed JUL (AM):** **Read** _Go Lang_ (Ch 3: Basic Types).
- [ ] **01 Wed JUL (PM):** **Task:** Benchmark Go implementation vs Python implementation.
- [ ] **02 Thu JUL (AM):** **Algorithm Practice:** LeetCode (Easy) in Go.
- [ ] **02 Thu JUL (PM):** **Task:** Learn Go Structs.
- [ ] **03 Fri JUL (AM):** **Algorithm Practice:** LeetCode (Easy) in Go.
- [ ] **03 Fri JUL (PM):** **Task:** Learn Go Methods.
- [ ] **04 Sat JUL (AM):** **System Design:** Design Key-Value Store.
- [ ] **04 Sat JUL (PM):** **Deep Work:** Implement "Satellite Structs" and Methods in Go.
- [ ] **05 Sun JUL (AM):** **Read:** Review Go syntax quirks.
- [ ] **05 Sun JUL (PM):** **Review:** Understand Go formatting (`gofmt`).

**Week 28 (Jul 6-12): Memory & Pointers**

- [ ] **06 Mon JUL (AM):** **Read** _Go Lang_ (Ch 4: Composite Types).
- [ ] **06 Mon JUL (PM):** **Task:** Experiment with Pointers vs Values.
- [ ] **07 Tue JUL (AM):** **Algorithm Practice:** LeetCode (Easy) in Go.
- [ ] **07 Tue JUL (PM):** **Task:** Build a "Packet Generator" struct.
- [ ] **08 Wed JUL (AM):** **Algorithm Practice:** LeetCode (Easy) in Go.
- [ ] **08 Wed JUL (PM):** **Task:** Pass structs by pointer.
- [ ] **09 Thu JUL (AM):** **Algorithm Practice:** LeetCode (Easy) in Go.
- [ ] **09 Thu JUL (PM):** **Task:** Pass structs by value. Compare.
- [ ] **10 Fri JUL (AM):** **Algorithm Practice:** LeetCode (Easy) in Go.
- [ ] **10 Fri JUL (PM):** **Task:** Understand Slices vs Arrays.
- [ ] **11 Sat JUL (AM):** **System Design:** Design Unique ID Generator.
- [ ] **11 Sat JUL (PM):** **Deep Work:** Understand Go Garbage Collection. Write a stress test that creates garbage.
- [ ] **12 Sun JUL (AM):** **Read:** Review Pointer arithmetic (or lack thereof).
- [ ] **12 Sun JUL (PM):** **Review:** Refactor code to be idiomatic Go.

**Week 29 (Jul 13-19): The Bridge (HTTP & JSON)**

- [ ] **13 Mon JUL (AM):** **Read** _Go Lang_ (Ch 4: JSON).
- [ ] **13 Mon JUL (PM):** **Task:** Build a simple HTTP Server in Go (using `net/http`).
- [ ] **14 Tue JUL (AM):** **Algorithm Practice:** LeetCode (Medium) in Go.
- [ ] **14 Tue JUL (PM):** **Task:** Write a handler that accepts JSON and unmarshals it to a Struct.
- [ ] **15 Wed JUL (AM):** **Algorithm Practice:** LeetCode (Medium) in Go.
- [ ] **15 Wed JUL (PM):** **Task:** Write a handler that returns JSON.
- [ ] **16 Thu JUL (AM):** **Algorithm Practice:** LeetCode (Medium) in Go.
- [ ] **16 Thu JUL (PM):** **Task:** Use `gorilla/mux` or `chi` for routing.
- [ ] **17 Fri JUL (AM):** **Algorithm Practice:** LeetCode (Medium) in Go.
- [ ] **17 Fri JUL (PM):** **Task:** Test the API with Postman.
- [ ] **18 Sat JUL (AM):** **System Design:** Design URL Shortener (Revisit).
- [ ] **18 Sat JUL (PM):** **Deep Work:** Connect Go Server to Python Client.
- [ ] **19 Sun JUL (AM):** **Read:** Review Go standard library docs (net/http).
- [ ] **19 Sun JUL (PM):** **Review:** Compare Python Flask/FastAPI vs Go `net/http`.

**Week 30 (Jul 20-26): Concurrency (Goroutines)**

- [ ] **20 Mon JUL (AM):** **Read** _Go Lang_ (Ch 8: Goroutines).
- [ ] **20 Mon JUL (PM):** **Task:** Launch 1,000 Goroutines to generate packets.
- [ ] **21 Tue JUL (AM):** **Read** _Go Lang_ (Ch 9: Shared Variables).
- [ ] **21 Tue JUL (PM):** **Task:** Use Channels to collect the packets safely.
- [ ] **22 Wed JUL (AM):** **Algorithm Practice:** LeetCode (Concurrency).
- [ ] **22 Wed JUL (PM):** **Task:** Implement Buffered Channels.
- [ ] **23 Thu JUL (AM):** **Algorithm Practice:** LeetCode (Concurrency).
- [ ] **23 Thu JUL (PM):** **Task:** Implement Select Statement.
- [ ] **24 Fri JUL (AM):** **Algorithm Practice:** LeetCode (Concurrency).
- [ ] **24 Fri JUL (PM):** **Task:** Handle timeouts.
- [ ] **25 Sat JUL (AM):** **System Design:** Design Chat System (Revisit).
- [ ] **25 Sat JUL (PM):** **Deep Work:** Implement "Worker Pool" pattern.
- [ ] **26 Sun JUL (AM):** **Read:** Review Go Concurrency Patterns.
- [ ] **26 Sun JUL (PM):** **Review:** Check for Race Conditions using `go run -race`.

### **AUGUST: Networking (UDP)**

**Week 31 (Jul 27-Aug 2): UDP Listener**

- [ ] **27 Mon JUL (AM):** **Read** _Computer Networking_ (Transport Layer).
- [ ] **27 Mon JUL (PM):** **Task:** Build a UDP Server in Go.
- [ ] **28 Tue JUL (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **28 Tue JUL (PM):** **Task:** Send dummy audio data from Python to Go via UDP.
- [ ] **29 Wed JUL (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **29 Wed JUL (PM):** **Task:** Handle UDP buffer size.
- [ ] **30 Thu JUL (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **30 Thu JUL (PM):** **Task:** Count packets received.
- [ ] **31 Fri JUL (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **31 Fri JUL (PM):** **Task:** Measure Packet loss.
- [ ] **01 Sat AUG (AM):** **System Design:** Design Streaming Service.
- [ ] **01 Sat AUG (PM):** **Task:** Implement a Ring Buffer to handle the stream.
- [ ] **02 Sun AUG (AM):** **Read:** Review UDP RFC.
- [ ] **02 Sun AUG (PM):** **Task:** Implement "Packet Loss" logic (Drop late packets).

**Week 32 (Aug 3-9): Integration**

- [ ] **03 Mon AUG (AM):** **Read** _gRPC Documentation_ (Concepts).
- [ ] **03 Mon AUG (PM):** **Task:** Design gRPC Proto file.
- [ ] **04 Tue AUG (AM):** **Read** _Protocol Buffers Documentation_.
- [ ] **04 Tue AUG (PM):** **Task:** Generate Go and Python code from Proto.
- [ ] **05 Wed AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **05 Wed AUG (PM):** **Task:** Implement gRPC Server in Go.
- [ ] **06 Thu AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **06 Thu AUG (PM):** **Task:** Implement gRPC Client in Python.
- [ ] **07 Fri AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **07 Fri AUG (PM):** **Task:** Test Remote Control (Python controls Go).
- [ ] **08 Sat AUG (AM):** **System Design:** Design Search Autocomplete.
- [ ] **08 Sat AUG (PM):** **Deep Work:** Integrate UDP Audio Router with gRPC Control.
- [ ] **09 Sun AUG (AM):** **Read:** Review gRPC patterns.
- [ ] **09 Sun AUG (PM):** **Review:** Check for deadlocks.

**Week 33 (Aug 10-16): Docker & Optimizations**

- [ ] **10 Mon AUG (AM):** **Read** _Docker Docs_ (Multi-stage builds).
- [ ] **10 Mon AUG (PM):** **Task:** Create Dockerfile for Go.
- [ ] **11 Tue AUG (AM):** **Read** _Docker Docs_ (Networking).
- [ ] **11 Tue AUG (PM):** **Task:** Use Multi-stage build.
- [ ] **12 Wed AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **12 Wed AUG (PM):** **Task:** Optimize Binary Size (Scratch image).
- [ ] **13 Thu AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **13 Thu AUG (PM):** **Task:** Dockerize Python Controller.
- [ ] **14 Fri AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **14 Fri AUG (PM):** **Task:** Create docker-compose for both.
- [ ] **15 Sat AUG (AM):** **System Design:** Design Distributed Lock.
- [ ] **15 Sat AUG (PM):** **Deep Work:** Final System Test.
- [ ] **16 Sun AUG (AM):** **Read:** Review Docker best practices.
- [ ] **16 Sun AUG (PM):** **Catch Up.**

**Week 34 (Aug 17-23): Final Polish**

- [ ] **17 Mon AUG (AM):** **Read** _Observability Engineering_ (Logs).
- [ ] **17 Mon AUG (PM):** **Task:** Add Logging.
- [ ] **18 Tue AUG (AM):** **Read** _Observability Engineering_ (Metrics).
- [ ] **18 Tue AUG (PM):** **Task:** Add Metrics (Packets/sec).
- [ ] **19 Wed AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **19 Wed AUG (PM):** **Task:** Write README.
- [ ] **20 Thu AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **20 Thu AUG (PM):** **Task:** Record Demo.
- [ ] **21 Fri AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **21 Fri AUG (PM):** **Task:** Final Refactor.
- [ ] **22 Sat AUG (All Day):** **Release:** Virtual Patchbay v1.0.
- [ ] **23 Sun AUG (All Day):** **Rest.**

### **SEPTEMBER: The Systems Bridge**

**Week 35 (Aug 24-30): Integration & Cleanup**

- [ ] **24 Mon AUG (AM):** **Read** _Clean Code_ (Refactoring).
- [ ] **24 Mon AUG (PM):** **Task:** Code Review - Virtual Patchbay.
- [ ] **25 Tue AUG (AM):** **Algorithm Practice:** LeetCode (Medium) in Go.
- [ ] **25 Tue AUG (PM):** **Task:** Fix outstanding bugs.
- [ ] **26 Wed AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **26 Wed AUG (PM):** **Task:** Improve Documentation.
- [ ] **27 Thu AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **27 Thu AUG (PM):** **Task:** Add Integration Tests.
- [ ] **28 Fri AUG (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **28 Fri AUG (PM):** **Task:** Create Release Tags.
- [ ] **29 Sat AUG (AM):** **System Design:** Design Metadata Service.
- [ ] **29 Sat AUG (PM):** **Deep Work:** Prepare for Q4 (Cloud).
- [ ] **30 Sun AUG (AM):** **Read:** Overview of Terraform.
- [ ] **30 Sun AUG (PM):** **Rest.**

**Week 36 (Aug 31-Sep 6): Python/Go Interaction**

- [ ] **31 Mon AUG (AM):** **Read** _Python High Performance_ (FFI).
- [ ] **31 Mon AUG (PM):** **Task:** Research calling Go from Python (Ctypes/CGO).
- [ ] **01 Tue SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **01 Tue SEP (PM):** **Task:** Build small Shared Library in Go.
- [ ] **02 Wed SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **02 Wed SEP (PM):** **Task:** Call Go func from Python.
- [ ] **03 Thu SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **03 Thu SEP (PM):** **Task:** Benchmark vs pure Python.
- [ ] **04 Fri SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **04 Fri SEP (PM):** **Task:** Document findings.
- [ ] **05 Sat SEP (AM):** **System Design:** Design CDN.
- [ ] **05 Sat SEP (PM):** **Deep Work:** Polish Systems Knowledge.
- [ ] **06 Sun SEP (AM):** **Read:** Review CGO docs.
- [ ] **06 Sun SEP (PM):** **Catch Up.**

**Week 37 (Sep 7-13): Container Orchestration Prep**

- [ ] **07 Mon SEP (AM):** **Read** _Kubernetes Docs_ (Concepts).
- [ ] **07 Mon SEP (PM):** **Task:** Install Minikube/Kind.
- [ ] **08 Tue SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **08 Tue SEP (PM):** **Task:** Write simple Pod yaml.
- [ ] **09 Wed SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **09 Wed SEP (PM):** **Task:** Deploy Nginx to K8s.
- [ ] **10 Thu SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **10 Thu SEP (PM):** **Task:** Expose Service via NodePort.
- [ ] **11 Fri SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **11 Fri SEP (PM):** **Task:** Deploy Virtual Patchbay to K8s.
- [ ] **12 Sat SEP (AM):** **System Design:** Design Scheduler.
- [ ] **12 Sat SEP (PM):** **Deep Work:** Understand K8s Services vs Ingress.
- [ ] **13 Sun SEP (AM):** **Read:** Review K8s Architecture.
- [ ] **13 Sun SEP (PM):** **Rest.**

**Week 38 (Sep 14-20): Pre-Cloud Config**

- [ ] **14 Mon SEP (AM):** **Read** _12 Factor App_ Manifesto.
- [ ] **14 Mon SEP (PM):** **Task:** Audit apps for 12-factor compliance.
- [ ] **15 Tue SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **15 Tue SEP (PM):** **Task:** Externalize all config (Env Vars).
- [ ] **16 Wed SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **16 Wed SEP (PM):** **Task:** Ensure statelessness.
- [ ] **17 Thu SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **17 Thu SEP (PM):** **Task:** Setup AWS Free Tier Account.
- [ ] **18 Fri SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **18 Fri SEP (PM):** **Task:** Setup AWS CLI & IAM User.
- [ ] **19 Sat SEP (AM):** **System Design:** Design Job Queue.
- [ ] **19 Sat SEP (PM):** **Deep Work:** Secure AWS Account (MFA, Billing Alarms).
- [ ] **20 Sun SEP (AM):** **Read:** Review IAM Best Practices.
- [ ] **20 Sun SEP (PM):** **Rest.**

**Week 39 (Sep 21-27): Final Prep**

- [ ] **21 Mon SEP (AM):** **Read** _Terraform Intro_.
- [ ] **21 Mon SEP (PM):** **Task:** Clean up GitHub Repos.
- [ ] **22 Tue SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **22 Tue SEP (PM):** **Task:** Update Resume with Go Skills.
- [ ] **23 Wed SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **23 Wed SEP (PM):** **Task:** Plan Q4 Architecture.
- [ ] **24 Thu SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **24 Thu SEP (PM):** **Task:** Create Q4 Repo `orbital-stream`.
- [ ] **25 Fri SEP (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **25 Fri SEP (PM):** **Task:** Initialize README for Q4.
- [ ] **26 Sat SEP (AM):** **System Design:** Design Big Data Pipeline.
- [ ] **26 Sat SEP (PM):** **Deep Work:** Rest & Recover.
- [ ] **27 Sun SEP (AM):** **Read:** Review Q3 Progress.
- [ ] **27 Sun SEP (PM):** **Review:** Ready for Q4.

---

## ☁️ Q4: The Cloud Architect (Oct - Dec)

**Project:** "Orbital Stream" (Big Data)
**Goal:** Infrastructure as Code & Distributed Systems.

### **OCTOBER: Infrastructure as Code**

**Week 40 (Sep 28-Oct 4): Terraform**

- [ ] **28 Mon SEP (AM):** **Read** _Terraform: Up & Running_.
- [ ] **28 Mon SEP (PM):** **Task:** Install Terraform.
- [ ] **29 Tue SEP (AM):** **Read** _Terraform Docs_ (Providers).
- [ ] **29 Tue SEP (PM):** **Task:** Write a `.tf` file to define an AWS VPC.
- [ ] **30 Wed SEP (AM):** **Read** _Terraform Docs_ (Resources).
- [ ] **30 Wed SEP (PM):** **Task:** Define Subnets and Security Groups.
- [ ] **01 Thu OCT (AM):** **Read** _AWS Docs_ (EC2).
- [ ] **01 Thu OCT (PM):** **Task:** Define EC2 Instance.
- [ ] **02 Fri OCT (AM):** **Read** _AWS Docs_ (RDS).
- [ ] **02 Fri OCT (PM):** **Task:** Define RDS Instance.
- [ ] **03 Sat OCT (AM):** **System Design:** Design AWS Deployment Architecture.
- [ ] **03 Sat OCT (PM):** **Constraint:** Deploy resources using ONLY Terraform. No Console clicking.
- [ ] **04 Sun OCT (AM):** **Read:** Review `terraform state`.
- [ ] **04 Sun OCT (PM):** **Review:** Understand `terraform state`.

**Week 41 (Oct 5-11): Kafka**

- [ ] **05 Mon OCT (AM):** **Read** _DDIA_ (Ch 6: Partitioning).
- [ ] **05 Mon OCT (PM):** **Task:** Spin up Kafka (Redpanda) in Docker.
- [ ] **06 Tue OCT (AM):** **Read** _Kafka Docs_ (Producers).
- [ ] **06 Tue OCT (PM):** **Task:** Write a Go Producer (sends data to Kafka).
- [ ] **07 Wed OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **07 Wed OCT (PM):** **Task:** Produce 10,000 messages/sec.
- [ ] **08 Thu OCT (AM):** **Read** _Kafka Docs_ (Consumers).
- [ ] **08 Thu OCT (PM):** **Task:** Write a Python Consumer (reads data from Kafka).
- [ ] **09 Fri OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **09 Fri OCT (PM):** **Task:** Handle Offset Commits.
- [ ] **10 Sat OCT (AM):** **System Design:** Design Event Sourcing System.
- [ ] **10 Sat OCT (PM):** **Task:** Write a Python Consumer (reads data from Kafka).
- [ ] **11 Sun OCT (AM):** **Read:** Review Kafka Consumer Groups.
- [ ] **11 Sun OCT (PM):** **Deep Work:** Handle Kafka Consumer Groups.

**Week 42 (Oct 12-18): TimescaleDB**

- [ ] **12 Mon OCT (AM):** **Read** _TimescaleDB Docs_ (Hypertables).
- [ ] **12 Mon OCT (PM):** **Task:** Setup TimescaleDB (Postgres for Time Series).
- [ ] **13 Tue OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **13 Tue OCT (PM):** **Task:** Define Hypertables.
- [ ] **14 Wed OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **14 Wed OCT (PM):** **Task:** Connect Consumer to DB.
- [ ] **15 Thu OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **15 Thu OCT (PM):** **Task:** Write Batch Inserts.
- [ ] **16 Fri OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **16 Fri OCT (PM):** **Task:** Optimize Insert Rate.
- [ ] **17 Sat OCT (AM):** **System Design:** Design Metrics Monitor.
- [ ] **17 Sat OCT (PM):** **Deep Work:** Analytics: Write SQL queries to find "Fuel Anomalies" over time.
- [ ] **18 Sun OCT (AM):** **Read:** Review SQL Optimization.
- [ ] **18 Sun OCT (PM):** **Review:** Optimize SQL using Hypertable partitioning.

**Week 43 (Oct 19-25): Integration**

- [ ] **19 Mon OCT (AM):** **Read** _DDIA_ (Ch 8: Distributed Systems).
- [ ] **19 Mon OCT (PM):** **Task:** Connect Go Producer to Constellation Command.
- [ ] **20 Tue OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **20 Tue OCT (PM):** **Task:** Connect Kafka to DB.
- [ ] **21 Wed OCT (AM):** **Read** _Grafana Docs_.
- [ ] **21 Wed OCT (PM):** **Task:** Visualize Data in Grafana.
- [ ] **22 Thu OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **22 Thu OCT (PM):** **Task:** Monitor Lag.
- [ ] **23 Fri OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **23 Fri OCT (PM):** **Task:** Dockerize everything.
- [ ] **24 Sat OCT (AM):** **System Design:** Design Log Aggregator.
- [ ] **24 Sat OCT (PM):** **Deep Work:** Full System Test.
- [ ] **25 Sun OCT (AM):** **Read:** Review Architecture.
- [ ] **25 Sun OCT (PM):** **Catch Up.**

### **NOVEMBER: Deployment**

**Week 44 (Oct 26-Nov 1): Cloud Deployment**

- [ ] **26 Mon OCT (AM):** **Read** _Terraform_ (Modules).
- [ ] **26 Mon OCT (PM):** **Task:** Terraform for Kafka.
- [ ] **27 Tue OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **27 Tue OCT (PM):** **Task:** Terraform for DB.
- [ ] **28 Wed OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **28 Wed OCT (PM):** **Task:** Terraform for Apps.
- [ ] **29 Thu OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **29 Thu OCT (PM):** **Task:** Deploy to AWS.
- [ ] **30 Fri OCT (AM):** **Algorithm Practice:** LeetCode (Medium).
- [ ] **30 Fri OCT (PM):** **Task:** Verify connectivity.
- [ ] **31 Sat OCT (AM):** **System Design:** Design Global App Deployment.
- [ ] **31 Sat OCT (PM):** **Deep Work:** Load Test in the Cloud.
- [ ] **01 Sun NOV (AM):** **Read:** Review AWS Cost Management.
- [ ] **01 Sun NOV (PM):** **Review:** Check AWS Bill.

**Week 45 (Nov 2-8): System Design Study**

- [ ] **02 Mon NOV (AM):** **Read** _DDIA_ (Part 2: Distributed Systems).
- [ ] **02 Mon NOV (PM):** **Task:** Watch "System Design Interview" videos (MIT/Google).
- [ ] **03 Tue NOV (AM):** **Read** _DDIA_ (Replication).
- [ ] **03 Tue NOV (PM):** **Task:** Practice "Design a URL Shortener" on whiteboard.
- [ ] **04 Wed NOV (AM):** **Read** _DDIA_ (Partitioning).
- [ ] **04 Wed NOV (PM):** **Task:** Practice "Design a Web Crawler".
- [ ] **05 Thu NOV (AM):** **Read** _DDIA_ (Transactions).
- [ ] **05 Thu NOV (PM):** **Task:** Practice "Design a Chat System".
- [ ] **06 Fri NOV (AM):** **Read** _DDIA_ (Consistency).
- [ ] **06 Fri NOV (PM):** **Task:** Practice "Design a Rate Limiter".
- [ ] **07 Sat NOV (AM):** **System Design:** Full Mock Interview (45 min).
- [ ] **07 Sat NOV (PM):** **Deep Work:** Review "Alex Xu" System Design book.
- [ ] **08 Sun NOV (AM):** **Read:** Review System Design Notes.
- [ ] **08 Sun NOV (PM):** **Rest.**

**Week 46 (Nov 9-15): Design Docs**

- [ ] **09 Mon NOV (AM):** **Read** _Google SRE Book_ (Service Levels).
- [ ] **09 Mon NOV (PM):** **Task:** Draft a design doc for "Design Twitter".
- [ ] **10 Tue NOV (AM):** **Algorithm Practice:** LeetCode (Hard).
- [ ] **10 Tue NOV (PM):** **Task:** Critique your design doc. Find bottlenecks.
- [ ] **11 Wed NOV (AM):** **Algorithm Practice:** LeetCode (Hard).
- [ ] **11 Wed NOV (PM):** **Task:** Draft a design doc for "Design Uber".
- [ ] **12 Thu NOV (AM):** **Algorithm Practice:** LeetCode (Hard).
- [ ] **12 Thu NOV (PM):** **Task:** Critique Uber design. Focus on Geospatial index.
- [ ] **13 Fri NOV (AM):** **Algorithm Practice:** LeetCode (Hard).
- [ ] **13 Fri NOV (PM):** **Task:** Peer review (or self-review) design docs.
- [ ] **14 Sat NOV (AM):** **System Design:** Design YouTube.
- [ ] **14 Sat NOV (PM):** **Deep Work:** Polish Design Docs for Portfolio.
- [ ] **15 Sun NOV (AM):** **Read:** Review Portfolio.
- [ ] **15 Sun NOV (PM):** **Catch Up.**

**Week 47 (Nov 16-22): Mock Interviews**

- [ ] **16 Mon NOV (AM):** **Algorithm Practice:** Timed Mock (20 min).
- [ ] **16 Mon NOV (PM):** **Task:** Record yourself explaining an algorithm.
- [ ] **17 Tue NOV (AM):** **Algorithm Practice:** Timed Mock (20 min).
- [ ] **17 Tue NOV (PM):** **Task:** Record yourself explaining System Design.
- [ ] **18 Wed NOV (AM):** **Algorithm Practice:** Timed Mock (20 min).
- [ ] **18 Wed NOV (PM):** **Task:** Watch back recordings. Improve communication.
- [ ] **19 Thu NOV (AM):** **Algorithm Practice:** Timed Mock (20 min).
- [ ] **19 Thu NOV (PM):** **Task:** Behavioral Interview prep (STAR method).
- [ ] **20 Fri NOV (AM):** **Algorithm Practice:** Timed Mock (20 min).
- [ ] **20 Fri NOV (PM):** **Task:** Mock Interview with friend or online.
- [ ] **21 Sat NOV (AM):** **System Design:** Design Ticketmaster.
- [ ] **21 Sat NOV (PM):** **Deep Work:** Final Interview Prep.
- [ ] **22 Sun NOV (AM):** **Read:** Review Weaknesses.
- [ ] **22 Sun NOV (PM):** **Rest.**

### **DECEMBER: Final Defense**

**Week 48 (Nov 23-29): The Portfolio**

- [ ] **23 Mon NOV (AM):** **Read** _Career Guide_ (Negotiation).
- [ ] **23 Mon NOV (PM):** **Task:** Final Polish of all 4 GitHub Repos.
- [ ] **24 Tue NOV (AM):** **Algorithm Practice:** Maintenance (1 Problem).
- [ ] **24 Tue NOV (PM):** **Task:** Write a "Case Study" blog post for the Orbital Stream project.
- [ ] **25 Wed NOV (AM):** **Algorithm Practice:** Maintenance (1 Problem).
- [ ] **25 Wed NOV (PM):** **Task:** Update LinkedIn: "Senior Backend Engineer".
- [ ] **26 Thu NOV (AM):** **Algorithm Practice:** Maintenance (1 Problem).
- [ ] **26 Thu NOV (PM):** **Task:** Reach out to recruiters.
- [ ] **27 Fri NOV (AM):** **Algorithm Practice:** Maintenance (1 Problem).
- [ ] **27 Fri NOV (PM):** **Task:** Apply to 5 "Dream" companies.
- [ ] **28 Sat NOV (AM):** **System Design:** Review all notes.
- [ ] **28 Sat NOV (PM):** **Deep Work:** Portfolio Website update (if applicable).
- [ ] **29 Sun NOV (AM):** **Read:** Review Year's Progress.
- [ ] **29 Sun NOV (PM):** **Rest.**

**Week 49 (Nov 30-Dec 6): The Job Hunt (Sprint 1)**

- [ ] **30 Mon NOV (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **30 Mon NOV (PM):** **Task:** Apply to 5 Companies (Tailored Cover Letters).
- [ ] **01 Tue DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **01 Tue DEC (PM):** **Task:** Apply to 5 Companies.
- [ ] **02 Wed DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **02 Wed DEC (PM):** **Task:** Apply to 5 Companies.
- [ ] **03 Thu DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **03 Thu DEC (PM):** **Task:** Apply to 5 Companies.
- [ ] **04 Fri DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **04 Fri DEC (PM):** **Task:** Apply to 5 Companies.
- [ ] **05 Sat DEC (AM):** **System Design:** Review Scalability Patterns.
- [ ] **05 Sat DEC (PM):** **Deep Work:** Technical Screening Prep (Phone screen drills).
- [ ] **06 Sun DEC (AM):** **Read:** Rest.
- [ ] **06 Sun DEC (PM):** **Review:** Weekly Application Tracker.

**Week 50 (Dec 7-13): The Job Hunt (Interview Mode)**

- [ ] **07 Mon DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **07 Mon DEC (PM):** **Task:** Follow up on Week 49 Applications.
- [ ] **08 Tue DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **08 Tue DEC (PM):** **Task:** Apply to 3 "High Value" Companies.
- [ ] **09 Wed DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **09 Wed DEC (PM):** **Task:** Apply to 3 "High Value" Companies.
- [ ] **10 Thu DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **10 Thu DEC (PM):** **Task:** Mock Interview (Behavioral).
- [ ] **11 Fri DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **11 Fri DEC (PM):** **Task:** Mock Interview (Technical).
- [ ] **12 Sat DEC (AM):** **System Design:** Review Database Sharding.
- [ ] **12 Sat DEC (PM):** **Deep Work:** Study specific companies (Architecture blogs).
- [ ] **13 Sun DEC (AM):** **Read:** Rest.
- [ ] **13 Sun DEC (PM):** **Review:** Adjust Resume based on feedback.

**Week 51 (Dec 14-20): The Job Hunt (Sprint 2)**

- [ ] **14 Mon DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **14 Mon DEC (PM):** **Task:** Apply to 5 Companies.
- [ ] **15 Tue DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **15 Tue DEC (PM):** **Task:** Apply to 5 Companies.
- [ ] **16 Wed DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **16 Wed DEC (PM):** **Task:** Apply to 5 Companies.
- [ ] **17 Thu DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **17 Thu DEC (PM):** **Task:** Apply to 5 Companies.
- [ ] **18 Fri DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **18 Fri DEC (PM):** **Task:** Apply to 5 Companies.
- [ ] **19 Sat DEC (AM):** **System Design:** Review Caching Strategies.
- [ ] **19 Sat DEC (PM):** **Deep Work:** Prepare for Technical Take-home tests.
- [ ] **20 Sun DEC (AM):** **Read:** Rest.
- [ ] **20 Sun DEC (PM):** **Review:** Weekly Tracker.

**Week 52 (Dec 21-27): Maintenance & Holiday**

- [ ] **21 Mon DEC (AM):** **Algorithm Practice:** 1 LeetCode Easy (Maintenance).
- [ ] **21 Mon DEC (PM):** **Task:** Light coding (Open Source contribution).
- [ ] **22 Tue DEC (AM):** **Algorithm Practice:** 1 LeetCode Easy.
- [ ] **22 Tue DEC (PM):** **Task:** Read Engineering Blogs (Netflix/Uber).
- [ ] **23 Wed DEC (AM):** **Algorithm Practice:** 1 LeetCode Easy.
- [ ] **23 Wed DEC (PM):** **Task:** Networking (LinkedIn holiday messages).
- [ ] **24 Thu DEC:** **Holiday:** Rest.
- [ ] **25 Fri DEC:** **Holiday:** Rest.
- [ ] **26 Sat DEC:** **Holiday:** Rest.
- [ ] **27 Sun DEC (AM):** **Read:** Year End Review.
- [ ] **27 Sun DEC (PM):** **Review:** Plan 2027 Goals.

**Week 53 (Dec 28-31): Final Push**

- [ ] **28 Mon DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **28 Mon DEC (PM):** **Task:** Respond to Recruiters (Jan hiring surge).
- [ ] **29 Tue DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **29 Tue DEC (PM):** **Task:** Schedule Interviews for Jan.
- [ ] **30 Wed DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **30 Wed DEC (PM):** **Task:** Final Organize of local files.
- [ ] **31 Thu DEC (AM):** **Algorithm Practice:** 1 LeetCode Medium.
- [ ] **31 Thu DEC (PM):** **Task:** Mission Accomplished.
- [ ] **01 Jan 2027:** **Task:** Start your new job.
