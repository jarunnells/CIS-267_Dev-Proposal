-- =========================
-- CREATE TABLES SCRIPT
-- =========================
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS items (
 id TEXT PRIMARY KEY,
 category TEXT NOT NULL,
 name TEXT NOT NULL,
 label TEXT NOT NULL,
 price REAL NOT NULL
);
COMMIT;
