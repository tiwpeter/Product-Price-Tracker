
# Copilot / Agent Quick Instructions

This project is a Vite + React (TypeScript-capable) frontend using Tailwind. The repository mixes `.ts/.tsx` and `.js/.jsx` files and follows a feature-based layout under `src/features`.

- **Start dev server:** `npm run dev` (runs `vite`).
- **Build (prod):** `npm run build` — note it runs `tsc -b` first, then `vite build` (TypeScript project build step is required).
- **Preview production build:** `npm run preview`.
- **Lint:** `npm run lint` (ESLint is configured in the repo).

Key files and patterns (examples):

- App entry & routing: [src/main.tsx](src/main.tsx) — router is created with `createBrowserRouter` and `MainLayout` wraps feature routes.
- Layout: [src/components/Layout](src/components/Layout) — top-level layout and shared UI.
- Feature structure: `src/features/<feature>/{components,hooks,pages,services}` — e.g. [src/features/products](src/features/products) contains `pages`, `components`, `hooks`, and `services`.
- API surface: `src/features/*/services/*` — implement backend calls here (the current `productApi.js` is a placeholder).
- Hooks: `src/features/*/hooks/*` — local data-fetching/business-logic hooks live here and are used by pages/components.

Project-specific conventions discovered:

- Feature-first layout: Put pages, presentational components, hooks, and service modules inside the feature folder.
- Mixed JS/TS usage: Some files are `.js/.jsx` (hooks/components) while the project supports TypeScript (`.ts/.tsx`) and runs `tsc -b` during build. When adding new code prefer TypeScript for pages and central logic, but keep consistency with surrounding files.
- Router changes: Add new routes in [src/main.tsx](src/main.tsx) by adding child entries to the `router` definition.

Integration notes and actionable pointers for agents:

- Implement network calls in `src/features/products/services/productApi.js` (axios is already a dependency) and expose functions consumed by `hooks` (e.g. `useProducts`).
- When editing UI, prefer adding components under the feature's `components` folder and import them into the `pages` file used by the router.
- Keep the `layout` component as the root wrapper to preserve shared navigation/header logic.

Developer workflows and gotchas:

- Because `npm run build` runs `tsc -b`, missing or broken TypeScript references will fail the build even if Vite would compile JS files fine during dev.
- There is currently no test runner configured (no `test` script), so do not assume automated tests are present.

What I preserved from the repo: this file replaced an empty `.github/copilot-instructions.md` — no previous instructions to merge.

If anything important is missing (backend base URL, environment variables, auth flows, or CI commands), tell me where to look or provide the values and I will add them. Ready to iterate on any unclear section.
