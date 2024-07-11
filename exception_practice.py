class OutOfStockError(Exception):
    def __init__(self, paint_in_stock):
        self.paint_in_stock = paint_in_stock

    def __str__(self):
        item = f"{self.paint_in_stock} is not in stock"
        return item