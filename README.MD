# Notes App

**Proof of Skill:** Frontend Frameworks, State Management & Authentication

A modern, full-stack **Notes Application** built with **Flask (Python)** on the backend and **Vue 3 (Vite)** on the frontend.
This project demonstrates skills in **frontend frameworks**, **authentication (JWT)**, **drag-and-drop reordering**, and **responsive UI design** using **TailwindCSS**.

---

## Features

*  User registration and login with JWT-based authentication
*  Add, edit, and delete notes
*  Drag to reorder notes (using Sortable.js)
*  Dark and Light mode toggle (persistent)
*  RESTful Flask backend with CORS support
*  Responsive Vue 3 (Vite) frontend with modular components
*  Styled with TailwindCSS for a sleek, modern UI

---

## Tech Stack

| Layer          | Technologies                                        |
| -------------- | --------------------------------------------------- |
| Frontend       | Vue 3 (Vite) + TailwindCSS + Sortable.js + Axios    |
| Backend        | Flask + Flask-CORS + PyJWT + Werkzeug (for hashing) |
| Database       | In-memory (for demo) / JSON or SQLite (optional)    |
| Authentication | JSON Web Tokens (JWT)                               |

---

## Setup Instructions

### Backend (Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate      # or venv\Scripts\activate on Windows
pip install flask flask-cors PyJWT werkzeug
python app.py
```

The backend will run on **[http://localhost:5000](http://localhost:5000)**

---

### Frontend (Vue + Vite)

```bash
cd frontend
npm install
npm run dev
```

The frontend runs on **[http://localhost:5173](http://localhost:5173)**
and connects to the backend API at **[http://localhost:5000](http://localhost:5000)**

---

## TailwindCSS Setup

Tailwind was installed and configured for this Vue project:

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

`tailwind.config.js`:

```js
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: 'class',
  theme: { extend: {} },
  plugins: [],
}
```

Add Tailwind directives to `src/style.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Dark mode is toggled by adding/removing a `dark` class to the root `<html>` element and persisted via `localStorage`.

---

## Project Structure

```
src/
├── App.vue
├── main.js
├── style.css
├── router/
│   └── index.js
├── components/
│   ├── Header.vue
│   ├── ThemeToggle.vue
│   ├── AddNoteModal.vue
│   └── NoteCard.vue
└── pages/
    ├── LoginPage.vue
    ├── RegisterPage.vue
    └── NotesPage.vue
```

---

## API Endpoints

| Method | Endpoint      | Description        | Auth |
| ------ | ------------- | ------------------ | ---- |
| POST   | `/register`   | Register new user  | ❌    |
| POST   | `/login`      | Obtain JWT token   | ❌    |
| GET    | `/notes`      | Fetch user’s notes | ✅    |
| POST   | `/notes`      | Add a new note     | ✅    |
| DELETE | `/notes/<id>` | Delete a note      | ✅    |

---

## Authentication Flow

* The user registers or logs in to receive a JWT.
* The token is stored in `localStorage` and sent with every authorized request via Axios headers.
* The backend validates tokens for protected routes using PyJWT.

---

## Validation Rules

* Notes cannot be empty
* Token required for note operations
* Duplicate usernames are prevented at registration

---

## UI Highlights

* Floating **Add Note** button — draggable and visually prominent
* Tailwind-powered grid layout for notes
* Responsive design with smooth transitions
* Dark/light theme toggle saved between sessions

---

## Skills Demonstrated

* Full-stack authentication flow (JWT)
* State management between parent/child Vue components
* Vue 3 Composition API and reactivity model
* TailwindCSS for responsive UI
* Event-based drag-and-drop using Sortable.js
* RESTful API integration and Axios interceptors
* Clean modular component-based architecture

---

## License

This project is licensed under the **MIT License**.

---

## Proof of Skill Series

This repository is part of the **Proof of Skill Series** — a collection of focused, single-day builds showcasing specific technical competencies.
Each project emphasizes one clear skillset, such as secure auth flows, frontend frameworks, or integration patterns.
The goal is to demonstrate **applied knowledge through concise, deployable examples**.
