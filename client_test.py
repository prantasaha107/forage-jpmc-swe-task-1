import unittest
from client3 import getDataPoint


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Calculate the expected dataPoint value
        expected_dataPoint = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2

        # Calling the function to get the actual dataPoint value
        actual_dataPoint = getDataPoint(quotes[0])

        # Extract the price from the tuple
        actual_calculated_price = actual_dataPoint[3]

        # Here is the assertions
        self.assertEqual(actual_calculated_price, expected_dataPoint)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Calculate the expected dataPoint value
        expected_dataPoint = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2

        # Calling the function to get the actual dataPoint value
        actual_dataPoint = getDataPoint(quotes[0])

        # Extract the price from the tuple
        actual_calculated_price = actual_dataPoint[3]

        # Here is the assertions
        self.assertEqual(actual_calculated_price, expected_dataPoint)

    # Add more test methods here to test other aspects of your code


if __name__ == '__main__':
    unittest.main()
