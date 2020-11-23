BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS items (
 id TEXT PRIMARY KEY,
 category TEXT NOT NULL,
 name TEXT NOT NULL,
 label TEXT NOT NULL,
 price REAL NOT NULL
);
INSERT INTO "items" VALUES('BK001','bkfast','Muffin','MUFFIN',2.75);
INSERT INTO "items" VALUES('BK002','bkfast','Oatmeal','OATS',2.85);
INSERT INTO "items" VALUES('BK003','bkfast','Breakfast Burrito','B-BURRITO',2.8);
INSERT INTO "items" VALUES('BK004','bkfast','Breakfast Sandwich','B-SAND',2.8);
INSERT INTO "items" VALUES('BK005','bkfast','Bagel','BAGEL',1.5);
INSERT INTO "items" VALUES('BK006','bkfast','Yogurt','YOGURT',2.3);
INSERT INTO "items" VALUES('HB001','bev_hot','Coffee','COFFEE',1.99);
INSERT INTO "items" VALUES('HB002','bev_hot','Hot Tea','HOT TEA',1.99);
INSERT INTO "items" VALUES('HB003','bev_hot','Hot Cocoa','COCOA',1.99);
INSERT INTO "items" VALUES('CB001','bev_cold','Aquafina','AQUA H20',1.0);
INSERT INTO "items" VALUES('CB002','bev_cold','Life Water','LIFE H20',1.87);
INSERT INTO "items" VALUES('CB003','bev_cold','Sobe','SOBE',2.34);
INSERT INTO "items" VALUES('CB004','bev_cold','5hr Energy','5 HOUR',2.8);
INSERT INTO "items" VALUES('CB005','bev_cold','Rockstar','ROCKSTAR',2.8);
INSERT INTO "items" VALUES('CB006','bev_cold','Milk','MILK',1.87);
INSERT INTO "items" VALUES('CB007','bev_cold','Chocolate Milk','CHOC MILK',1.87);
INSERT INTO "items" VALUES('CB008','bev_cold','Juice','JUICE',1.87);
INSERT INTO "items" VALUES('DE001','deli','Noodle Cup','NOODLE CUP',1.0);
INSERT INTO "items" VALUES('DE002','deli','Soup','SOUP',2.8);
INSERT INTO "items" VALUES('DE003','deli','Small Salad','SM SALAD',2.1);
INSERT INTO "items" VALUES('DE004','deli','Large Salad','LG SALAD',5.0);
INSERT INTO "items" VALUES('DE005','deli','Deli Sand','DELI SAND',4.44);
INSERT INTO "items" VALUES('DE006','deli','Fresh Whole Fruit','FRESH FRUIT',1.0);
INSERT INTO "items" VALUES('DE007','deli','Fruit Cup','FRUIT CUP',2.3);
INSERT INTO "items" VALUES('DE008','deli','Hummus','HUMMUS',2.69);
INSERT INTO "items" VALUES('DE009','deli','Guacamole','GUAC',2.69);
INSERT INTO "items" VALUES('DE010','deli','String Cheese','STRING CHZ',0.75);
INSERT INTO "items" VALUES('DE011','deli','Veggies Snack Pack','VEGGIES',1.49);
INSERT INTO "items" VALUES('DE012','deli','Sargento Snack Pack','SARGENTO',1.49);
INSERT INTO "items" VALUES('SN001','snack','House Cookie','HOUSE COOKIE',1.64);
INSERT INTO "items" VALUES('SN002','snack','Chips','CHIPS',0.65);
INSERT INTO "items" VALUES('SN003','snack','House Baked Cookie','HOUSE COOKIE',1.64);
INSERT INTO "items" VALUES('SN004','snack','Oreo Cookie','OREO COOKIES',0.75);
INSERT INTO "items" VALUES('SN005','snack','M&M Cookie','M&M COOKIE',0.75);
INSERT INTO "items" VALUES('SN006','snack','Chips Ahoy','CHIPS AHOY',0.75);
INSERT INTO "items" VALUES('SN007','snack','Rice Krispy','RICE KRISPY',0.75);
INSERT INTO "items" VALUES('SN008','snack','Candy','CANDY',0.75);
INSERT INTO "items" VALUES('SN009','snack','Kind Bar','KIND BAR',2.49);
INSERT INTO "items" VALUES('SN010','snack','Oreo Pie','OREO PIE',2.99);
INSERT INTO "items" VALUES('CD001','condiment','Salsa','SALSA',0.0);
INSERT INTO "items" VALUES('CD002','condiment','Plain Cream Cheese','PLAIN CRM CHZ',0.75);
INSERT INTO "items" VALUES('CD003','condiment','House Cream Cheese','CREAM CHEESE',0.75);
INSERT INTO "items" VALUES('CD004','condiment','Granola','GRANOLA',0.5);
INSERT INTO "items" VALUES('CD005','condiment','Crackers','CRACKERS',0.0);
INSERT INTO "items" VALUES('CD006','condiment','Dressing','DRESSING',0.75);
COMMIT;
