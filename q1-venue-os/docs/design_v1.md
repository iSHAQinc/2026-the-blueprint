# Technical Design Doc: VenueOS (v1.0)

**Author:** [Omar Ishaq
**Status:** Draft
**Date:** 2026-01-01

## 1. Context & Scope

VenueOS is a high-concurrency facility management system. It allows venue managers to define complex spaces (buildings, floors, rooms) and allows users to book these spaces.

**Core Problem:** Preventing "Double Bookings" (Race Conditions) when thousands of users try to book the same slot simultaneously.

**In Scope:**

- User Authentication (Admin, Manager, Customer).
- Venue/Space Management (Recursive hierarchy).
- Booking Engine with ACID compliance.
- Basic Availability Search.

**Out of Scope (for v1):**

- Payment Gateway Integration (Stripe).
- Visual Interactive Maps.

## 2. Architecture Overview

We will use a standard **Monolithic Architecture** for v1 to ensure data consistency. Distributed systems (Microservices) introduce complexity that is unnecessary for strict transactional integrity at this stage.

- **Backend:** Python (Django 5.x)
- **Database:** PostgreSQL 16+ (Required for Row-level locking)
- **API:** Django REST Framework (DRF)
- **Containerization:** Docker & Docker Compose

## 3. Database Schema (The Data Model)

This is the most critical section. We need a relational schema that supports hierarchy and strict integrity.

### 3.1. Users (`CustomUser`)

_We replace the default Django User to allow future scalability (e.g., adding 'Organization' fields)._

- `id`: UUID (Primary Key)
- `email`: EmailField (Unique, Username)
- `role`: Enum (ADMIN, MANAGER, CUSTOMER)
- `is_active`: Boolean

### 3.2. Venues (`Venue`)

_The top-level entity (e.g., "Wembley Stadium" or "Main Library")._

- `id`: UUID
- `name`: CharField
- `owner`: ForeignKey(User)
- `timezone`: CharField (Critical for booking logic)

### 3.3. Spaces (`Space`) - **The Recursive Model**

_A Space can be a building, a floor, or a specific room. We use an Adjacency List pattern._

- `id`: UUID
- `venue`: ForeignKey(Venue)
- `parent`: ForeignKey('self', null=True, related_name='children')
  - _Logic:_ If `parent` is Null, it is a top-level building. If `parent` is set, it is a room inside that parent.
- `name`: CharField
- `capacity`: Integer
- `is_bookable`: Boolean (e.g., A "Floor" might not be bookable, but the "Room" inside it is).

### 3.4. Bookings (`Booking`)

- `id`: UUID
- `user`: ForeignKey(User)
- `space`: ForeignKey(Space)
- `start_time`: DateTime
- `end_time`: DateTime
- `status`: Enum (CONFIRMED, CANCELLED, PENDING)

## 4. Key Constraints & Data Integrity

### 4.1. Preventing Overlaps (The "Hard" Part)

We cannot rely on Python code alone to prevent double bookings. We must enforce this at the Database level where possible.

**Strategy:**

1.  **Postgres Exclusion Constraint (B-Tree/GIST):** We will try to implement a Postgres constraint that forbids two rows for the same `space_id` to have overlapping `tstzrange` (Timestamp Ranges).
2.  **Application Locking:** When creating a booking, we will use `transaction.atomic()` and `select_for_update` to lock the rows.

### 4.2. Hierarchy Logic

- A booking on a "Parent" space (e.g., The Whole Hall) must block bookings on "Child" spaces (e.g., Room A inside the Hall).
- _Decision:_ For v1, we will only allow bookings on the "Leaf" nodes (the smallest unit) to simplify logic, or explicit logic to check parent availability.

## 5. API Design (Draft)

- `GET /api/venues/` - List venues
- `POST /api/bookings/` - Create a booking
  - Input: `{ space_id, start_time, end_time }`
  - Output: `201 Created` or `409 Conflict` (if taken)

## 6. Open Questions

- How do we handle "Opening Hours"? (e.g., The venue is closed on Sundays).
  - _Proposed Solution:_ A separate `AvailabilityRule` model linked to Venue.
