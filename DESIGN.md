---
name: "Max Gloves BD Ltd — Architectural Industrial PPE Showcase"
description: "Authoritative B2B industrial PPE exporter showcase design system"
colors:
  steel: "#0B1118"
  crimson: "#C81E1E"
  canvas: "#F8FAFC"
  well: "#F1F5F9"
  card: "#FFFFFF"
  border: "#E2E8F0"
  border-dark: "#CBD5E1"
  text-muted: "#64748B"
  text-body: "#334155"
typography:
  headline:
    fontFamily: "Barlow, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontWeight: 700
  body:
    fontFamily: "'Public Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontWeight: 400
  mono:
    fontFamily: "'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontWeight: 600
rounded:
  sm: "3px"
  md: "4px"
components:
  button-primary:
    backgroundColor: "{colors.crimson}"
    textColor: "#FFFFFF"
    rounded: "{rounded.md}"
    padding: "10px 22px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.steel}"
    rounded: "{rounded.md}"
    padding: "10px 22px"
---

# Design System: Max Gloves BD Ltd.

## Overview
An architectural, high-precision industrial PPE exporter showcase designed for international procurement officers, safety directors, and wholesale importers across Europe, North America, Japan, and Korea. The aesthetic communicates manufacturing authority, certified compliance, physical durability, and operational transparency.

## Colors
- **Carbon Steel (`#0B1118`)**: Primary dark anchor for structural headers, timelines, metric strips, and authoritative typography. Never pure black.
- **Industrial Crimson (`#C81E1E`)**: High-contrast, safety-critical accent used for CTAs, RFQ triggers, active states, and focal cues. Replaces low-contrast orange (`#F66202`). WCAG AAA/AA compliant (>5.6:1 contrast ratio against light backgrounds).
- **Light Canvas (`#F8FAFC`)**: Slate-tinted neutral background for clean readability and reduced glare. Never pure white full-bleed.
- **Studio Well (`#F1F5F9`)**: Neutral 4:3 product photography wells providing consistent lighting and high object definition without distracting background clutter.
- **Structural Border (`#E2E8F0`)**: Crisp 1px solid dividers defining containers, technical grids, and card perimeters. Darker counterpart: `#CBD5E1`.

## Typography
Strictly curated 3-font hierarchy. Default Inter and generic Arial fonts are strictly banned.

1. **Barlow (`sans-serif`, weights 600, 700, 800)**:
   - Primary display and section heading font.
   - Low-contrast industrial proportions, tight letter-spacing (`-0.02em`), confident and authoritative.
2. **Public Sans (`sans-serif`, weights 400, 500, 600, 700)**:
   - Body copy, narrative blocks, paragraph specifications, form labels, and operational copy.
   - Clean legibility, balanced x-height, comfortable reading rhythm.
3. **IBM Plex Mono (`monospace`, weights 500, 600, 700)**:
   - SKU codes (`SKU: #MG-204`), technical badges, tabular counters (`01 // KNITTING`), metrics (`500,000+ DZN/MO`), timestamps, and breadcrumbs.
   - Tabular figures (`font-variant-numeric: tabular-nums`) guarantee zero visual jitter during animations and scans.

## Layout
- **Architectural Grid**: 12-column responsive grid with standardized 24px/32px gutters.
- **Zero Layout Shift Sticky Header**:
  - Compact `#0B1118` topbar with real-time operational status and compliant touch targets.
  - Sticky navigation bar with fixed height reservation, ensuring 0 CLS during scroll pinning.
  - Multi-category glove mega-menu with visual catalog thumbnails and clear categorical grouping.
- **Mobile Navigation Drawer**:
  - Slide-in architectural panel from right with full `aria-expanded`, `aria-controls`, and keyboard `Escape` trap.
  - Dedicated accordion drawers for 7 core glove categories.

## Elevation & Depth
- **Structural Planar Hierarchy**: Depth is established via crisp 1px borders (`#E2E8F0`) and contrast shifts (`#0B1118` vs `#F8FAFC`) rather than heavy blurred drop-shadows.
- **Subtle Elevation**: Hover states utilize micro-elevations (`box-shadow: 0 8px 24px rgba(11, 17, 24, 0.06)`) paired with `translateY(-2px)` transitions.
- **Dark Scrims**: High-contrast linear gradients (`linear-gradient(90deg, rgba(11, 17, 24, 0.92) 0%, rgba(11, 17, 24, 0.5) 100%)`) over hero sliders ensure text passes WCAG AAA readability.

## Shapes
- **Radius Standard**: Fixed **4px** border radius (`var(--radius-md)`) across all buttons, cards, containers, input fields, and studio wells.
- **Banned Geometries**:
  - No pill-shaped containers for cards.
  - No nested cards within cards.
  - No side-tab thick colored borders (AI visual artifact).

## Components
- **Product Item Card**:
  - Fixed 4:3 studio well (`aspect-ratio: 4/3`, background `#F1F5F9`).
  - Centered product imagery with `object-fit: contain` and `filter: drop-shadow(...)`.
  - Floating top badges for SKU code and 3D preview indicators.
  - Dedicated card body with category kicker, product title, and forward inspection link.
- **4-Step Industrial Timeline**:
  - Full-width dark carbon-steel (`#0B1118`) section container.
  - Tabular counters (`01`, `02`, `03`, `04`) in IBM Plex Mono.
  - Step code badges (`STAGE // 01`, `STAGE // 02`) with studio process imagery and technical specs.
- **Certification Trust Grid**:
  - Symmetrical 1px `#E2E8F0` bordered matrix with verified SVG vector marks (ISO 9001:2015, ISO 14001:2015, CE EN 388, BSCI, OEKO-TEX Standard 100).
- **Interactive 3D Product Scrubber**:
  - Isolated horizontal scrub interaction with `touch-action: pan-y` to prevent vertical mobile scroll hijacking.
  - Frame counter (`FRAME 01 / 36`) and one-click RFQ launcher pre-filling SKU details.

## Do's and Don'ts
- **DO** use IBM Plex Mono for all numeric measurements, SKUs, step numbers, and technical metadata.
- **DO** maintain 1px `#E2E8F0` structural borders with 4px radii.
- **DO** maintain authentic Savar, Dhaka facility credentials and export positioning.
- **DON'T** use generic Arial or Inter fonts anywhere.
- **DON'T** add thick side-tab borders on alert or card left edges.
- **DON'T** use pure `#000000` black or washed out low-contrast gray text.
- **DON'T** reintroduce ungrounded historical claims or fake e-commerce shopping carts.
