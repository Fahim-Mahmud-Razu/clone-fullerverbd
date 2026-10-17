# Fullever BD — faithful website clone specification

Reference: [fulleverbd.com](https://www.fulleverbd.com/). Inspection date: **1 October 2026**, Asia/Dhaka. Companion implementation instructions: [agent.md](./agent.md).

## 1. Objective and evidence

Reproduce the reference site's public appearance, content placement, navigation, responsive layouts, assets, and observable interactions. This is a fidelity project: preserve the site's existing design, including differences between pages. Do not turn it into a new brand, a modernized landing page, or an ecommerce store.

This specification is based on live browser inspection, rendered screenshots, DOM measurements, the original stylesheets, and a separate route audit. Desktop inspection used a 1440 × 900 viewport; mobile inspection used 390 × 844. Desktop content width was 1425px because the browser reserved scrollbar space. Measurements below are CSS pixels, not dimensions inferred from resized screenshot previews.

**Verified scope:** 10 English main/process routes, 13 category routes, and 123 distinct linked product routes: **146 English URLs**. All category IDs, counts, and ordered product IDs were checked against the live site. The home, About, facilities, compliance, gallery, contact, and four process pages were inspected live. Detailed live product inspection covered `/product/163`; other representative details were inspected through public web extraction.

Japanese and Korean homepages and linked destinations were audited through web extraction. Their complete live layouts, translations, and product coverage remain to be captured. No claim is made that all 123 product descriptions, every sprite, every localized page, or every hover state has already been measured.

The recommended build is **Astro + TypeScript + source-matched CSS + small browser scripts**, described in `agent.md`.

## 2. Fidelity requirements

- Keep original section order, visible labels, typography, text wrapping, images, image crops, colors, spacing, borders, shadows, and active states.
- Keep numeric category/product IDs and original clean URL paths. Preserve duplicate-looking records when their IDs differ.
- Reproduce desktop and mobile navigation, synchronized hero controls, gallery filtering/modal viewing, product image viewing, certification controls, and the contact-card popup.
- Treat each language site as its own reference. Do not generate translations or assume it contains the same products as English.
- Use the original artwork. Hero artwork contains baked-in text and graphics; substituting an HTML heading over a different photograph will not match it.
- Preserve observed visual inconsistencies. Record broken resources or unusual layouts and establish a settled reference before deciding how to reproduce them. Do not silently replace them with attractive placeholders.
- Keep inquiries on a clone-owned delivery endpoint. Public appearance can be copied without reusing the original site's form processor, analytics identifiers, or API credentials.

## 3. Routes and catalog inventory

### Main and process pages

| Route | Page type |
| --- | --- |
| `/` | Home |
| `/about` | Company profile, statistics, vision, commitments, sales CTA |
| `/facilities` | Factory overview, image, feature strip |
| `/compliance` | Compliance topics and certifications |
| `/gallery` | Filterable company photo gallery |
| `/contact` | Map, inquiry form, address, sales contacts, contact-card popup |
| `/raw-materials` | Process page |
| `/cutting-process` | Process page |
| `/sewing-process` | Process page |
| `/packaging` | Process page |

Navigation order is Home → About Us → Our Facilities → Compliance → Our Product → Gallery → Contact Us → Language. The product parent is an in-page `#` trigger, not a verified standalone product-index page. The logo links home. Main-page destinations are linked from the [reference homepage](https://www.fulleverbd.com/).

### Categories and ordered product IDs

Every ID below maps to `/product/{id}`. Counts and order are live observations, not suggested sample content.

| Category | Route | Count | Product IDs, in displayed order |
| --- | --- | ---: | --- |
| Leather Winter Gloves | `/category/23` | 6 | 163, 164, 166, 209, 211, 212 |
| Leather Driver Gloves | `/category/17` | 7 | 95, 109, 110, 112, 115, 116, 198 |
| Leather Grain Gloves | `/category/18` | 10 | 104, 106, 119, 120, 122, 124, 125, 127, 128, 129 |
| Leather Split Gloves | `/category/19` | 11 | 91, 113, 114, 117, 118, 133, 135, 136, 139, 142, 143 |
| Leather Welding Gloves | `/category/20` | 27 | 111, 123, 126, 132, 134, 148, 150, 151, 162, 173, 178, 179, 183, 184, 185, 186, 195, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226 |
| Leather Palm Gloves | `/category/21` | 11 | 93, 144, 147, 149, 152, 155, 156, 157, 159, 160, 161 |
| Leather Welding Apparel | `/category/24` | 7 | 84, 85, 180, 181, 182, 196, 197 |
| Leather Welding Apparel | `/category/25` | 7 | 167, 168, 175, 176, 177, 193, 194 |
| Synthetic Leather Gloves | `/category/27` | 9 | 170, 171, 172, 190, 191, 192, 200, 201, 204 |
| Mechanic's Gloves | `/category/29` | 12 | 174, 189, 202, 203, 206, 208, 210, 213, 214, 215, 227, 239 |
| Impact Gloves | `/category/30` | 3 | 187, 205, 207 |
| 100% Cotton Interlock Gloves | `/category/31` | 1 | 199 |
| Gardening Gloves | `/category/32` | 12 | 225, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238 |

The desktop/mobile dropdown has 12 categories: the table order with `/category/25` omitted. Both `/category/24` and `/category/25` appear in home/footer navigation and must exist. They have the same category heading but different product IDs. No category pagination controls were observed. See the [driver category](https://www.fulleverbd.com/category/17), [apparel category 24](https://www.fulleverbd.com/category/24), and [apparel category 25](https://www.fulleverbd.com/category/25).

### Language destinations

The language menu links to [Japanese](https://jp.fulleverbd.com/) and [Korean](https://kr.fulleverbd.com/) sites. Cached homepages expose 11 navigation categories and omit Gardening. Inspect their current live versions before treating that difference as final. For a self-contained clone, configure equivalent locale origins and preserve each locale's actual route inventory; language switching must use the observed destination behavior rather than an invented route-preserving translation switch.

## 4. Base styling and shared shell

The original loaded CSS identifies **Bootstrap 4.3.1**. Its base layout also uses custom template CSS, MeanMenu, Slick, Font Awesome, and Flaticon styles. Multiple old browser libraries are present; this is evidence about appearance and behavior, not a requirement to reproduce their dependency chain. Primary styling evidence: [site CSS](https://www.fulleverbd.com/front-end/css/style.css), [Bootstrap CSS](https://www.fulleverbd.com/front-end/css/bootstrap.min.css), and [mobile menu CSS](https://www.fulleverbd.com/front-end/css/meanmenu.min.css).

### Base tokens

| Role | Verified value |
| --- | --- |
| Main navy | `#082c4b` |
| Footer navy | `#092d4c` |
| Primary red | `#ee212b` |
| Hero control background | `#da101a` |
| Selected hero control | `#cd0d16` |
| Active main-nav background / text | `#c9dff3` / `#ff0404` |
| Body text / heading text | `#646464` / `#111111` |
| Background / light section | `#ffffff` / `#f8f8f8` |
| Home company-summary blue | `#6ac5f2` |
| Base body type | `Roboto, sans-serif`; 16px; weight 400; line-height 30px |
| Base paragraphs | bottom margin 20px |
| Base heading scale | h1 34px; h2 36px; h3 22px; h4 20px; h5 18px; h6 16px |

These are base rules. Page-specific styles override them, particularly on About. Do not enforce one font or one token palette everywhere.

Responsive base h2 sizes are 32/30/28/26px at ≤1199/991/767/575px; base h3 becomes 20px at ≤767px. Base h1 has an unusual scale: 40px at ≤1199px, 38px at ≤991px, 34px at ≤767px, 32px at ≤575px, and 30px at ≤479px. Inner-banner h1 overrides that scale to 30px at ≤991px and 28px at ≤767px. Match the winning selector rather than assuming headings shrink monotonically.

### Containers and breakpoints

Bootstrap containers have 15px left/right padding, centered margins, and these maximum widths:

| Viewport width | Maximum container width |
| --- | ---: |
| below 576px | fluid |
| 576–767px | 540px |
| 768–991px | 720px |
| 992–1199px | 960px |
| 1200–1229px | 1140px |
| 1230px and above | 1200px |

The legacy stylesheet changes the root font size: 62.5% normally, 60% at ≤1199px, 55% at ≤991px, 50% at ≤767px, 45% at ≤479px, and 40% at ≤320px. The body remains 16px. Therefore 1rem is 10px on the audited desktop, but 7.2px at the audited 390px mobile width. Preserve computed dimensions; do not convert all rem values using a 16px assumption.

### Desktop header

- Navy top strip, email at left, animated welcome text near the middle, four social links at right.
- On the audited home viewport, topbar height was 46px and the white menu row 86px. Both used 85px horizontal wrapper padding.
- Main logo source is `bd_logo-new.png`, intrinsic 384 × 84; audited desktop rendering approximately 179 × 39.
- Main links are uppercase Roboto, 15px, weight 500, line-height 15px, letter-spacing 0.5px, approximately 35px vertical and 15px horizontal padding.
- Active page has pale blue background and red text. Product dropdown is white, 250px wide, red top border, light shadow, and a short downward-to-rest entrance transition.
- Preserve actual nested menu topology, social destinations, and language flags. Do not add search, account, cart, or a sales CTA to this row.
- The stylesheet defines a sticky menu with shorter padding after scrolling; verify the actual activation threshold before implementing it.

### Mobile header

At ≤991px the desktop header is hidden and a fixed white mobile header appears. Its wrapper reserves 50px above page content; the observed bar was about 51px including border. Logo sits left; the right hamburger becomes `X` when expanded. Expanded main rows use gray `#ebebeb`, black 14px bold text, and generous vertical padding. Products has a separate `+` control that becomes `-` and reveals 12 category links. Language appears at the bottom. Both menu expansion and product expansion were tested live.

### Interior banners

Most inner routes use `.inner-page-banner`, 24px vertical padding at desktop, with a translucent red overlay `rgba(237,28,37,.7)`. White title and breadcrumbs sit above the overlay. Heading weight is 600. Preserve route-specific banner height: the audited contact banner was 151px; the representative product banner omits the usual breadcrumb row and is shorter. Do not force a fixed 151px height on every route.

### Footer

Preserve the existing three-column desktop footer: company/logo/member block; two lists of quick links; company contact/social block. It stacks on small screens. Use the monochrome logo, association logo, red short heading rules, subdued text, and navy social buttons. Default top-area padding is 100px top / 70px bottom; bottom copyright area is 25px vertical / 10px horizontal with a `#1f3d56` top border. Verify inline and page-specific overrides. The audited copyright year was 2026.

A circular return-to-top control is fixed near the lower-right corner after scrolling; inspect its trigger and smooth-scroll behavior. Keep original footer labels and destinations, including `/category/25`.

Footer headings use 24px / weight 500; their title blocks have 28px bottom margin, 22px bottom padding, and a 49 × 4px red underline. Social buttons are 47 × 42px, radius 4px, background `#1b466a`, becoming 40 × 40px at ≤767px. The late contact-paragraph override uses `#c5c4b2`. About's page-level cascade can alter shared elements, so compare its footer separately.

## 5. Home page composition

The section order is fixed:

1. Shared header.
2. Full-width artwork carousel.
3. Red synchronized six-item carousel navigation.
4. Navy manufacturing-process section.
5. Category-heading artwork and 13 category tiles.
6. Blue company-experience section with image background and About link.
7. Navy four-statistic strip.
8. Custom certification heading and card carousel.
9. Shared footer.

### Hero and synchronized controls

Six original artwork files, in order, are listed in the asset table below. There are no visible arrow or dot controls on the hero. Original `data-slick` configuration specifies one main slide, 1000ms transition speed, 2000ms autoplay delay, pause on hover, progressive image loading, and synchronization with `.slick-nav`. The control strip specifies six visible items on desktop, five on its tablet setting, three on its mobile setting, and two on its smallest setting. Confirm the script's exact breakpoint mapping before using those settings.

The first control represents the company welcome image; the other five represent glove/apparel groups. Controls use the small outlined-glove artwork, white labels, and darker selected red. Desktop control padding is 50px top, 5px horizontal, 22px bottom; icons have 20px bottom spacing. On the audited desktop, hero artwork occupied approximately 525px and controls approximately 193px. Artwork ratios differ slightly; preserve measured sizing and cropping instead of assuming every file is 1920 × 700.

The source hides separate hero text through `.big-text { display: none !important; }`. Do not duplicate the words already embedded in the images as visible headings.

### Working process

Four circular 250 × 250 source photographs with white 10px borders, red numbered badges, and linked labels. Desktop has four columns; 768–991px has two; narrower screens stack. Number badges are 55px circles positioned near the upper-right of each photograph. Process links use the four exact process routes. Desktop wrapper padding is 95px top / 65px bottom. Image hover changes the border to red and uses the original pulse treatment.

### Category tiles

The heading is image artwork `CT.png`. The 13 tiles follow the category table order, except `/category/25` appears before `/category/24` on the home page. Preserve both identical apparel labels and their distinct images/routes. Tiles use `col-lg-4 col-md-6 col-12`: three columns at ≥992px, two at 768–991px, one below 768px.

Source wrapper padding is 34px top / 85px bottom. The desktop observed tile width was 380px; legacy image-area height is 336px. Hover zooms the image and reveals a centered navy overlay, category link, and bordered action. Late CSS adds a cyan radial gradient, image width 96%, and image top margin −53px. These overrides materially affect cropping and must be matched rather than replaced with generic cards.

The final category link at the bottom points home in the reference. Preserve that destination rather than inventing a product index.

### Experience, statistics, certifications

The company-summary section has blue background and `about-bg.png` placed at the lower-right. Preserve its experience-number composition, paragraph placement, and About link. The following four statistics show 1,200 workers; 12,000 square meters; 1,00,000 dozen monthly output; and 40 million overall output. Preserve the original number formatting. The current home statistic wrapper computes to 20px padding, overriding the template's larger default.

The certification area is a newer custom component, not the old template logo strip. It has a shaped blue-gradient title banner with an orange backing shape, an Arial Black heading, a gray `#e6e9ef` background, and six white cards: SQP, GSV, FLAXA, WCA, ISO 9001, ISO 14001. Current inline styles define 240px card width, 14px corner radius, 20px track gap, and a 92px badge area. Tags are navy pills; description text is bright pink `#ff1493`. Preserve these unusual colors and small text sizes.

Certification arrows, dots, hover lift, and drag cursor are present. Track transition is 0.5s with `cubic-bezier(0.22,0.61,0.36,1)`; card hover uses a 4px upward shift and gold accent. Confirm actual paging, drag behavior, and any autoplay through live interaction before calling this component complete. Both ISO cards currently reference `ISO_14001.png`; do not silently substitute a different badge. Some images were initially unloaded during inspection; a zero initial natural size does not establish a broken asset.

Source: [live home page](https://www.fulleverbd.com/).

## 6. Inner-page templates

### About

The current [About page](https://www.fulleverbd.com/about) uses a newer visual system. It has an introduction, a two-column company copy/image area, a four-statistic gradient strip, vision image/copy and four small supporting points, three commitment cards, and a green sales CTA. Capture its complete current copy and wrapping separately; older cached About pages are not reliable layout references.

Final page-level variables include navy `#102b45`, green `#25845d`, darker green `#126a47`, red `#e32635`, background `#f5f7f6`, border `#e3e8eb`, and text `#4e6172`. Body font stack is `Inter, "Segoe UI", Roboto, Arial, sans-serif`, 16px / 28px. This declares Inter but does not prove the font file is available; reproduce the actually loaded font, not a new font download by assumption. Headings still inherit Roboto in the observed cascade; h2 was 46px / 52.9px on desktop.

Relevant rules: section padding 82px vertical; company grid `0.88fr 1.12fr`, gap 28px; cards 24px radius; copy padding 38px; stats padding 70px vertical and four columns; commitment grid three columns. Page styles use additional breakpoints at 900, 850, 600, and 560px. Preserve the winning cascade where their ranges overlap. About also affects shared typography/buttons through broad selectors; equivalent route-scoped CSS may reproduce those effects without leaking them onto other pages.

Images: `gallery/Cover.png` and `about/mission.jpg`. The sales CTA is a `mailto:` link in the current source.

### Facilities

The [facilities page](https://www.fulleverbd.com/facilities) retains the shared banner but uses its own content grid: 70px vertical / 5% horizontal section padding; `0.9fr 1.1fr` columns; 55px gap; descriptive copy and one factory photo; then four feature cells for quality, workforce, capacity, and safety. The grid becomes one column at ≤900px. Source text is 17px with 1.9 line-height and gray `#596273`; accent red is `#ed3340`. Its feature panel is white, rounded, shadowed, with four columns becoming one at ≤900px. Use the actual emoji/icons where shown.

Some stylesheet rules reference thumbnails or `.main-img` elements not observed in the current DOM. Do not add those elements just because styles exist. Main observed photo: `about/facilities.jpg`.

### Compliance

The [compliance page](https://www.fulleverbd.com/compliance) presents eight policy topics covering legal compliance, management, hours, compensation, association, child labor, discrimination, and workplace safety. Preserve order, text density, four interspersed illustrations, and the certification area following the policy content. It has the shared header/banner/footer; its content does not use the About redesign automatically.

### Working-process pages

All four use a shared process template: inner banner; main content/photo slider on the right at desktop; process-navigation sidebar on the left. DOM columns are `col-lg-8 order-lg-2` and `col-lg-4 order-lg-1`. Below desktop, preserve their DOM-driven stacking order. Wrapper padding is 100px top / 45px bottom at desktop.

Raw materials, cutting, and sewing have three source photographs each; packaging has four. Capture slide settings, text, active sidebar treatment, and image states separately. Source groups are `workingprocess/rm`, `ps`, `pro`, and `pa`. References: [raw materials](https://www.fulleverbd.com/raw-materials), [cutting](https://www.fulleverbd.com/cutting-process), [sewing](https://www.fulleverbd.com/sewing-process), [packaging](https://www.fulleverbd.com/packaging).

### Category pages

Shared banner with category heading and category breadcrumb; product grid; shared footer. Capture each card's normal state and hover overlay, label, and image association. Do not expose product titles below every image if the original reveals them only in its overlay.

Observed column classes are `col-lg-4 col-md-6 col-12 col-sm-4`. Their effective Bootstrap behavior is unusual: three columns at ≥992px, two at 768–991px, **three at 576–767px**, and one below 576px. Match the actual cascade; do not substitute the home grid's breakpoint behavior. Recheck representative widths during implementation.

### Product pages

Preserve the route-specific banner, left product viewer, right title/SKU/description, tab styling, size guide, and footer. SKU values are strings because leading zeroes are meaningful. Product preview, sprite, size-chart image, apparel sizes, and description are separate fields; titles alone are not unique identifiers.

The live [winter product example](https://www.fulleverbd.com/product/163) has a draggable handle and an image-sprite viewer, labeled as a 3D view. Its sprite CSS is 1600% wide, indicating a 16-frame strip; confirm frame count and mapping from each product's actual viewer metadata. No WebGL canvas was observed. Use the matching sprite rather than inventing a Three.js model or applying a simple CSS rotation to the flat preview. The source preview and sprite may differ; preserve source associations until they are verified.

Description paragraphs use approximately 19px line-height, black text, and justified alignment in the late source CSS. Apparel pages may use textual size lists instead of a glove sizing image. Inspect all products before accepting complete content coverage.

### Gallery

The current [gallery](https://www.fulleverbd.com/gallery) has 22 image tiles and 10 filter buttons: Show all, Factory, Product Dashboard, Office Staff, Cutting Section, Sewing Section, Finishing Section, QC Section, Buffing & Milling Section, Finished Goods Warehouse. Preserve order and group membership.

Desktop tiles are approximately one-third of the row with 8px padding. Factory filtering was tested and leaves three visible tiles. Clicking a thumbnail opens an image modal with Close and image-navigation controls; first-image next control was observed. Preserve full-image sources, modal dimensions, filter active styling, and modal navigation boundaries. Capture keyboard/backdrop behavior before implementation acceptance.

### Contact

The [contact page](https://www.fulleverbd.com/contact) uses an eight-column main region and four-column contact sidebar on desktop. The main area contains a map iframe, then an inquiry form. Sidebar includes address, sales contacts, and a contact-card action. Preserve the arrangement, contact information formatting, colored heading strips, and bordered cards.

| Field | Source name | Source type | Required |
| --- | --- | --- | --- |
| Name | `name` | text | yes |
| E-mail | `email` | email | yes |
| Phone | `phone` | text | yes |
| Subject | `subject` | text | yes |
| Comments | `comment` | textarea, seven rows | yes |

Preserve visible required markers and Send Now button. The original form uses POST with `contact.php` as its action; this does not prove its delivery behavior or the site's complete backend architecture. Do not send test inquiries to it. Implement matching visible validation and clone-owned success/error states, verifying original UI states without sending production messages.

The source map iframe declares 600 × 450; verify its rendered responsive box. View Card was tested and opens a card image popup with a Close control. Card asset path is `front-end/img/Visiting_Card.png`; availability must be confirmed after opening the popup.

## 7. Known asset map

Paths are relative to `https://www.fulleverbd.com/` unless another origin is shown. Preserve filename spelling and case. This table is a starting map, not a complete download bundle.

| Role | Source path | Intrinsic dimensions where observed |
| --- | --- | --- |
| Main logo | `front-end/img/bd_logo-new.png` | 384 × 84 |
| Footer logo | `front-end/img/bd_logo-bw.png` | 318 × 84 |
| Hero 1 | `front-end/img/slider/Fullever_Banner1.png` | 2076 × 758 |
| Hero 2 | `front-end/img/slider/Driver_gloves26.png` | 1920 × 700 |
| Hero 3 | `front-end/img/slider/Grain-Gloves.png` | 2073 × 759 |
| Hero 4 | `front-end/img/slider/FULLEVER_SPLIT_GLOVES_1920x700_150kb.jpg` | 1920 × 700 |
| Hero 5 | `front-end/img/slider/Welding-gloves2026_09.jpg` | 1900 × 700 |
| Hero 6 | `front-end/img/slider/Palm-Gloves.jpg` | 2069 × 760 |
| Hero control icon | `front-end/img/ggafp.png` | 32 × 51 |
| Process images | `front-end/img/service/rawmaterials.jpg`, `catting.jpg`, `swwim.jpg`, `Packaging.jpg` in the same directory | each 250 × 250 |
| Category heading artwork | `front-end/img/CT.png` | 1672 × 172 |
| Home company background | `front-end/img/about/about-bg.png` | capture from source |
| About profile image | `front-end/img/gallery/Cover.png` | 1024 × 1536 |
| About vision image | `front-end/img/about/mission.jpg` | 960 × 632 |
| Facilities image | `front-end/img/about/facilities.jpg` | 960 × 632 |
| Association image | `front-end/img/FLAXA.png` | 405 × 152 |
| ISO image used by both current home ISO cards | `front-end/img/ISO_14001.png` | 360 × 360 |
| Contact card | `front-end/img/Visiting_Card.png` | recheck after popup opens |
| Example product preview | `product-images/1681893067163.png` | 384 × 408 |
| Example product sprite | `product-images/16481069961617519743002120732600.jpg` | capture full strip |
| Example sizing image | `front-end/img/size/0259346360.jpg` | capture after load |

Home category tile files, in order, live under `media-library/`:

| Category ID | File |
| --- | --- |
| 23 | `wenter.png` |
| 17 | `driver.png` |
| 18 | `Grain-Gloves.png` |
| 19 | `slipt.png` |
| 20 | `walding.png` |
| 21 | `117356021.png` |
| 25 | `pant.png` |
| 24 | `jek.png` |
| 27 | `Micro-Gloves.png` |
| 29 | `0172317000.png` |
| 30 | `0000025056864_1.png` |
| 31 | `cotton_new.png` |
| 32 | `GG1_F.png` |

First twelve tile images were 500 × 596; the gardening image was 384 × 392. Do not stretch all assets to one invented aspect ratio.

Capture every page's remaining images, CSS background images, icon fonts, font files, sprites, modal images, flags, and sizing charts into a local asset manifest. Record original URL, local path, page/component usage, dimensions, and load status. Internal assets should be local in the finished clone. External social/mail links and configured map embeds retain their intended destination behavior.

## 8. Responsive and state verification

Use at least 1440 × 900, 1280 × 800, 1024 × 768, 768 × 1024, 600 × 900, 390 × 844, and 360 × 800 for implementation comparison. Only desktop 1440 × 900 and mobile 390 × 844 were visually audited here; the additional sizes are a proposed verification matrix.

Capture desktop dropdowns, sticky header, mobile open/closed menu, expanded mobile products, hero first/other slide, certification first/last position, category hover, gallery each filter/modal, representative product sprite frames, contact validation, and contact-card popup.

A global source rule at ≤1024px adds 40px top padding to `.item-img`, affecting multiple components. Mobile audit showed some horizontal overflow. Establish a stable reference and record whether each effect is persistent or a loading artifact. Strict fidelity should reproduce persistent behavior; do not claim that a repaired layout is an exact match.

Wait for the preloader, fonts, images, and slider initialization before taking baselines. Immediately after navigation, some screenshots were faded or showed uninitialized stacked slides. Those are transient loading states, not the settled page design.

## 9. Acceptance criteria

- All 146 known English URLs render correctly on direct visit and reload. Unknown IDs produce a controlled 404.
- Category counts, ordered IDs, card-to-product associations, and duplicate apparel routes match this audit or a documented newer live capture.
- All page sections, source copy, assets, translations, and interactions are captured and implemented. No placeholder products, invented content, generic replacement icons, or fabricated 3D models remain.
- Compare reference and clone in the same browser/OS, viewport, device scale, scroll position, loaded-font state, and interaction state. Freeze changing counters/sliders at the same observed state for comparison; do not mask static layout differences.
- There should be no unexplained differences in geometry, typography, artwork, or colors. A proposed automated screenshot gate is ≤0.5% differing unmasked pixels, calibrated for rendering noise; manual overlay review remains required.
- Exercise real navigation, gallery filters/modal controls, mobile expansions, product viewer, certification controls, form validation and clone-owned delivery failure/success, and return-to-top behavior.
- Build/type checks pass; internal links and local assets resolve; the clone does not call original production inquiry/analytics endpoints.
- Complete Japanese/Korean inventory and verification before describing the entire website clone as complete.

## 10. Items to resolve during implementation

1. Complete product-detail content, SKU, preview/sprite/size mapping for all 123 products.
2. Full live Japanese/Korean route, content, layout, and asset inventories.
3. Exact slider breakpoint mapping, certification paging/drag/autoplay behavior, process sliders, sticky threshold, and keyboard behavior.
4. Settled asset failures versus lazy/transient loading. The bundled `reset.css` request returned 404; several icon-font fallback URLs returned HTML. Confirm which real font files actually load.
5. Original visible contact success/error behavior and clone delivery configuration. The original backend is not available through public-page inspection.

These are verification tasks, not reasons to replace source features with approximations. The specification is ready for implementation; it is not a claim that an exact clone has already been built.
