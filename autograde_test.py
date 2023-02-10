# DO NOT MODIFY THIS FILE

from optimal_change import optimal_change


class TestOptimalChange:
    def test_1(self):
        assert optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

    def test_2(self):
        assert optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
    
    def test_3(self):
        assert optimal_change(99.99, 100) == "The optimal change for an item that costs $99.99 with an amount paid of $100 is 1 penny."

    def test_4(self):
        assert optimal_change(53.27, 250) == "The optimal change for an item that costs $53.27 with an amount paid of $250 is 1 $100 bill, 1 $50 bill, 2 $20 bills, 1 $5 bill, 1 $1 bill, 2 quarters, 2 dimes, and 3 pennies."
    
    def test_5(self):
        assert optimal_change(23.17, 97.99) == "The optimal change for an item that costs $23.17 with an amount paid of $97.99 is 1 $50 bill, 1 $20 bill, 4 $1 bills, 3 quarters, 1 nickel, and 2 pennies."
        
    def test_6(self):
        assert optimal_change(37.78, 40) == "The optimal change for an item that costs $37.78 with an amount paid of $40 is 2 $1 bills, 2 dimes, and 2 pennies."
    
    def test_7(self):
        assert optimal_change(23.17, 97.99) == "The optimal change for an item that costs $23.17 with an amount paid of $97.99 is 1 $50 bill, 1 $20 bill, 4 $1 bills, 3 quarters, 1 nickel, and 2 pennies."
    
    def test_8(self):
        assert optimal_change(5.07, 100) == "The optimal change for an item that costs $5.07 with an amount paid of $100 is 1 $50 bill, 2 $20 bills, 4 $1 bills, 3 quarters, 1 dime, 1 nickel, and 3 pennies."
    
    def test_9(self):
        assert optimal_change(90, 100) == 'The optimal change for an item that costs $90 with an amount paid of $100 is 1 $10 bill.'

    def test_10(self):
        assert optimal_change(465.32, 1000) == "The optimal change for an item that costs $465.32 with an amount paid of $1000 is 5 $100 bills, 1 $20 bill, 1 $10 bill, 4 $1 bills, 2 quarters, 1 dime, 1 nickel, and 3 pennies."
    
    def test_11(self):
        assert optimal_change(15.95, 200) == "The optimal change for an item that costs $15.95 with an amount paid of $200 is 1 $100 bill, 1 $50 bill, 1 $20 bill, 1 $10 bill, 4 $1 bills, and 1 nickel."

    def test_12(self):
        assert optimal_change(74.19, 75) == "The optimal change for an item that costs $74.19 with an amount paid of $75 is 3 quarters, 1 nickel, and 1 penny."

    def test_13(self):
        assert optimal_change(100, 1000) == "The optimal change for an item that costs $100 with an amount paid of $1000 is 9 $100 bills."

    def test_14(self):
        assert optimal_change(113.59, 300) == "The optimal change for an item that costs $113.59 with an amount paid of $300 is 1 $100 bill, 1 $50 bill, 1 $20 bill, 1 $10 bill, 1 $5 bill, 1 $1 bill, 1 quarter, 1 dime, 1 nickel, and 1 penny."
