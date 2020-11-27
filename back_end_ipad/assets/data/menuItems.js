const ITEM = (id, category, name, label, cost) => {
    this.id = id;
    this.category = category;
    this.name = name;
    this.label = label;
    this.cost = cost;
    this.info = () => {
        return `ID: ${this.id}, Category: ${this.category}, Name: ${this.name}, Label: ${this.label}, Cost: $${this.cost.toFixed(2)}`
    };
}

const items = [
    new ITEM('BK001', 'bkfast', 'Muffin', 'MUFFIN', 2.75),
    new ITEM('BK002', 'bkfast', 'House Bagel', 'BAGEL', 3.99),
    new ITEM('BK003', 'bkfast', 'Breakfast Burrito', 'B-BURRITO', 2.80),
    new ITEM('BK004', 'bkfast', 'Breakfast Sandwich', 'B-SAND', 2.80),
    new ITEM('BK005', 'bkfast', 'Bagel', 'BAGEL', 1.50),
    new ITEM('BK006', 'bkfast', 'Yogurt', 'YOGURT', 2.30),
    new ITEM('HB001', 'bev_hot', 'Coffee', 'COFFEE', 1.99),
    new ITEM('HB002', 'bev_hot', 'Hot Tea', 'HOT TEA', 1.99),
    new ITEM('HB003', 'bev_hot', 'Hot Cocoa', 'COCOA', 1.99),
    new ITEM('CB001', 'bev_cold', 'Aquafina', 'AQUA H20', 1.00),
    new ITEM('CB002', 'bev_cold', 'Life Water', 'LIFE H20', 1.87),
    new ITEM('CB003', 'bev_cold', 'Sobe', 'SOBE', 2.34),
    new ITEM('CB004', 'bev_cold', '5hr Energy', '5 HOUR', 2.80),
    new ITEM('CB005', 'bev_cold', 'Rockstar', 'ROCKSTAR', 2.80),
    new ITEM('CB006', 'bev_cold', 'Milk', 'MILK', 1.87),
    new ITEM('CB007', 'bev_cold', 'Chocolate Milk', 'CHOC MILK', 1.87),
    new ITEM('CB008', 'bev_cold', 'Juice', 'JUICE', 1.87),
    new ITEM('DE001', 'deli', 'Noodle Cup', 'NOODLE CUP', 1.00),
    new ITEM('DE002', 'deli', 'Soup', 'SOUP', 2.80),
    new ITEM('DE003', 'deli', 'Small Salad', 'SM SALAD', 2.10),
    new ITEM('DE004', 'deli', 'Large Salad', 'LG SALAD', 5.00),
    new ITEM('DE005', 'deli', 'Deli Sand', 'DELI SAND', 4.44),
    new ITEM('DE006', 'deli', 'Fresh Whole Fruit', 'FRESH FRUIT', 1.00),
    new ITEM('DE007', 'deli', 'Fruit Cup', 'FRUIT CUP', 2.30),
    new ITEM('DE008', 'deli', 'Hummus', 'HUMMUS', 2.69),
    new ITEM('DE009', 'deli', 'Guacamole', 'GUAC', 2.69),
    new ITEM('DE010', 'deli', 'String Cheese', 'STRING CHZ', 0.75),
    new ITEM('DE011', 'deli', 'Veggies Snack Pack', 'VEGGIES', 1.49),
    new ITEM('DE012', 'deli', 'Sargento Snack Pack', 'SARGENTO', 1.49),
    new ITEM('SN001', 'snack', 'House Cookie', 'HOUSE COOKIE', 1.64),
    new ITEM('SN002', 'snack', 'Chips', 'CHIPS', 0.65),
    new ITEM('SN003', 'snack', 'House Baked Cookie', 'HOUSE COOKIE', 1.64),
    new ITEM('SN004', 'snack', 'Oreo Cookie', 'OREO COOKIES', 0.75),
    new ITEM('SN005', 'snack', 'M&M Cookie', 'M&M COOKIE', 0.75),
    new ITEM('SN006', 'snack', 'Chips Ahoy', 'CHIPS AHOY', 0.75),
    new ITEM('SN007', 'snack', 'Rice Krispy', 'RICE KRISPY', 0.75),
    new ITEM('SN008', 'snack', 'Candy', 'CANDY', 0.75),
    new ITEM('SN009', 'snack', 'Kind Bar', 'KIND BAR', 2.49),
    new ITEM('SN010', 'snack', 'Oreo Pie', 'OREO PIE', 2.99),
    new ITEM('CD001', 'condiment', 'Salsa', 'SALSA', 0.00),
    new ITEM('CD002', 'condiment', 'Plain Cream Cheese', 'PLAIN CRM CHZ', 0.75),
    new ITEM('CD003', 'condiment', 'House Cream Cheese', 'CREAM CHEESE', 0.75),
    new ITEM('CD004', 'condiment', 'Granola', 'GRANOLA', 0.50),
    new ITEM('CD005', 'condiment', 'Crackers', 'CRACKERS', 0.00),
    new ITEM('CD006', 'condiment', 'Dressing', 'DRESSING', 0.75)
]
