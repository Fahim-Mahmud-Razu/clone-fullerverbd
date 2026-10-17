# Agent instructions — Fullever BD faithful clone

## Mission

Build a complete public-site clone of [https://www.fulleverbd.com/](https://www.fulleverbd.com/) using the companion [design.md](./design.md). Preserve the reference site's visual design and observable behavior across desktop, mobile, category/product pages, and its Japanese/Korean versions. Finish the full route/content/asset inventory before claiming complete coverage.

This file is an implementation brief supplied as `agent.md`, as requested. A coding tool that automatically discovers `AGENTS.md` can use a copy under that conventional filename in the implementation repository. This documentation delivery itself does not scaffold or deploy an application.

## Recommended technology stack

**Decision: Astro + TypeScript + precise CSS + minimal vanilla TypeScript.** The reference is a public company/catalog site with repeated static templates and a few interactive components. Astro fits that structure, generates navigable HTML pages, and lets CSS/markup fidelity drive the implementation. Its default architecture sends no framework runtime unless a component needs one. [Astro architecture](https://docs.astro.build/en/concepts/why-astro/)

| Layer | Choice | Purpose |
| --- | --- | --- |
| Framework | Stable Astro release selected when implementation starts | Static multipage HTML, reusable layouts, generated catalog routes |
| Language | TypeScript, strict configuration | Typed content, safe IDs/assets, browser interactions |
| Runtime | Supported even-numbered Node LTS meeting Astro requirements | Repeatable development/build environment |
| Package management | npm with committed `package-lock.json` | Reproducible dependencies; `npm ci` in CI |
| Styling | Verified source CSS as a compatibility layer, then page/component CSS | Exact source geometry and cascade |
| Grid compatibility | Original Bootstrap 4.3.1 CSS rules where needed | Preserve original breakpoint behavior and dimensions |
| Content | Typed local JSON/content files | Category/product/page/locale manifests |
| Media | Original assets stored locally under `public/` | Correct artwork, sprites, logos, fonts, size guides |
| Interactions | Small TypeScript modules | Menus, sliders, gallery, image viewer, popups, counters |
| Visual verification | Playwright screenshots and focused interaction checks | Compare reference/clone at identical states |
| Hosting | Static host with clean-path/direct-route support | Serve generated routes reliably |
| Inquiry delivery | One clone-owned serverless/API handler when production delivery is enabled | Validated contact submission with server-side credentials |
| Database/CMS | None for the initial replica | Public site does not establish a need for either |

Astro's current installation documentation lists Node ≥22.12.0 and excludes odd-numbered releases. Recheck requirements when installing, record the chosen versions, and commit the lockfile; this brief intentionally does not guess a future package version. [Astro installation](https://docs.astro.build/en/install-and-setup/)

### Architecture boundaries

- Use static output and file-based routes. Generate `/category/[id]` and `/product/[id]` with `getStaticPaths()`. Use one data record for each original ID. [Astro routing](https://docs.astro.build/en/guides/routing/)
- Keep traditional page navigation. Do not introduce a client-side SPA router or page transitions that differ from the source.
- Do not add React, Next.js, Tailwind, shadcn, Material UI, Redux, an ORM, or authentication merely to create the replica.
- Next.js is a reasonable future alternative if the scope becomes a substantial application, but its React/server feature model is unnecessary for the observed static catalog. Static export also changes which server features are available. [Next.js static exports](https://nextjs.org/docs/app/guides/static-exports)
- Bootstrap is a CSS compatibility layer here, not a reason to import its old JavaScript stack. Do not carry over duplicate jQuery versions, analytics tags, or unused plugins.
- Rebuild behavior in small modules. Add a maintained carousel dependency only if measured source behavior is impractical to reproduce accurately with a small module; style it to the reference and justify the addition.
- Product viewing is an image-sprite interaction. Do not use Three.js without evidence that a particular source product needs actual 3D rendering.
- Deploy only when requested. Use the user's chosen provider; a static host plus one inquiry handler is sufficient for the initial architecture.

## Mandatory fidelity rules

1. `design.md` and the current rendered reference are the visual authorities. A newer live capture supersedes an older cached page only when the difference is documented.
2. Do not redesign, simplify page coverage, modernize spacing, normalize copy, or invent missing content. Preserve source spelling, SKU leading zeroes, artwork text, duplicate labels, link targets, and locale differences.
3. Prefer original assets and dimensions. Avoid generic stock imagery, generated glove images, emoji replacements for existing icons, and placeholder products.
4. Preserve numeric IDs and source item order. Never deduplicate by product/category name. `/category/24` and `/category/25` are separate required records.
5. Match CSS cascade, not just approximate colors. Avoid new global resets. Page-specific overrides on About and facilities are part of the design.
6. Capture persistent defects and transient loading separately. Do not silently repair visible source quirks while describing the result as identical.
7. Keep original public social/mail/map behaviors where appropriate, but use clone-owned infrastructure for inquiry delivery. Never reuse the original production form action, tracking IDs, or map/API credentials.
8. Public HTML cannot establish unseen backend behavior. Report missing delivery configuration or inaccessible source assets precisely; do not fake successful inquiry delivery.
9. Do not claim pixel-perfect or complete until the route, asset, behavior, and visual checks below pass.

## Suggested implementation structure

```text
project/
  design.md
  agent.md
  astro.config.mjs
  package.json
  package-lock.json
  tsconfig.json
  public/
    front-end/                  # source-compatible asset paths if useful
    media-library/
    product-images/
    fonts/
  src/
    layouts/
      BaseLayout.astro
      AboutLayout.astro
    components/
      SiteHeader.astro
      MobileMenu.astro
      SiteFooter.astro
      PageBanner.astro
      HeroSlider.astro
      ProcessCards.astro
      CategoryCard.astro
      ProductCard.astro
      ProductViewer.astro
      CertificationSlider.astro
      GalleryGrid.astro
      ContactForm.astro
      ContactCardModal.astro
    data/
      navigation.json
      categories.json
      products.json
      gallery.json
      certifications.json
      pages.json
      locales.json
      assets.json
    pages/
      index.astro
      about.astro
      facilities.astro
      compliance.astro
      gallery.astro
      contact.astro
      raw-materials.astro
      cutting-process.astro
      sewing-process.astro
      packaging.astro
      category/[id].astro
      product/[id].astro
      404.astro
    styles/
      source-base.css
      source-grid.css
      shared.css
      home.css
      about.css
      facilities.css
      catalog.css
      gallery.css
      contact.css
    scripts/
      navigation.ts
      hero.ts
      certifications.ts
      gallery.ts
      product-viewer.ts
      contact.ts
      scroll.ts
  tests/
    routes.spec.ts
    interactions.spec.ts
    visuals.spec.ts
  reference/                   # dated captures + manifests, outside public output
  hosting/                     # provider-specific inquiry function if needed
```

This is a proposed structure, not files already created. Use shared process components rather than duplicating four layouts. Locale organization must follow the captured source inventory. Prefer configurable locale origins and one template system; do not assume every locale shares identical data or HTML.

## Content and asset contracts

Use explicit records with relationships rather than ad hoc arrays inside templates.

| Record | Required fields |
| --- | --- |
| Category | source ID, route, localized label, ordered product IDs, home tile asset, nav/home/footer placement |
| Product | source ID, route, category association, localized title, SKU string, source description structure, preview asset, optional sprite asset/frame metadata, optional sizing image or size list |
| Gallery image | stable ID, original order, thumbnail/full-image assets, filter groups, captured alt/caption |
| Main/process page | route, locale, title/breadcrumb, ordered blocks, image associations, source URL |
| Asset | original URL, local path, media type, intrinsic dimensions, usage, availability, optional checksum |
| Locale | language code, original origin, clone origin, source route coverage, label/font differences |

Do not flatten paragraphs, emphasized spans, lists, or tables if doing so changes wrapping or structure. Sanitize captured markup and keep data local. Do not put remote scripts or executable source-page content into the clone merely because it was captured.

Preserve asset bytes initially. Optimize only after comparison shows the output matches source cropping, dimensions, and color. Do not create responsive-image transformations that change the visible artwork. Use explicit image dimensions where compatible with source behavior and preload only the critical first artwork/font.

## Implementation sequence

### Phase 1 — Complete the reference capture

1. Read both briefs. Establish a dated reference baseline rather than relying on search-engine caches.
2. Visit the 146 known English routes from `design.md`; preserve all IDs and ordered category membership. Capture every product's actual title, SKU, preview, sprite, size information, and description.
3. Audit both localized sites fully. Record actual route coverage and translation content; do not extrapolate from English.
4. Capture top, middle, and footer screenshots at the agreed viewport matrix. Record actual loaded fonts, box dimensions, image fit, computed styles, and page-specific overrides.
5. Capture interaction states: desktop menus/sticky header; mobile menu/category expansion; hero controls; certification states; gallery filters/modal; product handle/frame changes; contact card; validation states.
6. Build a local asset manifest. Verify failures after settled loading, including backgrounds and sprites that do not appear as `<img>` elements.
7. Record unresolved observations explicitly. Do not submit forms on the reference site to discover backend results.

Deliver a usable local reference set and data manifest before treating approximate mockup content as final.

### Phase 2 — Build the shared shell and one complete route

1. Scaffold Astro with strict TypeScript and static output. Record runtime/dependency versions and lockfile.
2. Recreate base CSS order and grid behavior. Preserve the 1230px container override and legacy root-font scaling.
3. Implement header, mobile menu, banners, footer, and return-to-top. Verify normal/active/open states.
4. Complete the entire home page, including the current certification design. Match it by overlays before expanding all templates.
5. Keep each page's styles local where possible while reproducing page-specific effects on its shell.

### Phase 3 — Generate all content routes

1. Build category pages from the 13 category records and product pages from all 123 product records.
2. Confirm each generated route opens directly; do not use an SPA fallback that hides missing static pages.
3. Build About with its current green/navy system; facilities with its own grid; compliance with its policy/certification structure.
4. Build all four process pages with shared sidebar/slider components and route-specific media/text.
5. Build the 22-image gallery and exact filter groups.
6. Build contact with map, required five-field form, sales sidebar, and contact-card popup.
7. Build localized variants against their own captured routes/data/styles.

### Phase 4 — Match observable behavior

| Component | Required behavior |
| --- | --- |
| Desktop navigation | exact links, active item, product nesting, source hover timing, language destinations |
| Mobile navigation | hamburger/X; expandable products +/−; correct scroll/stack behavior |
| Hero | original artwork order, synchronized selected control, 2000ms source autoplay delay, 1000ms transition, hover pause, measured responsive controls |
| Certifications | observed arrow/dot paging, selected position, hover treatment, drag behavior if verified |
| Gallery | all 10 filters, active filter, correct visible images, modal open/close and boundary navigation |
| Product viewer | source preview and sprite association; correct frame/handle mapping; pointer/touch interaction |
| Contact card | same visible trigger/card/close layout and verified dismissal behavior |
| Contact form | source-like field validation plus truthful clone-owned pending/success/error states |
| Scroll effects | measured sticky threshold, counters if observed, return-to-top trigger/behavior |

Support keyboard operation and focus restoration without altering the normal visual state. Honor reduced-motion preferences where applicable; comparisons should use the same motion setting on reference and clone. Do not introduce extra product UI or visible implementation jargon.

### Phase 5 — Contact delivery configuration

For a functional published clone, connect the form to a clone-owned serverless/API endpoint. Validate name, email, phone, subject, and comments on the server; set sensible input limits and basic abuse controls; keep delivery credentials in server-only environment variables. Preserve the form's visible design.

Recipient address and sender/service credentials must come from project configuration. Do not assume the reference company's public email is the authorized recipient of clone submissions. Before configuration exists, keep submission behavior explicit in the development environment and mark delivery as pending; do not display a false success message. Use a local/test receiver for automated verification.

## Verification and completion gates

Set project scripts for `dev`, `build`, `preview`, `check`, and focused Playwright checks. Suggested developer workflow:

```sh
npm ci
npm run check
npm run build
npm run preview
npm run test:e2e
```

Add only meaningful tests: source route coverage and associations, critical interactions, inquiry validation/delivery states, and visual comparisons. Avoid tests that merely assert implementation-specific class names.

Playwright screenshot baselines must use the same environment, font readiness, device scale, viewport, scroll position, and controlled slider/counter state as the reference. Screenshot results are environment-dependent. [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots)

Required completion evidence:

- 146 English routes plus every discovered locale route; no missing known product IDs or category membership.
- All local images/fonts/sprites resolve or have a documented source failure faithfully handled.
- Source/clone overlays for every page template at desktop, tablet, narrow intermediate width, and mobile, plus full route screenshot coverage on desktop.
- No unexplained layout, crop, font, color, or content mismatch. Apply the proposed ≤0.5% unmasked pixel-difference gate with documented rendering-noise calibration and manual inspection.
- Mobile products and language menus; hero sync; gallery filter/modal; sprite handle; certification controls; contact-card popup; form states; and scroll behavior verified.
- Type/build checks pass, direct route reloads work, and no original production inquiry or analytics requests are sent.
- Delivery integration tested against a configured clone-owned test receiver, or clearly identified as awaiting credentials.
- A final report states what was built, how it was verified, and any specific remaining discrepancy. Never label a homepage-only replica or a generic template clone complete.

## Highest-priority pitfalls

The source contains several mixed design systems. About's newer body font stack and green/navy cards must coexist with legacy Roboto red/navy pages. Hero words are mostly baked into artwork. Category pages have a three-column 576–767px range unlike the home category grid. Both apparel categories must survive. Numeric SKUs retain zeroes. Product 3D controls use image sprites. Late thumbnail CSS changes crop and placement. Initial faded/stacked content must not become the settled screenshot baseline. Source resource errors must be distinguished from delayed loading.

Keep these details in the implementation checklist: they are the most likely reasons a plausible-looking clone would still fail the user's requirement that everything look the same.
