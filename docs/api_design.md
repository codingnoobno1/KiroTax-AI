# API Design & Models

## 🔌 NEXT.JS API ROUTES (50+) `src/app/api/`
Target: 50–70 API routes

- **auth/**
  - login/route.ts
  - register/route.ts
  - logout/route.ts
- **bills/**
  - upload/
  - list/
  - parse/
  - delete/
- **gst/**
  - generate/
  - report/
  - validate/
- **templates/**
  - create/
  - train/
  - list/
- **tenders/**
  - analyze/
  - list/
- users/
- roles/
- analytics/
- export/
- notifications/
- mapper/
- ai/
- health/

## 🧱 MODELS FOLDER `src/models/`
- user.ts
- bill.ts
- gst.ts
- template.ts
- tender.ts
- analytics.ts
- role.ts
- session.ts

## 🧠 LIB FOLDER `src/lib/`
- apiClient.ts
- auth.ts
- rbac.ts
- fetcher.ts
- validators.ts
- constants.ts
- **hooks/**
  - useUser.ts
  - useBills.ts
  - useGST.ts
